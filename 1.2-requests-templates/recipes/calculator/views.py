from django.shortcuts import render
from django.http import HttpResponse, Http404

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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }

def get_recipe(recipe_name, servings):
    if recipe_name not in DATA:
        raise Http404("Рецепт не найден")

    recipe = DATA[recipe_name]

    if servings > 0:
        return {ingredient: amount * servings for ingredient, amount in recipe.items()}
    return recipe

def omlet(request):
    servings = request.GET.get('servings', 1)  # По умолчанию 1 порция
    try:
        servings = int(servings)
        if servings < 1:
            raise ValueError
    except ValueError:
        return HttpResponse("Параметр servings должен быть положительным целым числом.", status=400)

    recipe = get_recipe('omlet', servings)

    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings < 1:
            raise ValueError
    except ValueError:
        return HttpResponse("Параметр servings должен быть положительным целым числом.", status=400)

    recipe = get_recipe('pasta', servings)

    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings < 1:
            raise ValueError
    except ValueError:
        return HttpResponse("Параметр servings должен быть положительным целым числом.", status=400)

    recipe = get_recipe('buter', servings)

    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)