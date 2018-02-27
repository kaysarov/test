from django.urls import include, path
from . import views

urlpatterns = [
    path('erl/', views.erl, name='erl'),
    path('giperexp/', views.giperexp, name='giperexp'),
    path('exp/', views.exp, name='exp'),
    path('trap/', views.trap, name='trap'),
    path('treug/', views.treug, name='treug'),
    path('norm/<key>/', views.norm, name='norm'),
    path('rav/<key>/', views.rav, name='rav'),
    path('', views.base, name='base'),
]
