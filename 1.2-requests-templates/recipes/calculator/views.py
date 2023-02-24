from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'firmennoe': {
        'куриная грудка, г': 200,
        'лук репчатый, г': 50,
        'соевый соус, мл': 50,
        'рис круглозерный': 150,
    },
    # можете добавить свои рецепты ;)
}


def reciept(request, dish):
    template = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    content = DATA[dish].copy()
    content.update({n: servings * content[n] for n in content.keys()})
    return render(request, template, {'content': content})
