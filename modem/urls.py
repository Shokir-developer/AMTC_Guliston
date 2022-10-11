from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('lasts', last30, name='last30'),
    path('eski_olt', eski_olt, name='eski_olt'),
    path('lasts_eski', last30_eski, name='last30_eski'),

]