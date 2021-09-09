from django.urls import path

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', HomeFilms.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', CategoriesFilms.as_view(), name='category'),
    # path('films/<int:news_id>/', view_news, name='view_news'),
    path('films/<int:pk>/', ViewFilms.as_view(), name='view_films'),
]
