from django.contrib import admin

from .models import Recipe #, Ingredient, Instruction, Website, Book
# Register your models here.

# class IngredientInline(admin.StackedInline):
#     model = Ingredient
#     extra = 0

# class InstructionInline(admin.StackedInline):
#     model = Instruction
#     extra = 0

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'new', 'ingredients', 'recipe_source', 'source_name')

# admin.site.register(Recipe)