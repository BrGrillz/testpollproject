from django.urls import path
from .views import *


urlpatterns = [
    path('poll/create/', PollsCreateView.as_view(), name='poll create'),
    path('poll/list/', PollListView.as_view(), name='poll list'),
    path('poll/detail/<int:pk>/', PollsDetailView.as_view(), name='poll detail'),
    path('poll/update/<int:pk>/', PollsUpdateView.as_view(), name='poll change'),
    path('poll/delete/<int:pk>/', PollsDeleteView.as_view(), name='poll delete'),
    path('question/create/', QuestionCreateView.as_view(), name='question create'),
    path('question/change/', QuestionDeleteUpdateListView.as_view(), name='question update'),
    path('answer/create/', AnswerCreateView.as_view(), name='question create'),
    path('user/answer/', UserAnswerView.as_view(), name='user answer'),
    path('user/answer/<int:pk>/', UserAnswerListView.as_view(), name='user answer list'),

]
