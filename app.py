import os
from flask import Flask, render_template, request, jsonify

# 현재 파일(app.py)의 절대 경로를 기준으로 폴더를 지정합니다.
base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))
# 사진 2의 캐릭터 상세 정보
SUN_TYPES = {
    'Glowy': {
        'title': '빛돌이', 'image': 'glowy.png', 'type_desc': 'Sun (강력차단형)',
        'tags': '#광노화방어 #자극민감형',
        'story': '빛돌이는 강력한 태양 빛을 사랑하는 에너제틱한 수호자예요. 세련된 선글라스로 자외선을 감시하며, 손에는 SPF50+의 빛나는 왕관을 들고 어떤 강렬한 햇볕도 당당하게 맞서죠!',
        'status': '야외 활동이 잦아 자외선에 직접 노출되는 시간이 길거나, 햇볕에 금방 붉어지는 타입입니다.',
        'feature': '잡티 고민이 시작되었거나 가장 강력한 자외선 차단 방패가 필요한 피부입니다.',
        'care': 'SPF50+/PA++++ 등급의 강력한 차단 및 비타민 성분이 함유된 선케어를 추천합니다.',
        'rec_btn': '빛돌이가 추천하는 선제품 보러가기',
        'link': 'https://m.innisfree.com/kr/ko/dp/product/100331?inmPrdCatCd=SUAB',
        'skincare_link': 'https://m.innisfree.com/kr/ko/dp/product-list/blemish-brightening?catNm=%EC%9E%A1%ED%8B%B0/%ED%94%BC%EB%B6%80%ED%86%A4&tp=2&pageNo=1',
        'solution': "당신의 피부는 자외선 노출이 많아 칙칙해지고 탄력이 떨어진 상태군요! 빛돌이가 '빛나는 왕관'으로 자외선을 완벽하게 차단하고, 맑은 피부톤과 탄력을 되찾아줄게요."
    },
    'Blocky': {
        'title': '무암이', 'image': 'blocky.png', 'type_desc': 'Stone (장벽손상형)',
        'tags': '#장벽악화 #자극초민감형',
        'story': '제주의 거친 비바람을 견딘 현무암과 치유의 시카 잎이 만나 태어났어요. 단단한 몸체로 자극을 막아주고, 손에 든 시카 잎사귀로 상처받은 피부를 따뜻하게 감싸 안아주는 든든한 보호자랍니다.',
        'status': '외부 환경에 쉽게 뒤집어지고 피부 결이 거칠어진 손상 피부 타입입니다.',
        'feature': '아무 제품이나 쓰면 따가움을 느끼는 극민감성 피부라는 특징이 있습니다.',
        'care': '시카, 판테놀 등 장벽 회복 성분이 포함된 저자극 무기자차 선케어를 추천합니다.',
        'rec_btn': '무암이가 추천하는 선제품 보러가기',
        'link': 'https://m.innisfree.com/kr/ko/dp/product/35223?inmPrdCatCd=SUAB',
        'skincare_link': 'https://m.innisfree.com/kr/ko/dp/product-list/soothing-sensitive?catNm=%EC%A7%84%EC%A0%95/%EB%AF%BC%EA%B0%90&tp=2&pageNo=1',
        'solution': "당신의 피부는 외부 자극으로 인해 민감해지고 장벽이 손상된 상태군요! 무암이가 '싱그러운 시카 잎사귀'로 피부를 진정시키고 장벽을 탄탄하게 회복시켜 줄게요."
    },
    'Powdy': {
        'title': '뭉게', 'image': 'powdy.png', 'type_desc': 'Cloud (피지불균형형)',
        'tags': '#피지뿜뿜 #밸런스붕괴형',
        'story': '제주의 푸른 하늘 위 폭신한 구름과 파우더 퍼프가 만나 탄생했어요! 매직 파우더 퍼프로 유분을 싹 잡아주어, 변덕스러운 피부 컨디션 속에서도 항상 산뜻한 공기감을 선사해 주는 캐릭터예요.',
        'status': 'T존의 번들거림이 심하고 유분으로 인해 선크림의 끈적임을 극도로 싫어하는 상태입니다.',
        'feature': '유수분 밸런스가 깨져 피부 컨디션이 구름처럼 변덕스럽습니다.',
        'care': '세범 컨트롤, 노세범 기능이 포함된 산뜻하고 보송한 선케어를 추천합니다.',
        'rec_btn': '뭉게가 추천하는 선제품 보러가기',
        'link': 'https://m.innisfree.com/kr/ko/dp/product/103267?inmPrdCatCd=SUAB',
        'skincare_link': 'https://m.innisfree.com/kr/ko/dp/product-list/pore-oilyskin-blackheads?catNm=%EB%AA%A8%EA%B3%B5/%ED%94%BC%EC%A7%80/%EB%B8%94%EB%9E%99%ED%97%A4%EB%93%9C&tp=2&pageNo=1',
        'solution': "당신의 피부는 유분이 과도하여 번들거리고 모공이 넓어진 상태군요! 뭉게가 '매직 파우더 퍼프'로 피지를 싹 잡아, 하루 종일 산뜻하고 보송한 피부 결을 선사할게요."
    },
    'Leafe': {
        'title': '이슬숲이', 'image': 'leafe.png', 'type_desc': 'Forest (수분부족형)',
        'tags': '#수분공황 #속건조형',
        'story': '깊은 제주 숲속, 맑은 수분을 간직한 나뭇잎에서 태어난 정령이에요. 머리엔 녹차 잎이 자라나고 손엔 물방울 지팡이를 들고 있죠. 건조한 피부를 보면 수분을 채워주려 먼저 발 벗고 나선답니다.',
        'status': '세안 후 당김이 심하고 속은 바짝 마른 수분 부족형 타입입니다.',
        'feature': '피부가 푸석해 보이고 메이크업이 잘 들뜨는 특징이 있습니다.',
        'care': '히알루론산 등 수분 공급 및 진정 성분 중심의 선케어가 필요합니다.',
        'rec_btn': '이슬숲이가 추천하는 선제품 보러가기',
        'link': 'https://m.innisfree.com/kr/ko/dp/product/100510?inmPrdCatCd=SUAB',
        'skincare_link': 'https://m.innisfree.com/kr/ko/dp/product-list/moisturizing-dryskin?catNm=%EC%88%98%EB%B6%84/%EB%B3%B4%EC%8A%B5/%EC%86%8D%EA%B1%B4%EC%A1%B0&tp=2&pageNo=1',
        'solution': "당신의 피부는 수분이 부족하여 메마르고 거칠어진 상태군요! 이슬숲이가 '물방울 지팡이'로 맑은 수분을 꽉 채워, 하루 종일 촉촉하고 생기 넘치는 피부로 가꿔줄게요."
    }
}

@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    score_sum = sum(data.get('answers', []))
    
    # 점수 구간별 캐릭터 매칭 (기존 로직과 통일)
    if score_sum > 75: res_key = 'Glowy'
    elif score_sum > 55: res_key = 'Powdy'
    elif score_sum > 35: res_key = 'Leafe'
    else: res_key = 'Blocky'
    
    return jsonify(SUN_TYPES[res_key])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)