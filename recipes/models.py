from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Recipe(models.Model):
    """
    a class for a single recipe
    """
    name = models.CharField(max_length=200)
    prep_time = models.IntegerField(null=True, blank=True)
    cook_time = models.IntegerField(null=True, blank=True)
    recipe_status_new = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name

class Ingredient(models.Model):
    """
    class for a single ingredient in a recipe
    """
    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Instruction(models.Model):
    """
    class for single instruction in a recipe. The primary key will define the step number
    """
    step_text = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.step_text

class Source(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)

class Book(Source):
    title = models.CharField(max_length=200)
    page_number = models.IntegerField()

    def __str__(self) -> str:
        return self.title

class Website(Source):
    website_url = models.URLField()

    def __str__(self) -> str:
        return self.website_url