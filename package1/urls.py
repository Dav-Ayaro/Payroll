from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index_view'),
    path('manager',manager_view, name='manager_view'),
    path('Accountant',accountant_view, name='accountant_view'),
    path('Hr',hr_view, name='hr_view'),
    path('logout',logout, name='logout_page'),
]