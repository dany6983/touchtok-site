#!/usr/bin/env python3
"""터치톡 사이트 정본 금지어 대조 (읽기만, 쪽을 고치지 않는다).

쓰는 법:
  python3 tools/canon_words_check.py <raytok-site>/marketing/products

- 쪽은 손목록이 아니라 `git ls-files '*.html'` 로 걸어 찾는다
- 낱말은 정본에서 읽는다: _common-forbidden.json words + touchtok.json forbidden.words
  (notice 는 통지만, 실패로 치지 않는다)
- 손님이 읽는 글자만 본다 (주석·style·script·태그 속성 제거)
- 면제는 낱말이 아니라 뜻(부정 고지꼴)에 건다. 면제 건수는 매번 찍고 상한 5건
- html lang 이 ko 가 아닌 쪽(외국어판)은 한국어 정본 낱말로 구조적으로 0 이라 [못 봄] 으로 매번 찍는다
종료 코드: 진짜 걸림 > 0 이거나 면제 > 상한 이면 1
"""
import json, os, re, subprocess, sys

EXEMPT_CAP = 5
# 법정 고지 부정꼴: 「…치료를 위한 의료기기가 아니며」「치료와는 무관」
NEG = re.compile(r"(아니며|아닙니다|아님|무관|않습니다|않으며)")
WINDOW = 40  # 낱말 뒤 몇 글자 안에 부정꼴이 있어야 면제


def visible(h: str) -> str:
    h = re.sub(r"<!--[\s\S]*?-->", " ", h)
    h = re.sub(r"<style[\s\S]*?</style>", " ", h, flags=re.I)
    h = re.sub(r"<script[\s\S]*?</script>", " ", h, flags=re.I)
    h = re.sub(r"<[^>]+>", " ", h)
    h = re.sub(r"&[a-z]+;|&#\d+;", " ", h, flags=re.I)
    return re.sub(r"\s+", " ", h)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    prod = sys.argv[1]
    common = json.load(open(os.path.join(prod, "_common-forbidden.json"), encoding="utf-8"))
    tt = json.load(open(os.path.join(prod, "touchtok.json"), encoding="utf-8"))["forbidden"]
    words = sorted(set(common.get("words", [])) | set(tt.get("words", [])))
    notice = sorted(set(common.get("notice", [])) | set(tt.get("notice", [])))
    nonhangul = [w for w in words if not re.search(r"[가-힣]", w)]

    root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
    pages = subprocess.check_output(["git", "ls-files", "*.html"], cwd=root, text=True).split()
    # 디스크 걸음 셈을 나란히 — 이름 거르개 없이 .html 로 끝나는 것 전부. 둘이 다르면 멈춘다
    disk = sorted(os.path.relpath(os.path.join(d, f), root) for d, ds, fs in os.walk(root)
                  if not (ds.__setitem__(slice(None), [x for x in ds if x not in (".git", "node_modules")]))
                  for f in fs if f.endswith(".html"))

    # 언어 폴더는 손목록 말고 build.py LANGS 에서 읽는다 (코드, lang, 이름, "폴더/")
    LANG_DIRS = set(re.findall(r'\("[a-z]+", "[^"]+", "[^"]+", "([a-z]+)/"\)', open(os.path.join(root, "tools", "build.py"), encoding="utf-8").read()))
    if len(LANG_DIRS) < 5:
        sys.exit(f"build.py LANGS 를 못 읽음: {LANG_DIRS}")
    real, exempt, notes, blind, nolang, mismatch = [], [], [], [], [], []
    for p in pages:
        raw = open(os.path.join(root, p), encoding="utf-8").read()
        t = visible(raw)
        lang = re.search(r'<html[^>]*\blang="([^"]+)"', raw)
        top = p.split("/")[0] if "/" in p else ""
        if not lang:
            nolang.append(p)  # 밝히지 않음 — 한국어로 가정하지 않는다
        elif not lang.group(1).lower().startswith("ko"):
            blind.append(f"{p}({lang.group(1)})")
        if lang and top in LANG_DIRS and not lang.group(1).lower().startswith(top):
            mismatch.append(f"{p}({lang.group(1)})")  # /en/ 길인데 lang=ko 같은 것
        for w in words:
            for m in re.finditer(re.escape(w), t):
                tail = t[m.end(): m.end() + WINDOW]
                (exempt if NEG.search(tail) else real).append((p, w, t[max(0, m.start() - 20): m.end() + WINDOW]))
        for w in notice:
            c = t.count(w)
            if c:
                notes.append((p, w, c))

    print(f"쪽 {len(pages)} (git ls-files) · 디스크 걸음 {len(disk)} · words {len(words)} · notice {len(notice)}")
    for p, w, ctx in real:
        print(f"  ✗ 걸림 {p} 「{w}」 … {ctx}")
    for p, w, ctx in exempt:
        print(f"  · 면제(부정 고지꼴) {p} 「{w}」 … {ctx}")
    for p, w, c in notes:
        print(f"  ○ 통지 {p} 「{w}」 ×{c}")
    print(f"[못 봄] 한국어 아닌 쪽(html lang) {len(blind)}개 — 정본 낱말 중 비한글은 {nonhangul} 뿐이라 이 쪽들의 0건은 「깨끗」이 아니라 「안 봄」: {', '.join(blind)}")
    print(f"[밝히지 않음] html lang 없는 쪽 {len(nolang)}개" + (f": {', '.join(nolang)}" if nolang else ""))
    print(f"[길↔lang 어긋남] {len(mismatch)}개" + (f": {', '.join(mismatch)}" if mismatch else ""))
    print(f"결과: 걸림 {len(real)} · 면제 {len(exempt)}/{EXEMPT_CAP} · 통지 {sum(c for *_, c in notes)}")
    if sorted(pages) != disk:
        print(f"  ✗ 쪽 셈 불일치 — ls-files 에만: {sorted(set(pages) - set(disk))} · 디스크에만: {sorted(set(disk) - set(pages))}")
    if real or len(exempt) > EXEMPT_CAP or sorted(pages) != disk or nolang or mismatch:
        sys.exit(1)


if __name__ == "__main__":
    main()
