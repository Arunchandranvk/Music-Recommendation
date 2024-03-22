from django.urls import path
from .views import *

urlpatterns =[
    path('survey/',Survey.as_view(),name='s'),
    path('result/',Result.as_view(),name='r'),
    path('detect-emotions/',detect_emotions, name='detect_emotions'),
    path('emotion/',Emotion.as_view(),name='e')
]