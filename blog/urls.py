from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path(r'',views.index,name='index'),
    path(r'post/<int:pk>/',views.detail,name='detail'),
    path(r'archives/<int:year>/<int:month>/',views.archives,name='archives'),
    path(r'category/<int:pk>/', views.category, name='category'),
    path(r'tag/<int:pk>/', views.tag, name='tag'),
]