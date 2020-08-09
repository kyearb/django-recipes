from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe #Ingredient, Instruction, Book, Website

class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        """
        return all recipes
        """
        return Recipe.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['new_recipe_list'] = Recipe.objects.filter(new=True)
        context['old_recipe_list'] = Recipe.objects.filter(new=False)
        context['recipe_list'] = Recipe.objects.all()
        return context

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

    def get_queryset(self):
        """
        returns all recipes
        """
        return Recipe.objects.all()

def index(request):
    return render(request, 'recipes/index.html', {'recipe_list': Recipe.objects.order_by('-name')})

def detail(request, recipe_id):
    r = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': r})

def add(request):
    return render(request, 'recipes/add.html')

def add_new(request):
    name = request.POST['title']
    time = request.POST['time']
    if time=='':
        time = None
    ingredients_text = request.POST['ingredients']

    new = request.POST['new'] == 'on'

    recipe = Recipe(name=name, time=time, new=new, ingredients=ingredients_text)

    recipe.save()
    
    # website_url = request.POST['website']
    # if not website_url:
    #     book_title = request.POST['book']
    #     page_number = request.POST['page_number']
    #     # Book(recipe=recipe, title=book_title, page_number=page_number)
    # # else:
    #     # Website(recipe=recipe, website_url=website_url)

    # instructions_text = request.POST['instructions']
    
    # for ingredient in ingredients_text.split(','):
    #     recipe.ingredient_set.create(name=ingredient)
    
    # for instruction in instructions_text.split('\n'):
    #     recipe.instruction_set.create(step_text=instruction)
    
    # recipe.save()
    
    return HttpResponseRedirect(reverse('recipes:add'))