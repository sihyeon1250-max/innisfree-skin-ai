import os
from flask import Flask, render_template, request, jsonify

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

# [복구] 사진 2 스타일의 상세 정보를 포함한 캐릭터 데이터베이스
SUN_TYPES = {
    'Glowy': {
        'title': '빛돌이 (Glowy)',
        'image': 'glowy.png',
        # 사진 2 스타일 태그
        'tags': '#광노화방어 #강력차단 #자외선철벽',
        # 사진 2 스타일 상세 스토리
        'story': '빛돌이는 이글거리는 태양 빛을 가장 사랑하는 에너제틱한 수호자예요. 모두가 햇볕을 피해 그늘로 숨을 때, 빛돌이는 오히려 세련된 선글라스를 고쳐 쓰고 레이스의 가장 선두에 서죠. "뜨거움은 열정의 증거일 뿐이야!" 빛돌이가 든 SPF50+의 빛나는 왕관은 강력한 자외선으로부터 당신을 완벽하게 보호해 줍니다.',
        # [기획안 반영] 상세 항목
        'status': '야외 활동이 잦고, 피부 노화 방지를 위해 강력한 자외선 차단이 최우선인 상태입니다.',
        'feature': '햇볕에 쉽게 그을리거나 잡티가 걱정되는 활동적인 피부 타입입니다.',
        'care': '[강력 차단 존] 자극 없는 고효능 선케어 라인과 강력한 UV 방패가 필요합니다.',
        'rec_btn': '빛돌이 추천 선케어 보러가기',
        'link': 'https://m.innisfree.com/kr/ko/dp/product/100331?inmPrdCatCd=SUAB'
    },
    'Hyalumi': {
        'title': '히알루미 (Hyalumi)',
        'image': 'hyalumi.png',
        'tags': '#수분충전 #촉촉유지 #속건조해결',
        'story': '뜨거운 지열과 땀방울로 가득한 마라톤 코스는 히알루미에게 마치 사막과 같아요. 하지만 걱정 마세요! 히알루미는 머리 위에 자라난 싱싱한 녹차 잎과 손에 든 물방울 지팡이로 메마른 피부에 끝없는 생명력을 불어넣거든요. "멈추지 마세요, 수분은 제가 채울게요!" 당신이 한 걸음 내디딜 때마다 히알루미는 촘촘한 수분 잠금막을 형성해줍니다.',
        'status': '피부 당김이 심하고, 선케어 단계에서도 수분 크림 같은 촉촉함을 원하는 상태입니다.',
        'feature': '건조함으로 인해 화장이 들뜨거나 피부 결이 거친 수분 부족형 타입입니다.',
        'care': '[수분 급속 충전 존] 제주 하우스의 신선한 기초 수분 라인과 수분 앰플이 필요합니다.',
        'rec_btn': '히알루미 추천 선케어 보러가기',
        'link': 'https://m.innisfree.com/kr/ko/dp/product/100510?inmPrdCatCd=SUAB'
    },
    'Tone-Po': {
        'title': '톤뽀 (Tone-Po)',
        'image': 'tonepo.png',
        'tags': '#자연톤업 #화사피부 #유수분밸런스',
        'story': '뭉게구름처럼 폭신한 파우더 퍼프를 들고 다니는 톤뽀는 변덕스러운 피부 컨디션의 마법사예요. 레이스 도중 유분으로 번들거리는 피부를 보면 톤뽀는 즉시 매직 퍼프를 휘두르죠. "번들거림은 싹, 화사함만 남겨드릴게요!" 땀과 유분을 산뜻하게 잡아주면서도 마치 조명을 켠 듯 피부에 맑은 빛을 입혀줍니다.',
        'status': '번들거림을 잡고 싶어 하며, 선크림 하나로도 화사한 피부 톤 보정을 원하는 상태입니다.',
        'feature': '유수분 밸런스가 깨지기 쉽고 칙칙한 안색을 개선하고 싶은 타입입니다.',
        'care': '[유수분 밸런스 존] 유분을 잡는 노세범 라인과 화사한 톤업 선케어를 추천합니다.',
        'rec_btn': '톤뽀 추천 선케어 보러가기',
        'link': 'https://m.innisfree.com/kr/ko/dp/product/103267?inmPrdCatCd=SUAB'
    }
}

@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    answers = data.get('answers', [])
    score_sum = sum(answers)
    
    # 3가지 결과 분기 로직
    if score_sum > 72:
        res_key = 'Glowy'
    elif score_sum > 48:
        res_key = 'Tone-Po'
    else:
        res_key = 'Hyalumi'
    
    # 상세 데이터가 포함된 객체 반환
    return jsonify(SUN_TYPES[res_key])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)