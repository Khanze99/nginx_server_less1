from . import views
from django.urls import path

urlpatterns = [
        path('', views.question_list, name='new_question_list'),
        path('login/', views.login, name='login'),
        path('signup/', views.signup, name='signup'),
        path('question/<int:pk>/', views.question_detail, name='question_detail'),
        path('ask/', views.post_ask, name='new_ask'),
        path('popular/', views.popular_question_list, name='popular_question_list'),
        path('new/', views.test,)
        ]
