#!/usr/bin/env python3
# 터치톡 랜딩 생성기. 실행: python3 tools/build.py → index.html(한국어), en/ ja/ zh/ es/ vi/, assets/site.css, assets/og.html, CNAME 을 다시 만든다.
# 가격·주소는 "고칠 곳"에서, 문구는 그 아래 T(언어별 문구표)에서만 고친다. 한국어 문구를 바꾸면 다른 언어의 같은 칸도 함께 바꾼다.
# 썸네일 글자를 바꾸면 OGV 를 올리고 assets/og.html 을 1200x630 으로 찍어 og.jpg 를 바꾼다.
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ── 고칠 곳 ──
DRAFT = False             # 공개 전 초안 띠 + 검색 제외
SITE = "https://touchtok.kr"   # 끝 슬래시 없음. 구매 버튼은 SHOP(스마트에버 판매 페이지)으로 간다
OGV = 4                   # 공유 썸네일·CSS 버전
SHOP = "https://smartever.co.kr/product/detail.html?product_no="
P12, PLIST, P3 = "406,980", "478,800", "199,000"   # 12개월 판매가, 소비자가, 3개월 판매가 (숫자만)
# 언어: (코드, html lang, 버튼에 보이는 이름, 폴더). 맨 앞이 기본(한국어). 언어를 빼거나 더하려면 여기와 T 를 같이 고친다.
LANGS = [("ko", "ko", "한국어", ""), ("en", "en", "English", "en/"), ("ja", "ja", "日本語", "ja/"),
         ("zh", "zh-Hans", "简体中文", "zh/"), ("es", "es", "Español", "es/"), ("vi", "vi", "Tiếng Việt", "vi/")]
# ── 여기까지 ──
SELLER_ID = "(주)피디케이이엔티"
T = {}
T["ko"] = dict(
    title="터치톡 | 기기 하나로 다섯 가지 홈케어",
    desc="터치톡 뷰티 디바이스와 PDRN 마스크팩·부스터 수딩 겔을 함께 받는 12개월 구독 패키지.",
    nav_modes="5가지 모드", nav_set="구성", nav_price="가격",
    eyebrow="터치톡 뷰티 디바이스 · 12개월 구독", h1="기기 하나로<br>다섯 가지 홈케어",
    lead="디바이스와 PDRN 마스크팩, 부스터 수딩 겔을 함께 받는 구독 패키지입니다.",
    price_cap="12개월 구독 패키지 · 예약판매 특별가", price_sub="소비자가 {plist} · 스마트에버 공식몰 결제",
    cta="구독 패키지 보기", hero_fine="1년 무상 A/S · 5만원 이상 무료배송 · 무료 체험은 지금은 없습니다.", shop_note="",
    alt_set="터치톡 디바이스, PDRN MASK PRO, PDRN BOOSTER SOOTHING GEL", cap_img="연출 이미지", cap_vid="연출 영상",
    modes_h2="버튼 하나로 바꾸는<br>5가지 모드", modes_lead="전원 버튼을 길게 눌러 켜고, MODE 버튼으로 모드를, LEVEL 버튼으로 5단계 강도를 고릅니다.",
    modes=[("클렌징", "세안 후 물기를 닦고 사용합니다. 온열과 양이온을 쓰는 모드."), ("마스크", "마스크팩을 붙인 위에서 사용합니다. 음이온과 EMS를 쓰는 모드."), ("리프팅", "RF·EMS와 레드·그린 라이트를 함께 쓰는 모드. 주 2~3회 사용을 권장합니다."), ("아이케어", "눈가에 맞춰 RF·EMS 강도를 조절한 모드."), ("쿨링", "냉각과 블루 라이트로 마무리하는 모드.")],
    modes_note="모드 이름은 기기에 적힌 표기 그대로입니다.", alt_device="터치톡 디바이스 정면",
    vid_use="마스크팩 위에서 터치톡을 쓰는 모습", how_h2="마스크 위에<br>터치톡",
    how_lead="PDRN MASK PRO를 붙이고, 그 위에서 터치톡을 천천히 움직입니다.",
    steps=["세안 후 마스크팩을 얼굴에 붙입니다.", "모드를 고르고 마스크 위에서 기기를 사용합니다."],
    how_fine="부스터 수딩 겔은 기기와 함께 쓰는 겔 타입 스킨케어입니다. 자세한 사용 순서와 주의사항은 제품 설명서를 따르세요.",
    film_h2="영상으로 보기", vid_film="터치톡 세트와 사용 장면",
    set_h2="패키지 구성", set_lead="디바이스 하나와 전용 스킨케어 두 가지입니다.",
    c_dev="터치톡 디바이스", c_dev_p="5가지 모드 · 5단계 강도", c_mask_p="앰플 마스크 시트", c_gel_p="겔 타입 스킨케어",
    set_note="사진은 연출 이미지입니다. 구성 수량은 공식몰 상품 페이지에서 확인하세요.",
    price_h2="가격과 조건", r12="12개월 구독 패키지", r12_sub="예약판매 특별가 · 소비자가 {plist}", r3="3개월 구독 패키지",
    r_send="스킨케어 발송", r_send_v="3개월 · 6개월 · 일괄 중 선택", r_ship="배송비", r_ship_v="3,000원 (5만원 이상 무료)",
    r_as="A/S", r_as_v="1년 무상", r_trial="무료 체험", r_trial_v="지금은 없습니다",
    price_fine="12개월 구독 패키지 {p12} (예약판매 특별가 · 소비자가 {plist}). 결제 금액과 행사 내용은 공식몰 상품 페이지가 기준입니다.",
    faq_h2="자주 묻는 질문",
    faq=[("무료 체험이 있나요?", "지금은 없습니다."),
         ("결제는 어디서 하나요?", "스마트에버 공식몰(smartever.co.kr)에서 결제합니다. 아래 버튼이 상품 페이지로 연결됩니다."),
         ("마스크팩과 겔은 언제 오나요?", "주문할 때 3개월 · 6개월 · 일괄 발송 중에서 고릅니다."),
         ("해지·환불 조건은 어떻게 되나요?", "공식몰 상품 페이지의 안내를 따릅니다. 궁금한 점은 고객센터 1800-6825(평일 10~17시)로 문의하세요."),
         ("A/S는 어떻게 받나요?", "공식 판매처 구매 기준 1년 무상 A/S입니다.")],
    seller="판매·결제: 스마트에버 공식몰 {sid} · 고객센터 1800-6825 (평일 10~17시) · pdk@pdkent.co.kr",
    note="이 페이지의 사진·영상은 AI로 만든 연출 이미지입니다. 실제 제품과 세부 표기가 다를 수 있습니다.",
    asof="표시 가격은 2026년 10월 3일 스마트에버 공식몰 기준이며 바뀔 수 있습니다.", sticky="구독 패키지 보기 · {p12}")
T["en"] = dict(
    title="Touch Tok | One device, five home-care modes",
    desc="A 12-month subscription package: the Touch Tok beauty device with PDRN sheet masks and booster soothing gel.",
    nav_modes="5 modes", nav_set="What's inside", nav_price="Price",
    eyebrow="Touch Tok beauty device · 12-month subscription", h1="One device,<br>five home-care modes",
    lead="A subscription package that brings you the device together with PDRN sheet masks and booster soothing gel.",
    price_cap="12-month subscription package · pre-order price", price_sub="List price {plist} · Checkout at the Smartever official store",
    cta="See the package", hero_fine="1-year free after-sales service · Free shipping over ₩50,000 · No free trial at this time.",
    shop_note="The official store is in Korean and lists shipping within Korea.",
    alt_set="Touch Tok device, PDRN MASK PRO, PDRN BOOSTER SOOTHING GEL", cap_img="Staged image", cap_vid="Staged video (captions in Korean)",
    modes_h2="Five modes,<br>one button", modes_lead="Press and hold the power button to turn it on, pick a mode with the MODE button, then one of five intensity levels with the LEVEL button.",
    modes=[("Cleansing", "Use on clean, dry skin after washing. Uses warmth and positive ions."), ("Mask", "Use over a sheet mask. Uses negative ions and EMS."), ("Lifting", "Combines RF, EMS and red and green light. Recommended 2–3 times a week."), ("Eye care", "RF and EMS levels adjusted for the eye area."), ("Cooling", "Cooling and blue light to finish.")],
    modes_note="Mode names are shown exactly as printed on the device.", alt_device="Front of the Touch Tok device",
    vid_use="Using Touch Tok over a sheet mask", how_h2="Touch Tok,<br>over your mask",
    how_lead="Apply PDRN MASK PRO, then glide Touch Tok slowly over it.",
    steps=["After cleansing, apply the sheet mask to your face.", "Choose a mode and use the device over the mask."],
    how_fine="The booster soothing gel is a gel-type skincare product used together with the device. For the full routine and precautions, follow the product manual.",
    film_h2="Watch the video", vid_film="The Touch Tok set and how it is used",
    set_h2="What's in the package", set_lead="One device and two dedicated skincare products.",
    c_dev="Touch Tok device", c_dev_p="5 modes · 5 intensity levels", c_mask_p="Ampoule sheet mask", c_gel_p="Gel-type skincare",
    set_note="Photos are staged images. Check the official store's product page for quantities.",
    price_h2="Price and terms", r12="12-month subscription package", r12_sub="Pre-order price · list price {plist}", r3="3-month subscription package",
    r_send="Skincare delivery", r_send_v="Choose 3 months, 6 months, or all at once", r_ship="Shipping", r_ship_v="₩3,000 (free over ₩50,000, within Korea)",
    r_as="After-sales service", r_as_v="Free for 1 year", r_trial="Free trial", r_trial_v="Not available at this time",
    price_fine="12-month subscription package {p12} (pre-order price · list price {plist}). The official store's product page is the reference for the final amount and promotions.",
    faq_h2="Frequently asked questions",
    faq=[("Is there a free trial?", "Not at this time."),
         ("Where do I pay?", "At the Smartever official store (smartever.co.kr). The button below opens the product page. The store is in Korean."),
         ("When do the masks and gel arrive?", "When ordering, you choose delivery over 3 months, 6 months, or all at once."),
         ("What are the cancellation and refund terms?", "They follow the notice on the official store's product page. For questions, contact customer service at 1800-6825 (weekdays 10:00–17:00, Korea time)."),
         ("How do I get after-sales service?", "Purchases from the official seller come with 1 year of free after-sales service."),
         ("Do you ship overseas?", "The official store currently lists shipping within Korea. If you are ordering from abroad, please check the product page first.")],
    seller="Sales and payment: Smartever official store, {sid} · Customer service 1800-6825 (weekdays 10:00–17:00, Korea time) · pdk@pdkent.co.kr",
    note="Photos and videos on this page are staged images created with AI. Details may differ from the actual product.",
    asof="Prices are as listed on the Smartever official store on October 3, 2026 and may change.", sticky="See the package · {p12}")
T["ja"] = dict(
    title="Touch Tok｜1台で5つのホームケア",
    desc="Touch Tok美容デバイスとPDRNシートマスク、ブースタースージングジェルがセットになった12か月サブスクリプションパッケージ。",
    nav_modes="5つのモード", nav_set="セット内容", nav_price="価格",
    eyebrow="Touch Tok 美容デバイス · 12か月サブスクリプション", h1="1台で<br>5つのホームケア",
    lead="デバイスとPDRNシートマスク、ブースタースージングジェルを一緒に受け取れるサブスクリプションパッケージです。",
    price_cap="12か月サブスクリプションパッケージ · 予約販売特別価格", price_sub="定価 {plist} · Smartever公式ストアで決済",
    cta="パッケージを見る", hero_fine="1年間無償アフターサービス · ₩50,000以上で送料無料 · 無料体験は現在ありません。",
    shop_note="公式ストアは韓国語のサイトで、配送は韓国国内と表示されています。",
    alt_set="Touch Tok デバイス、PDRN MASK PRO、PDRN BOOSTER SOOTHING GEL", cap_img="イメージ画像", cap_vid="イメージ動画（字幕は韓国語）",
    modes_h2="ボタンひとつで切り替える<br>5つのモード", modes_lead="電源ボタンを長押しして電源を入れ、MODEボタンでモードを、LEVELボタンで5段階の強さを選びます。",
    modes=[("クレンジング", "洗顔後、水気を拭き取ってから使います。温熱とプラスイオンを使うモード。"), ("マスク", "シートマスクの上から使います。マイナスイオンとEMSを使うモード。"), ("リフティング", "RF・EMSとレッド・グリーンライトを組み合わせたモード。週2〜3回の使用がおすすめです。"), ("アイケア", "目元に合わせてRF・EMSの強さを調整したモード。"), ("クーリング", "冷却とブルーライトで仕上げるモード。")],
    modes_note="モード名はデバイスに記載された表記のままです。", alt_device="Touch Tok デバイス正面",
    vid_use="シートマスクの上からTouch Tokを使う様子", how_h2="マスクの上から<br>Touch Tok",
    how_lead="PDRN MASK PROを貼り、その上でTouch Tokをゆっくり動かします。",
    steps=["洗顔後、シートマスクを顔に貼ります。", "モードを選び、マスクの上からデバイスを使います。"],
    how_fine="ブースタースージングジェルは、デバイスと一緒に使うジェルタイプのスキンケアです。詳しい使用手順と注意事項は取扱説明書に従ってください。",
    film_h2="動画で見る", vid_film="Touch Tokセットと使用シーン",
    set_h2="パッケージ内容", set_lead="デバイス1台と専用スキンケア2種です。",
    c_dev="Touch Tok デバイス", c_dev_p="5つのモード · 5段階の強さ", c_mask_p="アンプルシートマスク", c_gel_p="ジェルタイプのスキンケア",
    set_note="写真はイメージです。数量は公式ストアの商品ページでご確認ください。",
    price_h2="価格と条件", r12="12か月サブスクリプションパッケージ", r12_sub="予約販売特別価格 · 定価 {plist}", r3="3か月サブスクリプションパッケージ",
    r_send="スキンケアの発送", r_send_v="3か月 · 6か月 · 一括から選択", r_ship="送料", r_ship_v="₩3,000（₩50,000以上で無料、韓国国内）",
    r_as="アフターサービス", r_as_v="1年間無償", r_trial="無料体験", r_trial_v="現在ありません",
    price_fine="12か月サブスクリプションパッケージ {p12}（予約販売特別価格 · 定価 {plist}）。お支払い金額とキャンペーン内容は公式ストアの商品ページが基準です。",
    faq_h2="よくある質問",
    faq=[("無料体験はありますか？", "現在ありません。"),
         ("どこで決済しますか？", "Smartever公式ストア（smartever.co.kr）で決済します。下のボタンから商品ページに移動します。ストアは韓国語です。"),
         ("マスクとジェルはいつ届きますか？", "注文時に3か月・6か月・一括発送から選びます。"),
         ("解約・返金の条件は？", "公式ストアの商品ページの案内に従います。ご不明な点はカスタマーセンター 1800-6825（平日10〜17時、韓国時間）までお問い合わせください。"),
         ("アフターサービスは受けられますか？", "公式販売店でのご購入の場合、1年間無償です。"),
         ("海外発送はできますか？", "公式ストアには現在、韓国国内配送と表示されています。海外からご注文の際は、先に商品ページでご確認ください。")],
    seller="販売・決済：Smartever公式ストア {sid} · カスタマーセンター 1800-6825（平日10〜17時、韓国時間）· pdk@pdkent.co.kr",
    note="このページの写真・動画はAIで作成したイメージです。実際の製品と細部の表記が異なる場合があります。",
    asof="表示価格は2026年10月3日時点のSmartever公式ストアの価格で、変更される場合があります。", sticky="パッケージを見る · {p12}")
T["zh"] = dict(
    title="Touch Tok｜一台仪器，五种居家护理",
    desc="Touch Tok 美容仪搭配 PDRN 面膜与舒缓凝胶的 12 个月订阅套装。",
    nav_modes="5 种模式", nav_set="套装内容", nav_price="价格",
    eyebrow="Touch Tok 美容仪 · 12 个月订阅", h1="一台仪器<br>五种居家护理",
    lead="美容仪与 PDRN 面膜、舒缓凝胶一起送达的订阅套装。",
    price_cap="12 个月订阅套装 · 预售特价", price_sub="标价 {plist} · 在 Smartever 官方商城付款",
    cta="查看订阅套装", hero_fine="1 年免费售后 · 满 ₩50,000 免运费 · 目前没有免费试用。",
    shop_note="官方商城为韩语网站，目前显示为韩国境内配送。",
    alt_set="Touch Tok 美容仪、PDRN MASK PRO、PDRN BOOSTER SOOTHING GEL", cap_img="示意图", cap_vid="示意视频（韩语字幕）",
    modes_h2="一键切换<br>5 种模式", modes_lead="长按电源键开机，用 MODE 键选择模式，用 LEVEL 键选择 5 档强度。",
    modes=[("清洁", "洁面后擦干水分再使用。使用温热与正离子的模式。"), ("面膜", "敷着面膜使用。使用负离子与 EMS 的模式。"), ("提拉", "结合 RF、EMS 与红光、绿光的模式。建议每周使用 2～3 次。"), ("眼部护理", "针对眼周调整 RF 与 EMS 强度的模式。"), ("冷却", "用冷却与蓝光收尾的模式。")],
    modes_note="模式名称与仪器上的标注一致。", alt_device="Touch Tok 美容仪正面",
    vid_use="在面膜上使用 Touch Tok", how_h2="敷上面膜<br>再用 Touch Tok",
    how_lead="敷上 PDRN MASK PRO，再用 Touch Tok 在面膜上缓慢移动。",
    steps=["洁面后将面膜敷在脸上。", "选择模式，在面膜上使用仪器。"],
    how_fine="舒缓凝胶是与仪器搭配使用的凝胶型护肤品。详细使用步骤和注意事项请参照产品说明书。",
    film_h2="观看视频", vid_film="Touch Tok 套装与使用场景",
    set_h2="套装内容", set_lead="一台仪器和两款专用护肤品。",
    c_dev="Touch Tok 美容仪", c_dev_p="5 种模式 · 5 档强度", c_mask_p="安瓶面膜", c_gel_p="凝胶型护肤品",
    set_note="图片为示意图。数量请以官方商城商品页为准。",
    price_h2="价格与条件", r12="12 个月订阅套装", r12_sub="预售特价 · 标价 {plist}", r3="3 个月订阅套装",
    r_send="护肤品发货", r_send_v="可选 3 个月、6 个月或一次性发货", r_ship="运费", r_ship_v="₩3,000（满 ₩50,000 免运费，韩国境内）",
    r_as="售后服务", r_as_v="1 年免费", r_trial="免费试用", r_trial_v="目前没有",
    price_fine="12 个月订阅套装 {p12}（预售特价 · 标价 {plist}）。付款金额与活动内容以官方商城商品页为准。",
    faq_h2="常见问题",
    faq=[("有免费试用吗？", "目前没有。"),
         ("在哪里付款？", "在 Smartever 官方商城（smartever.co.kr）付款。点击下方按钮进入商品页。商城为韩语。"),
         ("面膜和凝胶什么时候送到？", "下单时可选 3 个月、6 个月或一次性发货。"),
         ("退订和退款条件是什么？", "以官方商城商品页的说明为准。如有疑问，请联系客服 1800-6825（工作日 10–17 点，韩国时间）。"),
         ("如何获得售后服务？", "在官方销售渠道购买，可享 1 年免费售后。"),
         ("可以寄到海外吗？", "官方商城目前显示为韩国境内配送。海外下单前，请先在商品页确认。")],
    seller="销售与付款：Smartever 官方商城 {sid} · 客服 1800-6825（工作日 10–17 点，韩国时间）· pdk@pdkent.co.kr",
    note="本页图片和视频为 AI 制作的示意图，细节标注可能与实物不同。",
    asof="所示价格为 2026 年 10 月 3 日 Smartever 官方商城的价格，可能变动。", sticky="查看订阅套装 · {p12}")
T["es"] = dict(
    title="Touch Tok | Un dispositivo, cinco modos de cuidado en casa",
    desc="Paquete de suscripción de 12 meses: el dispositivo de belleza Touch Tok con mascarillas PDRN y gel calmante booster.",
    nav_modes="5 modos", nav_set="Qué incluye", nav_price="Precio",
    eyebrow="Dispositivo de belleza Touch Tok · Suscripción de 12 meses", h1="Un dispositivo,<br>cinco modos de cuidado en casa",
    lead="Un paquete de suscripción que incluye el dispositivo junto con mascarillas PDRN y gel calmante booster.",
    price_cap="Paquete de suscripción de 12 meses · precio de preventa", price_sub="Precio de lista {plist} · Pago en la tienda oficial Smartever",
    cta="Ver el paquete", hero_fine="1 año de servicio posventa gratuito · Envío gratis desde ₩50,000 · Por ahora no hay prueba gratuita.",
    shop_note="La tienda oficial está en coreano e indica envío dentro de Corea.",
    alt_set="Dispositivo Touch Tok, PDRN MASK PRO, PDRN BOOSTER SOOTHING GEL", cap_img="Imagen de muestra", cap_vid="Video de muestra (subtítulos en coreano)",
    modes_h2="Cinco modos,<br>un solo botón", modes_lead="Mantén pulsado el botón de encendido, elige el modo con el botón MODE y uno de los cinco niveles de intensidad con el botón LEVEL.",
    modes=[("Limpieza", "Úsalo con la piel limpia y seca tras lavar el rostro. Usa calor e iones positivos."), ("Mascarilla", "Úsalo sobre la mascarilla. Usa iones negativos y EMS."), ("Lifting", "Combina RF, EMS y luz roja y verde. Se recomienda 2–3 veces por semana."), ("Contorno de ojos", "RF y EMS ajustados para la zona de los ojos."), ("Frío", "Frío y luz azul para terminar.")],
    modes_note="Los nombres de los modos aparecen tal como están impresos en el dispositivo.", alt_device="Parte frontal del dispositivo Touch Tok",
    vid_use="Uso de Touch Tok sobre la mascarilla", how_h2="Touch Tok,<br>sobre la mascarilla",
    how_lead="Aplica PDRN MASK PRO y desliza Touch Tok lentamente sobre ella.",
    steps=["Después de limpiar el rostro, aplica la mascarilla.", "Elige un modo y usa el dispositivo sobre la mascarilla."],
    how_fine="El gel calmante booster es un producto de cuidado en gel que se usa junto con el dispositivo. Para la rutina completa y las precauciones, sigue el manual del producto.",
    film_h2="Ver el video", vid_film="El set Touch Tok y cómo se usa",
    set_h2="Qué incluye el paquete", set_lead="Un dispositivo y dos productos de cuidado específicos.",
    c_dev="Dispositivo Touch Tok", c_dev_p="5 modos · 5 niveles de intensidad", c_mask_p="Mascarilla de ampolla", c_gel_p="Cuidado en gel",
    set_note="Las fotos son imágenes de muestra. Consulta las cantidades en la página del producto de la tienda oficial.",
    price_h2="Precio y condiciones", r12="Paquete de suscripción de 12 meses", r12_sub="Precio de preventa · precio de lista {plist}", r3="Paquete de suscripción de 3 meses",
    r_send="Envío del cuidado de la piel", r_send_v="A elegir: 3 meses, 6 meses o todo de una vez", r_ship="Envío", r_ship_v="₩3,000 (gratis desde ₩50,000, dentro de Corea)",
    r_as="Servicio posventa", r_as_v="Gratis durante 1 año", r_trial="Prueba gratuita", r_trial_v="No disponible por ahora",
    price_fine="Paquete de suscripción de 12 meses {p12} (precio de preventa · precio de lista {plist}). El importe final y las promociones son los de la página del producto en la tienda oficial.",
    faq_h2="Preguntas frecuentes",
    faq=[("¿Hay prueba gratuita?", "Por ahora no."),
         ("¿Dónde se paga?", "En la tienda oficial Smartever (smartever.co.kr). El botón de abajo abre la página del producto. La tienda está en coreano."),
         ("¿Cuándo llegan las mascarillas y el gel?", "Al hacer el pedido eliges envío en 3 meses, 6 meses o todo de una vez."),
         ("¿Cuáles son las condiciones de cancelación y reembolso?", "Las que indica la página del producto en la tienda oficial. Si tienes dudas, contacta con atención al cliente: 1800-6825 (días laborables, 10:00–17:00, hora de Corea)."),
         ("¿Cómo funciona el servicio posventa?", "Las compras al vendedor oficial incluyen 1 año de servicio posventa gratuito."),
         ("¿Envían al extranjero?", "La tienda oficial indica actualmente envío dentro de Corea. Si compras desde otro país, confírmalo antes en la página del producto.")],
    seller="Venta y pago: tienda oficial Smartever, {sid} · Atención al cliente 1800-6825 (días laborables, 10:00–17:00, hora de Corea) · pdk@pdkent.co.kr",
    note="Las fotos y los videos de esta página son imágenes de muestra creadas con IA. Los detalles pueden diferir del producto real.",
    asof="Los precios corresponden a la tienda oficial Smartever al 3 de octubre de 2026 y pueden cambiar.", sticky="Ver el paquete · {p12}")
T["vi"] = dict(
    title="Touch Tok | Một thiết bị, năm chế độ chăm sóc tại nhà",
    desc="Gói đăng ký 12 tháng: thiết bị làm đẹp Touch Tok kèm mặt nạ PDRN và gel làm dịu booster.",
    nav_modes="5 chế độ", nav_set="Gói gồm gì", nav_price="Giá",
    eyebrow="Thiết bị làm đẹp Touch Tok · Gói đăng ký 12 tháng", h1="Một thiết bị,<br>năm chế độ chăm sóc tại nhà",
    lead="Gói đăng ký gồm thiết bị cùng mặt nạ PDRN và gel làm dịu booster.",
    price_cap="Gói đăng ký 12 tháng · giá đặt trước", price_sub="Giá niêm yết {plist} · Thanh toán tại cửa hàng chính thức Smartever",
    cta="Xem gói đăng ký", hero_fine="Bảo hành miễn phí 1 năm · Miễn phí vận chuyển từ ₩50,000 · Hiện chưa có dùng thử miễn phí.",
    shop_note="Cửa hàng chính thức dùng tiếng Hàn và hiện ghi là giao hàng trong Hàn Quốc.",
    alt_set="Thiết bị Touch Tok, PDRN MASK PRO, PDRN BOOSTER SOOTHING GEL", cap_img="Hình minh họa", cap_vid="Video minh họa (phụ đề tiếng Hàn)",
    modes_h2="Năm chế độ,<br>một nút bấm", modes_lead="Nhấn giữ nút nguồn để bật máy, chọn chế độ bằng nút MODE và một trong năm mức cường độ bằng nút LEVEL.",
    modes=[("Làm sạch", "Dùng sau khi rửa mặt và lau khô. Chế độ dùng nhiệt ấm và ion dương."), ("Mặt nạ", "Dùng trên mặt nạ giấy. Chế độ dùng ion âm và EMS."), ("Nâng cơ", "Kết hợp RF, EMS với ánh sáng đỏ và xanh lá. Khuyên dùng 2–3 lần mỗi tuần."), ("Chăm sóc mắt", "RF và EMS được điều chỉnh cho vùng quanh mắt."), ("Làm mát", "Làm mát và ánh sáng xanh dương để kết thúc.")],
    modes_note="Tên chế độ được ghi đúng như in trên thiết bị.", alt_device="Mặt trước của thiết bị Touch Tok",
    vid_use="Dùng Touch Tok trên mặt nạ giấy", how_h2="Touch Tok<br>trên mặt nạ",
    how_lead="Đắp PDRN MASK PRO rồi di chuyển Touch Tok chậm rãi trên mặt nạ.",
    steps=["Sau khi rửa mặt, đắp mặt nạ lên mặt.", "Chọn chế độ và dùng thiết bị trên mặt nạ."],
    how_fine="Gel làm dịu booster là sản phẩm dưỡng da dạng gel dùng cùng thiết bị. Về trình tự sử dụng chi tiết và lưu ý, vui lòng làm theo hướng dẫn sử dụng sản phẩm.",
    film_h2="Xem video", vid_film="Bộ Touch Tok và cách sử dụng",
    set_h2="Gói gồm những gì", set_lead="Một thiết bị và hai sản phẩm dưỡng da chuyên dụng.",
    c_dev="Thiết bị Touch Tok", c_dev_p="5 chế độ · 5 mức cường độ", c_mask_p="Mặt nạ ampoule", c_gel_p="Dưỡng da dạng gel",
    set_note="Ảnh là hình minh họa. Vui lòng xem số lượng tại trang sản phẩm của cửa hàng chính thức.",
    price_h2="Giá và điều kiện", r12="Gói đăng ký 12 tháng", r12_sub="Giá đặt trước · giá niêm yết {plist}", r3="Gói đăng ký 3 tháng",
    r_send="Giao sản phẩm dưỡng da", r_send_v="Chọn 3 tháng, 6 tháng hoặc giao một lần", r_ship="Phí vận chuyển", r_ship_v="₩3,000 (miễn phí từ ₩50,000, trong Hàn Quốc)",
    r_as="Bảo hành", r_as_v="Miễn phí 1 năm", r_trial="Dùng thử miễn phí", r_trial_v="Hiện chưa có",
    price_fine="Gói đăng ký 12 tháng {p12} (giá đặt trước · giá niêm yết {plist}). Số tiền thanh toán và chương trình khuyến mãi căn cứ theo trang sản phẩm của cửa hàng chính thức.",
    faq_h2="Câu hỏi thường gặp",
    faq=[("Có dùng thử miễn phí không?", "Hiện chưa có."),
         ("Thanh toán ở đâu?", "Tại cửa hàng chính thức Smartever (smartever.co.kr). Nút bên dưới mở trang sản phẩm. Cửa hàng dùng tiếng Hàn."),
         ("Khi nào nhận mặt nạ và gel?", "Khi đặt hàng, bạn chọn giao trong 3 tháng, 6 tháng hoặc giao một lần."),
         ("Điều kiện hủy và hoàn tiền thế nào?", "Theo thông báo tại trang sản phẩm của cửa hàng chính thức. Nếu có thắc mắc, vui lòng liên hệ chăm sóc khách hàng 1800-6825 (ngày thường 10:00–17:00, giờ Hàn Quốc)."),
         ("Bảo hành thế nào?", "Bảo hành miễn phí 1 năm khi mua tại nhà bán chính thức."),
         ("Có giao hàng ra nước ngoài không?", "Cửa hàng chính thức hiện ghi là giao hàng trong Hàn Quốc. Nếu đặt từ nước ngoài, vui lòng kiểm tra trước tại trang sản phẩm.")],
    seller="Bán hàng và thanh toán: cửa hàng chính thức Smartever, {sid} · Chăm sóc khách hàng 1800-6825 (ngày thường 10:00–17:00, giờ Hàn Quốc) · pdk@pdkent.co.kr",
    note="Ảnh và video trên trang này là hình minh họa được tạo bằng AI. Chi tiết có thể khác với sản phẩm thật.",
    asof="Giá hiển thị theo cửa hàng chính thức Smartever ngày 3/10/2026 và có thể thay đổi.", sticky="Xem gói đăng ký · {p12}")
MODE_EN = ["CLEAN", "MASK", "LIFTING", "EYE CARE", "COOL"]   # 기기에 적힌 표기
CSS = """:root{--bg:#fff8f6;--ink:#2b1a20;--mut:#7b6068;--pink:#f6ccd5;--rose:#cf6682;--berry:#8a2846;--line:#f0dcdf}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 Pretendard,"Apple SD Gothic Neo","Noto Sans KR","Malgun Gothic",sans-serif;word-break:keep-all;-webkit-font-smoothing:antialiased}
img,video{max-width:100%;display:block}a{color:inherit}
.w{max-width:1080px;margin:0 auto;padding:0 20px}
.draft{background:var(--ink);color:#fff;text-align:center;font-size:12px;padding:6px}
.top{position:sticky;top:0;z-index:5;background:rgba(255,248,246,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.top .w{display:flex;align-items:center;height:56px}
.logo{font-weight:800;font-size:19px;letter-spacing:-.02em;text-decoration:none;color:var(--berry);white-space:nowrap}
.top nav{margin-left:auto;display:flex;gap:18px;font-size:14px}.top nav a{text-decoration:none;color:var(--mut);white-space:nowrap}.top nav .pc{display:none}
.lang{position:relative;margin:0 0 0 14px;padding:0;border:0;background:none;border-radius:0}
.lang summary{list-style:none;display:flex;align-items:center;gap:6px;font-weight:600;font-size:13px;border:1px solid var(--line);border-radius:999px;padding:6px 12px;background:#fff;white-space:nowrap}
.lang summary::-webkit-details-marker{display:none}.lang summary::after{content:"▾";font-size:11px;color:var(--mut)}
.lang div{position:absolute;right:0;top:calc(100% + 8px);min-width:150px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:6px;box-shadow:0 12px 30px rgba(43,26,32,.12)}
.lang a{display:block;padding:9px 12px;border-radius:9px;text-decoration:none;font-size:14px}.lang a[aria-current]{background:var(--bg);font-weight:700;color:var(--berry)}
.btn{display:inline-block;background:var(--berry);color:#fff;text-decoration:none;font-weight:700;padding:14px 24px;border-radius:999px;text-align:center}
section{padding:52px 0;border-top:1px solid var(--line)}
.hero{position:relative;border-top:0;padding:0;color:#fff;background:#1a1016;overflow:hidden}
.hbg img{position:absolute;left:0;bottom:-22vw;width:100%;height:auto;max-width:none;-webkit-mask-image:linear-gradient(180deg,transparent 0,#000 24%);mask-image:linear-gradient(180deg,transparent 0,#000 24%)}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(22,10,20,.92) 0%,rgba(22,10,20,.78) 32%,rgba(22,10,20,.2) 54%,rgba(22,10,20,0) 72%,rgba(22,10,20,.5) 100%)}
.hero .w{position:relative;z-index:1;min-height:700px;min-height:calc(100svh - 56px);padding-top:28px;padding-bottom:90vw}
.hero .eyebrow{color:#ffc4d2}.hero .lead{color:rgba(255,255,255,.9);margin-bottom:16px}
.hero .price{background:rgba(255,255,255,.13);border-color:rgba(255,255,255,.3);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);margin:0}
.hero .price b{color:#fff}.hero .price .fine{color:rgba(255,255,255,.85)}
.hero .btn{display:none;background:#fff;color:var(--berry)}.hero>.w>.fine{display:none;color:rgba(255,255,255,.82)}
.hcap{position:absolute;right:12px;bottom:80px;z-index:1;font-size:11px;color:rgba(255,255,255,.75)}
.setfig{max-width:520px;margin:0 0 6px}
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
.mrow{list-style:none;padding:0 20px 4px;margin:22px -20px 12px;display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding:0 20px;-webkit-overflow-scrolling:touch;scrollbar-width:none}
.mrow::-webkit-scrollbar{display:none}
.mrow li{flex:0 0 64%;max-width:260px;scroll-snap-align:start;background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden;padding-bottom:14px}
.mrow .shot{border-radius:0;aspect-ratio:9/16}
.mrow .en{display:block;font-weight:800;font-size:12px;letter-spacing:.06em;color:var(--berry);margin:12px 14px 0}
.mrow b{display:block;margin:0 14px;font-size:16px}
.mrow p{margin:4px 14px 0;color:var(--mut);font-size:13.5px;line-height:1.5}
ol{padding-left:20px;margin:0 0 14px}ol li{margin:6px 0}
.cards{display:grid;gap:14px;margin:22px 0 14px}
.card{display:flex;align-items:center;background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden;text-decoration:none}
.card .ph{aspect-ratio:1/1;background:var(--pink);width:112px;flex:none}.card .ph img{width:100%;height:100%;object-fit:cover}
.card .tx{padding:14px 16px}.card p{margin:0;color:var(--mut);font-size:14px}.card b{color:var(--berry)}
table{width:100%;border-collapse:separate;border-spacing:0;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;margin:20px 0}
th,td{text-align:left;padding:13px 16px;border-bottom:1px solid var(--line);font-size:15px;vertical-align:top}
th{width:36%;font-weight:600;color:var(--mut)}tr:last-child th,tr:last-child td{border-bottom:0}td b{color:var(--berry)}
.faq details{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin-top:10px}
summary{font-weight:700;cursor:pointer}.faq details p{margin:8px 0 0;color:var(--mut)}
footer{padding:32px 0 104px;border-top:1px solid var(--line);font-size:13px;color:var(--mut)}footer p{margin:0 0 6px}
.sticky{position:fixed;left:0;right:0;bottom:0;padding:10px 16px calc(10px + env(safe-area-inset-bottom));background:rgba(255,248,246,.95);backdrop-filter:blur(8px);border-top:1px solid var(--line);z-index:6}
.sticky .btn{display:block}
html:lang(en) body,html:lang(es) body,html:lang(vi) body{font-family:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
html:lang(en) h1,html:lang(es) h1,html:lang(vi) h1{font-size:33px;letter-spacing:-.02em}
html:lang(ja) body{font-family:"Hiragino Sans","Yu Gothic UI",Meiryo,"Noto Sans JP","Noto Sans CJK JP",sans-serif;word-break:normal;line-break:strict}
html:lang(zh) body{font-family:"PingFang SC","Microsoft YaHei","Noto Sans SC","Noto Sans CJK SC",sans-serif;word-break:normal}
@media(min-width:800px){.top nav .pc{display:inline}.hero::after{background:linear-gradient(180deg,rgba(22,10,20,.9) 0%,rgba(22,10,20,.62) 26%,rgba(22,10,20,.12) 44%,rgba(22,10,20,0) 74%,rgba(22,10,20,.45) 100%)}
.hero .w{min-height:0;padding-top:52px;padding-bottom:38.5vw;text-align:center}
.hbg img{bottom:0}.hero h1 br{display:none}.hero .lead{max-width:640px;margin:0 auto 20px}
.hbuy{display:flex;justify-content:center;align-items:center;gap:14px}.hero .price{text-align:left;padding:10px 18px}.hero .btn{display:inline-block}
.hero>.w>.fine{display:block;position:absolute;left:20px;right:20px;bottom:18px;margin:0}.hcap{bottom:12px}.two{grid-template-columns:1fr 1fr;gap:56px;align-items:center}
h1{font-size:56px}h2{font-size:34px}section{padding:84px 0}.cards{grid-template-columns:repeat(3,1fr)}
html:lang(en) h1,html:lang(es) h1,html:lang(vi) h1{font-size:40px}html:lang(ja) h1{font-size:50px}
.mrow{margin:28px 0 12px;padding:0;display:grid;grid-template-columns:repeat(5,1fr);overflow:visible}.mrow li{max-width:none}
.card{display:block}.card .ph{width:auto}.sticky{display:none}footer{padding-bottom:48px}.film{max-width:880px}}
"""
GLOBE = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/></svg>'
def write(p, s):
    p = os.path.join(ROOT, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s); print("wrote", os.path.relpath(p, ROOT), len(s))
def won(code, n):
    return n + "원" if code == "ko" else "₩" + n
def text(code):
    """언어별 문구표에 가격을 채워 돌려준다."""
    v = dict(p12=won(code, P12), plist=won(code, PLIST), p3=won(code, P3), sid=SELLER_ID)
    f = lambda x: x.format(**v) if isinstance(x, str) else [f(i) for i in x] if isinstance(x, list) else tuple(f(i) for i in x)
    return {k: f(x) for k, x in T[code].items()}, v
def head(code, hl, path, t, up):
    og = (SITE + "/" if SITE else up) + "assets/og.jpg?v=%d" % OGV
    robots = '<meta name="robots" content="noindex">' if DRAFT else ""
    draft = '<div class="draft">초안 · 공개 전 검토용</div>' if DRAFT else ""
    canon = ""
    if SITE:
        canon = '<link rel="canonical" href="%s/%s"><meta property="og:url" content="%s/%s">' % (SITE, path, SITE, path)
        canon += "".join('<link rel="alternate" hreflang="%s" href="%s/%s">' % (h, SITE, p) for _, h, _, p in LANGS)
        canon += '<link rel="alternate" hreflang="x-default" href="%s/">' % SITE
    cur = [n for c, _, n, _ in LANGS if c == code][0]
    links = "".join('<a href="%s" lang="%s"%s>%s</a>' % ((up + p) or "./", h, ' aria-current="page"' if c == code else "", n) for c, h, n, p in LANGS)
    return f'''<!doctype html>
<html lang="{hl}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t["title"]}</title><meta name="description" content="{t["desc"]}">{robots}{canon}
<meta property="og:type" content="website"><meta property="og:title" content="{t["title"]}"><meta property="og:description" content="{t["desc"]}"><meta property="og:image" content="{og}">
<link rel="stylesheet" href="{up}assets/site.css?v={OGV}"></head><body>{draft}
<header class="top"><div class="w"><a class="logo" href="./">Touch Tok</a><nav><a class="pc" href="#modes">{t["nav_modes"]}</a><a class="pc" href="#set">{t["nav_set"]}</a><a href="#price">{t["nav_price"]}</a></nav>
<details class="lang"><summary aria-label="Language">{GLOBE}{cur}</summary><div>{links}</div></details></div></header>
'''
def fig(src, alt, cls, cap, lazy=' loading="lazy"'):
    return f'<figure><div class="shot {cls}"><img src="{src}" alt="{alt}"{lazy}></div><figcaption>{cap}</figcaption></figure>'
def vid(up, n, cls, label, cap):
    return f'<figure><div class="shot {cls}"><video src="{up}img/{n}.mp4" poster="{up}img/{n}.jpg" aria-label="{label}" autoplay muted loop playsinline preload="metadata"></video></div><figcaption>{cap}</figcaption></figure>'
def card(img, title, body):
    return f'<div class="card"><div class="ph"><img src="{img}" alt="{title}" loading="lazy"></div><div class="tx"><h3>{title}</h3><p>{body}</p></div></div>'
def page(code, hl, path):
    t, v = text(code)
    up = "../" if path else ""
    buy = SHOP + "33"
    modes = "".join(f'<li><div class="shot"><video data-auto src="{up}img/mode-{e.lower().replace(" ", "")}.mp4" poster="{up}img/mode-{e.lower().replace(" ", "")}.jpg" aria-label="{e} · {k}" muted loop playsinline preload="none"></video></div><span class="en">{e}</span><b>{k}</b><p>{d}</p></li>' for e, (k, d) in zip(MODE_EN, t["modes"]))
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    steps = "".join(f"<li>{s}</li>" for s in t["steps"])
    shop = f' {t["shop_note"]}' if t["shop_note"] else ""
    body = f'''<main>
<section class="hero"><picture class="hbg"><source media="(min-width:800px)" srcset="{up}img/hero-wide.webp"><img src="{up}img/hero-tall.webp" alt="{t["alt_set"]}"></picture><span class="hcap">{t["cap_img"]}</span>
<div class="w">
<div class="eyebrow">{t["eyebrow"]}</div>
<h1>{t["h1"].replace("<br>", " <br>")}</h1>
<p class="lead">{t["lead"]}</p>
<div class="hbuy"><div class="price"><span class="fine">{t["price_cap"]}</span><b>{v["p12"]}</b><span class="fine">{t["price_sub"]}</span></div><a class="btn" href="{buy}">{t["cta"]}</a></div>
<p class="fine">{t["hero_fine"]}{shop}</p></div></section>
<section id="modes"><div class="w">
<h2>{t["modes_h2"]}</h2>
<p class="lead">{t["modes_lead"]}</p>
<ul class="mrow">{modes}</ul><p class="fine">{t["cap_vid"].replace("（","(").split("(")[0].strip()} · {t["modes_note"]}</p></div></section>
<section id="how"><div class="w two">{vid(up, "use", "v9", t["vid_use"], t["cap_vid"])}<div>
<h2>{t["how_h2"]}</h2>
<p class="lead">{t["how_lead"]}</p>
<ol>{steps}</ol>
<p class="fine">{t["how_fine"]}</p></div></div></section>
<section><div class="w"><h2>{t["film_h2"]}</h2><div class="film">{vid(up, "film", "v16", t["vid_film"], t["cap_vid"])}</div></div></section>
<section id="set"><div class="w"><h2>{t["set_h2"]}</h2><p class="lead">{t["set_lead"]}</p>
<div class="setfig">{fig(up + "img/set.webp", t["alt_set"], "a34", t["cap_img"])}</div>
<div class="cards">{card(up + "img/device2.webp", t["c_dev"], t["c_dev_p"])}{card(up + "img/mask.webp", "PDRN MASK PRO", t["c_mask_p"])}{card(up + "img/gel.webp", "PDRN BOOSTER SOOTHING GEL", t["c_gel_p"])}</div>
<p class="fine">{t["set_note"]}</p></div></section>
<section id="price"><div class="w"><h2>{t["price_h2"]}</h2>
<table><tr><th>{t["r12"]}</th><td><b>{v["p12"]}</b><br><span class="fine">{t["r12_sub"]}</span></td></tr>
<tr><th>{t["r3"]}</th><td><b>{v["p3"]}</b></td></tr>
<tr><th>{t["r_send"]}</th><td>{t["r_send_v"]}</td></tr>
<tr><th>{t["r_ship"]}</th><td>{t["r_ship_v"]}</td></tr>
<tr><th>{t["r_as"]}</th><td>{t["r_as_v"]}</td></tr>
<tr><th>{t["r_trial"]}</th><td>{t["r_trial_v"]}</td></tr></table>
<a class="btn" href="{buy}">{t["cta"]}</a>
<p class="fine" style="margin:12px 0 0">{t["price_fine"]}{shop}</p></div></section>
<section class="faq"><div class="w"><h2>{t["faq_h2"]}</h2>{faq}</div></section>
</main>
<footer><div class="w"><p>{t["seller"]}</p><p>{t["note"]}</p><p>{t["asof"]}</p></div></footer>
<div class="sticky"><a class="btn" href="{buy}">{t["sticky"]}</a></div>
<script>(function(){{var v=[].slice.call(document.querySelectorAll("video[data-auto]"));if(!("IntersectionObserver" in window)){{v.forEach(function(x){{x.controls=true}});return}}var o=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{var p=e.target.play();if(p&&p.catch)p.catch(function(){{}})}}else e.target.pause()}})}},{{threshold:.5}});v.forEach(function(x){{o.observe(x)}})}})()</script></body></html>'''
    write(path + "index.html", head(code, hl, path, t, up) + body)
def og():
    write("assets/og.html", '''<!doctype html><html lang="ko"><meta charset="utf-8"><body style="margin:0;width:1200px;height:630px;display:flex;background:#fff8f6;font-family:Pretendard,'Noto Sans KR',sans-serif;color:#2b1a20;word-break:keep-all">
<div style="flex:1;padding:70px 20px 0 76px"><div style="font-size:34px;font-weight:800;color:#8a2846">Touch Tok</div>
<div style="font-size:74px;font-weight:800;line-height:1.16;letter-spacing:-3px;margin-top:64px">기기 하나로<br>다섯 가지 홈케어</div>
<div style="font-size:30px;color:#7b6068;margin-top:34px">디바이스 + PDRN 마스크팩 · 수딩 겔<br>12개월 구독 패키지</div></div>
<div style="width:470px;height:630px;position:relative"><img src="../img/set.webp" style="width:100%;height:100%;object-fit:cover"><div style="position:absolute;right:14px;bottom:10px;font-size:17px;color:#fff">연출 이미지</div></div></body></html>''')
if __name__ == "__main__":
    write("assets/site.css", CSS); og()
    for code, hl, _, path in LANGS: page(code, hl, path)
    if SITE: write("CNAME", SITE.split("//")[1] + "\n")
