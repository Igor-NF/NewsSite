from django.urls import path

from News.views import index, get_category


urlpatterns = [
    path('', index, name='Home'),
    path('categoty/<int:category_id>', get_category, name='Category')
]


