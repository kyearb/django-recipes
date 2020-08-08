from django.contrib import admin

from .models import Recipe, Ingredient, Instruction, Website, Book
# Register your models here.

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 0

class InstructionInline(admin.StackedInline):
    model = Instruction
    extra = 0

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'prep_time', 'cook_time', 'recipe_status_new')
    inlines = [
        IngredientInline,
        InstructionInline,
        ]


# admin.site.register(Recipe)