
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('menulist', MenuListAPIView.as_view()),
    path('details', Details.as_view()),
    path('makeorder', MakeTheOrder),
]
