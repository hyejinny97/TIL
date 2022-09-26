from multiprocessing import context
from django.shortcuts import render
from random import choice

# Create your views here.
def index(request):

    return render(request, "index.html")


def is_odd_even(request, number):
    if number == 0:
        rst = 0
    elif number % 2 == 0:
        rst = "짝수"
    else:
        rst = "홀수"

    content = {
        "number": number,
        "rst": rst,
    }
    return render(request, "is_odd_even.html", content)


def calculate(request, number1, number2):
    context = {
        "number1": number1,
        "number2": number2,
        "plus": number1 + number2,
        "minus": number1 - number2,
        "multiply": number1 * number2,
        "devide": number1 // number2,
    }

    return render(request, "calculate.html", context)


def past_life(request):
    return render(request, "past_life.html")


def past_life_result(request):
    animals = [
        [
            "사람",
            "https://w.namu.la/s/35be0f3ce9bf565a62c286c28a7b2be69b32ecf09a6d907d112e8138db7718b03e7e67a0ffa1ee3f3724507ea37193945675c6df5c93e125e36fe5dbc9259fd69567bf3de12469c315f2185f1b79dcce17dbb53959b8a0aab4ad9fb920280a5b9491eca4a0ba21d85b444533a7b9a11f",
        ],
        ["말", "http://www.mypetnews.net/news/photo/201402/503_324_397.jpg"],
        [
            "돼지",
            "https://www.korea.kr/goNewsRes/attaches/editor/2019.01/27/20190127224207298_MVBHMYGV.jpg",
        ],
        [
            "소",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Cow_%28Fleckvieh_breed%29_Oeschinensee_Slaunger_2009-07-07.jpg/250px-Cow_%28Fleckvieh_breed%29_Oeschinensee_Slaunger_2009-07-07.jpg",
        ],
        ["쥐", "http://www.astronomer.rocks/news/photo/201802/83932_1698_5038.jpg"],
        [
            "유니콘",
            "https://cdn.news.mycelebs.ai/mycelebs/2022/09/10124650/cafe_subdued20club_ReHf_4032487_0_0.webp",
        ],
        [
            "개미",
            "https://cdn.kormedi.com/wp-content/uploads/2022/05/gettyimages-497490373-580x386.jpg",
        ],
        [
            "닭",
            "https://t1.daumcdn.net/blogfile/fs12/27_blog_2008_02_28_16_48_47c6673e8ba3a?x-content-disposition=inline&filename=32%ED%86%A0%EC%A2%85%EB%8B%AD%ED%99%A9%EA%B0%88%EA%B3%84.jpg",
        ],
    ]

    context = {
        "name": request.GET.get("name"),
        "animal": choice(animals),
    }
    return render(request, "past_life_result.html", context)


def lorem_form(request):
    return render(request, "lorem_form.html")


def lorem_rst(request):
    paragraph_cnt = int(request.GET.get("paragraph"))
    word_cnt = int(request.GET.get("word"))

    words = ["딸기", "바나나", "파인애플", "메론", "코코넛", "자몽", "수박", "귤", "참외"]

    paragraphs = []
    for _ in range(paragraph_cnt):
        paragraph = []
        for _ in range(word_cnt):
            paragraph.append(choice(words))
        paragraphs.append(paragraph)

    context = {
        "paragraphs": paragraphs,
    }

    return render(request, "lorem_rst.html", context)
