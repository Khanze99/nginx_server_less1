from . import views
from django.urls import path

urlpatterns = [
        path('', views.question_list, name='new_question_list'),
        path('login/', views.test,),
        path('signup/', views.test,),
        path('question/<int:pk>/', views.question_detail, name='question_detail'),
        path('ask/', views.test,),
        path('popular/', views.popular_question_list, name='popular_question_list'),
        path('new/', views.test,)
        ]
