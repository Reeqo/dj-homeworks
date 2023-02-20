from django.shortcuts import render

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
        'рис круглозерый': 150,
    },
    # можете добавить свои рецепты ;)
}


def reciept(request, dish='firmennoe', servings=1):
    if request.GET('dish') and request.GET('serving'):
        dish = request.GET('dish')
        servings = request.GET('servings')
        content = DATA[dish]
        content.update({n: servings * content[n] for n in content.keys()})
        render(request, '', content)
    elif request.GET('dish'):
        dish = request.GET('dish')
        render(request, '', DATA[dish])
    elif request.GET('servings'):
        servings = request.GET('servings')
        content = DATA[dish]
        content.update({n: servings * content[n] for n in content.keys()})
    else:
        render(request, '', DATA[dish])
