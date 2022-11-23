from django.shortcuts import render
import copy


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
}


def index(request):    
    return render(request, 'calculator/index.html')


def recipe(request, recipe):
    if not recipe  in DATA:
        return render(request, 'calculator/index.html')

    servings = request.GET.get('servings', 1)
    copy_DATA = copy.deepcopy(DATA)

    for element in copy_DATA:
        if recipe == element:        
            DATA_only_one_recipe = {'recipe':copy_DATA[element]}        
            break

    for ingredient, amount in DATA_only_one_recipe['recipe'].items():    
        DATA_only_one_recipe['recipe'][ingredient] = amount * int(servings)

    return render(request, 'calculator/index.html', DATA_only_one_recipe)