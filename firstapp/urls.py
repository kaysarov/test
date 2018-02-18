from django.urls import include, path
from . import views
'''
urlpatterns = [
    path('', views.simple, name='simple'),
    path(r'^post/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
]
'''
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/', views.post_detail, name='post_detail'),
]
