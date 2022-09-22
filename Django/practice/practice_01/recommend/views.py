from django.shortcuts import render
from random import choice, sample
import requests
from datetime import date, datetime

# 저녁 메뉴 추천
def recommend_today_dinner(request):
    # 한식 메뉴 추천
    hansik_menu_list = ['부대찌개', '비빔밥', '감자탕', '불고기', '닭갈비']
    hansik_menu_images = {
        '부대찌개': 'http://www.newstap.co.kr/news/photo/202009/118343_196725_1049.jpg',
        '비빔밥': 'https://health.chosun.com/site/data/img_dir/2021/01/27/2021012702508_0.jpg',
        '감자탕': 'https://health.chosun.com/site/data/img_dir/2021/01/26/2021012602424_0.jpg',
        '불고기': 'https://oktoday.co.kr/web/product/big/202007/aa8dd777c4ab1bcd12d8a86bd449feba.jpg',
        '닭갈비': 'https://recipe1.ezmember.co.kr/cache/recipe/2019/10/30/33398b219faa7448ed4130b8b70e18c01.jpg',
    }
    hansik_menu = choice(hansik_menu_list)
    hansik_img = hansik_menu_images[hansik_menu]

    # 양식 메뉴 추천
    yangsik_menu_list = ['피자', '파스타', '햄버거', '스테이크']
    yangsik_menu_images = {
        '피자': 'https://image.newdaily.co.kr/site/data/img/2022/02/24/2022022400156_0.jpg',
        '파스타': 'https://images.chosun.com/resizer/w8wiCcDB5clwPSo5t-6I1rzaQLg=/960x575/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/HS2MWHN32OMYMSDYNGYRIZCXNI.jpg',
        '햄버거': 'https://biz.chosun.com/resizer/e_hRq82103yFIU6IWerqAJme8To=/616x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/PDA6T744P5BLTDWSLFXHTGMVSM.png',
        '스테이크': 'https://cdn.huffingtonpost.kr/news/photo/201811/77299_146809.jpeg',
    }
    yangsik_menu = choice(yangsik_menu_list)
    yangsik_img = yangsik_menu_images[yangsik_menu]

    # 중식 메뉴 추천
    jungsik_menu_list = ['짜장면', '짬뽕', '탕수육', '마라탕']
    jungsik_menu_images = {
        '짜장면': 'https://dimg.donga.com/wps/NEWS/IMAGE/2017/04/14/83849831.2.jpg',
        '짬뽕': 'https://recipe1.ezmember.co.kr/cache/recipe/2017/10/22/aaeb2a235b89ac305ba919e33da2e6331.jpg',
        '탕수육': 'https://i2.wp.com/starkaraokeuiuc.net/wp-content/uploads/2017/09/K-11.jpg?fit=639%2C409&ssl=1',
        '마라탕': 'https://w.namu.la/s/9029a4a5a86c93f71db711af4e0971506f8b3e1af25f94af24f9ff0f9a00da9afaa094621c3ee467ece96398fb324690c8eb9b79254511ea402e5d1f7ebd45a4aaf0764e0d4f4109eb2deef84cd0478a24b94b1013be7d7223133ea3215a1ac63ddfdad954d61e59208c5f325cadfdb9',
    }
    jungsik_menu = choice(jungsik_menu_list)
    jungsik_img = jungsik_menu_images[jungsik_menu]
    

    context = {
        'hansik_menu': hansik_menu,
        'hansik_img': hansik_img,
        'yangsik_menu': yangsik_menu,
        'yangsik_img': yangsik_img,
        'jungsik_menu': jungsik_menu,
        'jungsik_img': jungsik_img,
    }

    return render(request, 'today_dinner.html', context)



# 로또 번호 추천
def recommend_lotto(request):
    # 로또 API를 통해 이번주 로또 당첨 번호 가져오기
    # 현재 토요일 밤 9시라면, 다음 회차의 로또 api가 새로 업데이트됨
    # 데이터베이스에서 drwNo값 가져와서 해당 회차의 api끌어오기
    if date.today().weekday() == 5 and datetime.now().hour >= 9:
        pass
    
    drwNo = '1033'
    r = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + drwNo).json()



    recommend_nums_ranks = []   # 5줄

    # (당첨 번호와 일치하는 추천 번호 개수, 보너스 일치 여부) 반환
    def check(recommend_nums, lotto_nums, lotto_bonus):
        cnt = 0
        for num in recommend_nums:
            if num in lotto_nums:
                cnt += 1

        return (cnt, True if lotto_bonus in recommend_nums else False)

    # 5줄 뽑기
    for i in range(5):
        # 1~45까지의 숫자 중 6개 뽑기
        nums = sample(range(1, 45 + 1), 6)
        
        # 1033회차 로또 당첨 번호
        lotto_1033_nums = [3, 11, 15, 29, 35, 44]
        lotto_1033_bonus = 10

        # 1033회차 등수
        cnt, bonus = check(nums, lotto_1033_nums, lotto_1033_bonus)
        order = chr(i + 65)
        if cnt == 6:
            recommend_nums_ranks.append([order] + nums + ['1등'])
        elif cnt == 5:
            if bonus:
                recommend_nums_ranks.append([order] + nums + ['2등'])
                continue
            recommend_nums_ranks.append([order] + nums + ['3등'])
        elif cnt == 4:
            recommend_nums_ranks.append([order] + nums + ['4등'])
        elif cnt == 3:
            recommend_nums_ranks.append([order] + nums + ['5등'])
        else:
            recommend_nums_ranks.append([order] + nums + ['꽝'])


    context = {
        'recommend_nums_ranks': recommend_nums_ranks,
        'lotto_1033_nums': lotto_1033_nums,
        'lotto_1033_bonus': lotto_1033_bonus,
    }

    return render(request, 'lotto.html', context)
