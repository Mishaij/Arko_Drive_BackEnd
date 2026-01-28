from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tests/', views.tests_list, name='tests_list'),
    path('tests/<int:pk>/', views.test_detail, name='test_detail'),
    path('theory/', views.theory_list, name='theory_list'),
    path('theory/<int:pk>/', views.theory_detail, name='theory_detail'),
    path('trafficsigns/', views.trafficsigns, name='trafficsigns'),
    path('packages/', views.packages_view, name='packages'),
    path('about/', views.about_view, name='about'),
    path('random-question/', views.random_question_view, name='random_question'),

]