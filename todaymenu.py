import random
from flask import Flask, jsonify

todaymenu = Flask(__name__)

@todaymenu.route('/random_menu',methods=['POST'])
def random_menu():
    factor = '''라면
    김밥
    떡볶이
    냉면
    막국수
    비빔국수
    콩국수
    설렁탕
    닭볶음탕
    감자탕
    부대찌개
    곱창전골
    순댓국
    칼국수
    매운탕
    김치찌개
    된장찌개
    해물탕
    제육볶음
    불고기
    보쌈
    족발
    오돌뼈
    치킨
    닭갈비
    찜닭
    아구찜
    쭈꾸미
    낙지
    간장게장
    곱창볶음
    만두
    백반
    쌈밥
    갈비탕
    해장국
    소바
    라멘
    우동
    초밥
    카레
    텐동
    덮밥
    돈까스
    연어회
    참치회
    광어회
    회
    오꼬노미야끼
    탕수육
    짜장면
    짬뽕
    훠궈
    마라탕
    양꼬치
    양갈비
    소고기
    갈비
    양념갈비
    삼겹살
    목살
    갈매기살
    가브리살
    뒷고기
    곱창
    막창
    순대볶음
    순대
    오리고기
    스테이크
    피자
    파스타
    햄버거
    쌀국수
    샌드위치
    샐러드
    타코
    뷔페'''

    factor = factor.split('\n')
    
    rm = random.choice(factor)
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                   "basicCard": {
                       "title": "",
                       "description": '오늘은 ☠️' + rm + '☠️',
                       "thumbnail": {
                           "imageUrl": ""
                       },
                       "buttons": [
                           {
                               "action": "webLink",
                               "label": "주변 " + random.choice(factor) + "맛집 검색하기!",
                               "webLinkUrl": "https://map.naver.com/v5/search/" + rm
                           }            
                        ]
                    }
                }
            ]
        }
    }
    
    return jsonify(res)
                          
if __name__ == '__main__':
    todaymenu.run(host='0.0.0.0',port=5000,debug=True)
