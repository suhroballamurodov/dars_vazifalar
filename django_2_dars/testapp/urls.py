from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('ism_familiya',ism_familiya),
    path('manzil',manzil),
    path('malumot', malumot),
    path('umumiy',umumiy),
    path('html',html),
    # path('download',download),
]