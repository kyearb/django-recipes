from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe, Ingredient, Instruction, Book, Website

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
        context['new_recipe_list'] = Recipe.objects.filter(recipe_status_new=True)
        context['old_recipe_list'] = Recipe.objects.filter(recipe_status_new=False)
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
    cook_time = request.POST['cook_time']
    prep_time = request.POST['prep_time']
    if cook_time=='':
        cook_time = None
    if prep_time=='':
        prep_time = None

    recipe_status_new = request.POST['recipe_status_new'] == 'on'

    recipe = Recipe(name=name, cook_time=cook_time, prep_time=prep_time, recipe_status_new=recipe_status_new)

    recipe.save()
    
    website_url = request.POST['website']
    if not website_url:
        book_title = request.POST['book']
        page_number = request.POST['page_number']
        Book(recipe=recipe, title=book_title, page_number=page_number)
    else:
        Website(recipe=recipe, website_url=website_url)

    ingredients_text = request.POST['ingredients']
    instructions_text = request.POST['instructions']
    
    for ingredient in ingredients_text.split(','):
        recipe.ingredient_set.create(name=ingredient)
    
    for instruction in instructions_text.split('\n'):
        recipe.instruction_set.create(step_text=instruction)
    
    recipe.save()
    
    return HttpResponseRedirect(reverse('recipes:add'))