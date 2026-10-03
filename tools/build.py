#!/usr/bin/env python3
# 터치톡·스마트에버 랜딩 생성기. 실행: python3 tools/build.py → index.html, assets/site.css, assets/og.html, CNAME 을 다시 만든다.
# 가격·문구·주소는 "고칠 곳"에서만 고친다. 썸네일 글자를 바꾸면 OGV 를 올리고 assets/og.html 을 1200x630 으로 찍어 og.jpg 를 바꾼다.
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ── 고칠 곳 ──
DRAFT = False             # 공개 전 초안 띠 + 검색 제외
SITE = "https://touchtok.kr"   # 끝 슬래시 없음. 구매 버튼은 SHOP(스마트에버 판매 페이지)으로 간다
OGV = 1                   # 공유 썸네일·CSS 버전
ASOF = "2026년 10월 3일"   # 가격을 확인한 날
SHOP = "https://smartever.co.kr/product/detail.html?product_no="
TT_PRICE, TT_LIST, TT3_PRICE = "406,980원", "478,800원", "199,000원"
TT_LINE = f"12개월 구독 패키지 {TT_PRICE} (예약판매 특별가 · 소비자가 {TT_LIST})"
SELLER = "판매·결제: 스마트에버 공식몰 (주)피디케이이엔티 · 고객센터 1800-6825 (평일 10~17시) · pdk@pdkent.co.kr"
NOTE = "이 페이지의 사진·영상은 AI로 만든 연출 이미지입니다. 실제 제품과 세부 표기가 다를 수 있습니다."
# ── 여기까지 ──
CSS = """:root{--bg:#fff8f6;--ink:#2b1a20;--mut:#7b6068;--pink:#f6ccd5;--rose:#cf6682;--berry:#8a2846;--line:#f0dcdf}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 Pretendard,"Apple SD Gothic Neo","Noto Sans KR","Malgun Gothic",sans-serif;word-break:keep-all;-webkit-font-smoothing:antialiased}
img,video{max-width:100%;display:block}a{color:inherit}
.w{max-width:1080px;margin:0 auto;padding:0 20px}
.draft{background:var(--ink);color:#fff;text-align:center;font-size:12px;padding:6px}
.top{position:sticky;top:0;z-index:5;background:rgba(255,248,246,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.top .w{display:flex;align-items:center;height:56px}
.logo{font-weight:800;font-size:19px;letter-spacing:-.02em;text-decoration:none;color:var(--berry)}
.top nav{margin-left:auto;display:flex;gap:18px;font-size:14px}.top nav a{text-decoration:none;color:var(--mut)}.top nav .pc{display:none}
.btn{display:inline-block;background:var(--berry);color:#fff;text-decoration:none;font-weight:700;padding:14px 24px;border-radius:999px;text-align:center}
section{padding:52px 0;border-top:1px solid var(--line)}.hero{border-top:0;padding:36px 0 44px}
.two{display:grid;gap:28px}
.eyebrow{color:var(--rose);font-weight:700;font-size:13px}
h1{font-size:38px;line-height:1.18;letter-spacing:-.03em;margin:10px 0 14px;font-weight:800}
h2{font-size:26px;line-height:1.28;letter-spacing:-.02em;margin:0 0 10px;font-weight:800}
h3{margin:0 0 4px;font-size:17px}
.lead{color:var(--mut);margin:0 0 20px;font-size:17px}
.price{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin:0 0 16px}
.price b{display:block;font-size:26px;letter-spacing:-.02em;color:var(--berry);line-height:1.3}
.fine{font-size:12.5px;color:var(--mut)}
figure{margin:0}figcaption{font-size:11.5px;color:var(--mut);margin-top:6px}
.shot{border-radius:20px;overflow:hidden;background:var(--pink)}.shot img,.shot video{width:100%;height:100%;object-fit:cover}
.a34{aspect-ratio:3/4}.a45{aspect-ratio:4/5}.a45 img{object-position:50% 62%}.a11{aspect-ratio:1/1}.v16{aspect-ratio:16/9}
.v9{aspect-ratio:9/16;max-width:340px;margin:0 auto}
.modes{list-style:none;padding:0;margin:20px 0 12px;display:grid;gap:10px}
.modes li{display:flex;gap:12px;align-items:baseline;background:#fff;border:1px solid var(--line);border-radius:14px;padding:13px 16px}
.modes .en{font-weight:800;font-size:12px;letter-spacing:.06em;color:var(--berry);width:76px;flex:none}
.modes span{color:var(--mut);font-size:14px}
ol{padding-left:20px;margin:0 0 14px}ol li{margin:6px 0}
.cards{display:grid;gap:14px;margin:22px 0 14px}
.card{display:flex;align-items:center;background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden;text-decoration:none}
.card .ph{aspect-ratio:1/1;background:var(--pink);width:112px;flex:none}.card .ph img{width:100%;height:100%;object-fit:cover}
.card .tx{padding:14px 16px}.card p{margin:0;color:var(--mut);font-size:14px}.card b{color:var(--berry)}
table{width:100%;border-collapse:separate;border-spacing:0;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;margin:20px 0}
th,td{text-align:left;padding:13px 16px;border-bottom:1px solid var(--line);font-size:15px;vertical-align:top}
th{width:36%;font-weight:600;color:var(--mut)}tr:last-child th,tr:last-child td{border-bottom:0}td b{color:var(--berry)}
details{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin-top:10px}
summary{font-weight:700;cursor:pointer}details p{margin:8px 0 0;color:var(--mut)}
footer{padding:32px 0 104px;border-top:1px solid var(--line);font-size:13px;color:var(--mut)}footer p{margin:0 0 6px}
.sticky{position:fixed;left:0;right:0;bottom:0;padding:10px 16px calc(10px + env(safe-area-inset-bottom));background:rgba(255,248,246,.95);backdrop-filter:blur(8px);border-top:1px solid var(--line);z-index:6}
.sticky .btn{display:block}
@media(min-width:800px){.top nav .pc{display:inline}.hero{padding:64px 0 72px}.two{grid-template-columns:1fr 1fr;gap:56px;align-items:center}
h1{font-size:56px}h2{font-size:34px}section{padding:84px 0}.cards{grid-template-columns:repeat(3,1fr)}.cards.c2{grid-template-columns:repeat(2,1fr);max-width:720px}
.card{display:block}.card .ph{width:auto}.sticky{display:none}footer{padding-bottom:48px}.film{max-width:880px}}
"""
def write(p, s):
    p = os.path.join(ROOT, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s); print("wrote", os.path.relpath(p, ROOT), len(s))
def head(title, desc, up):
    og = (SITE + "/" if SITE else up) + "assets/og.jpg?v=%d" % OGV
    robots = '<meta name="robots" content="noindex">' if DRAFT else ""
    draft = '<div class="draft">초안 · 공개 전 검토용</div>' if DRAFT else ""
    home = up or "./"
    canon = '<link rel="canonical" href="%s/"><meta property="og:url" content="%s/">' % (SITE, SITE) if SITE else ""
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">{robots}{canon}
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{og}">
<link rel="stylesheet" href="{up}assets/site.css?v={OGV}"></head><body>{draft}
<header class="top"><div class="w"><a class="logo" href="{home}">Touch Tok</a><nav><a class="pc" href="{up}#modes">5가지 모드</a><a href="{up}#set">구성</a><a href="{up}#price">가격</a></nav></div></header>
'''
def foot(buy, label):
    return f'''<footer><div class="w"><p>{SELLER}</p><p>{NOTE}</p><p>표시 가격은 {ASOF} 스마트에버 공식몰 기준이며 바뀔 수 있습니다.</p></div></footer>
<div class="sticky"><a class="btn" href="{buy}">{label}</a></div></body></html>'''
def fig(src, alt, cls, cap="연출 이미지", lazy=' loading="lazy"'):
    return f'<figure><div class="shot {cls}"><img src="{src}" alt="{alt}"{lazy}></div><figcaption>{cap}</figcaption></figure>'
def vid(n, cls, label):
    return f'<figure><div class="shot {cls}"><video src="img/{n}.mp4" poster="img/{n}.jpg" aria-label="{label}" autoplay muted loop playsinline preload="metadata"></video></div><figcaption>연출 영상</figcaption></figure>'
def card(img, title, text, href=""):
    tag = f'a href="{href}"' if href else "div"
    return f'<{tag} class="card"><div class="ph"><img src="{img}" alt="{title}" loading="lazy"></div><div class="tx"><h3>{title}</h3><p>{text}</p></div></{tag.split()[0]}>'
MODES = [("CLEAN", "클렌징", "하루를 닦아내는 첫 단계"), ("MASK", "마스크", "마스크팩 위에서 쓰는 모드"), ("LIFTING", "리프팅", "탄력 케어 모드"),
         ("EYE CARE", "아이케어", "눈가에 쓰는 모드"), ("COOL", "쿨링", "차갑게 마무리하는 모드")]
FAQ = [("무료 체험이 있나요?", "지금은 없습니다."),
       ("결제는 어디서 하나요?", "스마트에버 공식몰(smartever.co.kr)에서 결제합니다. 아래 버튼이 상품 페이지로 연결됩니다."),
       ("마스크팩과 겔은 언제 오나요?", "주문할 때 3개월 · 6개월 · 일괄 발송 중에서 고릅니다."),
       ("해지·환불 조건은 어떻게 되나요?", "공식몰 상품 페이지의 안내를 따릅니다. 궁금한 점은 고객센터 1800-6825(평일 10~17시)로 문의하세요."),
       ("A/S는 어떻게 받나요?", "공식 판매처 구매 기준 1년 무상 A/S입니다.")]
def index():
    buy = SHOP + "33"
    modes = "".join(f'<li><span class="en">{e}</span><div><b>{k}</b> <span>{d}</span></div></li>' for e, k, d in MODES)
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    body = f'''<main>
<section class="hero"><div class="w two"><div>
<div class="eyebrow">터치톡 뷰티 디바이스 · 12개월 구독</div>
<h1>기기 하나로<br>다섯 가지 홈케어</h1>
<p class="lead">디바이스와 PDRN 마스크팩, 부스터 수딩 겔을 함께 받는 구독 패키지입니다.</p>
<div class="price"><span class="fine">12개월 구독 패키지 · 예약판매 특별가</span><b>{TT_PRICE}</b><span class="fine">소비자가 {TT_LIST} · 스마트에버 공식몰 결제</span></div>
<a class="btn" href="{buy}">구독 패키지 보기</a>
<p class="fine" style="margin:12px 0 0">1년 무상 A/S · 5만원 이상 무료배송 · 무료 체험은 지금은 없습니다.</p></div>
{fig("img/set.webp", "터치톡 디바이스, PDRN MASK PRO, PDRN BOOSTER SOOTHING GEL", "a34", lazy="")}</div></section>
<section id="modes"><div class="w two"><div>
<h2>버튼 하나로 바꾸는<br>5가지 모드</h2>
<p class="lead">MODE 버튼으로 모드를, LEVEL 버튼으로 5단계 강도를 고릅니다.</p>
<ul class="modes">{modes}</ul><p class="fine">모드 이름은 기기에 적힌 표기 그대로입니다.</p></div>
{fig("img/device.webp", "터치톡 디바이스 정면", "a45")}</div></section>
<section id="how"><div class="w two">{vid("use", "v9", "마스크팩 위에서 터치톡을 쓰는 모습")}<div>
<h2>마스크 위에<br>터치톡</h2>
<p class="lead">PDRN MASK PRO를 붙이고, 그 위에서 터치톡을 천천히 움직입니다.</p>
<ol><li>세안 후 마스크팩을 얼굴에 붙입니다.</li><li>모드를 고르고 마스크 위에서 기기를 사용합니다.</li></ol>
<p class="fine">부스터 수딩 겔은 기기와 함께 쓰는 겔 타입 스킨케어입니다. 자세한 사용 순서와 주의사항은 제품 설명서를 따르세요.</p></div></div></section>
<section><div class="w"><h2>영상으로 보기</h2><div class="film">{vid("film", "v16", "터치톡 세트와 사용 장면")}</div></div></section>
<section id="set"><div class="w"><h2>패키지 구성</h2><p class="lead">디바이스 하나와 전용 스킨케어 두 가지입니다.</p>
<div class="cards">{card("img/device2.webp", "터치톡 디바이스", "5가지 모드 · 5단계 강도")}{card("img/mask.webp", "PDRN MASK PRO", "앰플 마스크 시트")}{card("img/gel.webp", "PDRN BOOSTER SOOTHING GEL", "겔 타입 스킨케어")}</div>
<p class="fine">사진은 연출 이미지입니다. 구성 수량은 공식몰 상품 페이지에서 확인하세요.</p></div></section>
<section id="price"><div class="w"><h2>가격과 조건</h2>
<table><tr><th>12개월 구독 패키지</th><td><b>{TT_PRICE}</b><br><span class="fine">예약판매 특별가 · 소비자가 {TT_LIST}</span></td></tr>
<tr><th>3개월 구독 패키지</th><td><b>{TT3_PRICE}</b></td></tr>
<tr><th>스킨케어 발송</th><td>3개월 · 6개월 · 일괄 중 선택</td></tr>
<tr><th>배송비</th><td>3,000원 (5만원 이상 무료)</td></tr>
<tr><th>A/S</th><td>1년 무상</td></tr>
<tr><th>무료 체험</th><td>지금은 없습니다</td></tr></table>
<a class="btn" href="{buy}">구독 패키지 보기</a>
<p class="fine" style="margin:12px 0 0">{TT_LINE}. 결제 금액과 행사 내용은 공식몰 상품 페이지가 기준입니다.</p></div></section>
<section><div class="w"><h2>자주 묻는 질문</h2>{faq}</div></section>
</main>
'''
    write("index.html", head("터치톡 | 기기 하나로 다섯 가지 홈케어", "터치톡 뷰티 디바이스와 PDRN 마스크팩·부스터 수딩 겔을 함께 받는 12개월 구독 패키지.", "") + body + foot(buy, f"구독 패키지 보기 · {TT_PRICE}"))
def og():
    write("assets/og.html", '''<!doctype html><html lang="ko"><meta charset="utf-8"><body style="margin:0;width:1200px;height:630px;display:flex;background:#fff8f6;font-family:Pretendard,'Noto Sans KR',sans-serif;color:#2b1a20;word-break:keep-all">
<div style="flex:1;padding:70px 20px 0 76px"><div style="font-size:34px;font-weight:800;color:#8a2846">Touch Tok</div>
<div style="font-size:74px;font-weight:800;line-height:1.16;letter-spacing:-3px;margin-top:64px">기기 하나로<br>다섯 가지 홈케어</div>
<div style="font-size:30px;color:#7b6068;margin-top:34px">디바이스 + PDRN 마스크팩 · 수딩 겔<br>12개월 구독 패키지</div></div>
<div style="width:470px;height:630px;position:relative"><img src="../img/set.webp" style="width:100%;height:100%;object-fit:cover"><div style="position:absolute;right:14px;bottom:10px;font-size:17px;color:#fff">연출 이미지</div></div></body></html>''')
if __name__ == "__main__":
    write("assets/site.css", CSS); index(); og()
    if SITE: write("CNAME", SITE.split("//")[1] + "\n")
