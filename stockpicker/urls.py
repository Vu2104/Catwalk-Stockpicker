from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'view'),       # index page with 10x10 grid

    path('stockpicker/',views.stockPickerPage, name = 'stockpicker'),   #  this is the picked stock page

    path('pickstock/', views.pickStock, name = 'pickstock'),

    path('reset/',views.reset, name = 'reset'), # reset stock page

    path('catwalk/',views.catwalk, name = 'catwalk'),   # randomly-picked stock page

]
