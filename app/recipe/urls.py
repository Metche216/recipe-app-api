"""
URL mappings form the recipe app.

"""
from django.urls import (
    path,
    include
)

from rest_framework.routers import DefaultRouter #creates routes automatically for all the different options available for that view

from recipe import views

#autogenerated urls depending on the functionality that is avialable on the viewset
router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns= [
    path('', include(router.urls))
]