from django.shortcuts import render
from .models import News, Category
from django.views.generic import ListView, DeleteView
from django.shortcuts import get_object_or_404
from .utils import MyMixin

class HomeFilms(MyMixin, ListView):
    model = News
    template_name = 'films/index.html'
    context_object_name = 'films'
    paginate_by = 3
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):# метод для динамического обновления заголовка
        context = super().get_context_data(**kwargs) #записываем в переменную данные ,кот были до этого
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def index(request):
#     films = News.objects.order_by('-created_at')
#     context = {'films': films,
#                'title': 'Список фильмов',
#                }
#     return render(request, template_name='films/index.html', context=context)

class CategoriesFilms(MyMixin, ListView):
    model = Category
    template_name = 'films/index.html'
    context_object_name = 'films'
    allow_empty = False
    paginate_by = 3

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):# метод для динамического обновления заголовка
        context = super().get_context_data(**kwargs) #записываем в переменную данные ,кот были до этого
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context
class ViewFilms(DeleteView):
    model = News
    context_object_name = 'films_item'
    # pk_url_kwarg = 'news_id'

# def get_category(request, category_id):
#     films = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'films/category.html', {'films': films,})

# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'films/view_films.html', {"news_item": news_item})