from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'view'),       # index page with 10x10 grid

    path('stockpicker/',views.stockPickerPage, name = 'stockpicker'),   #  URL for stockpicker

    path('pickstock/', views.pickStock, name = 'pickstock'),

    path('reset/',views.reset, name = 'reset'), # URL for resetting the page

    path('catwalk/',views.catwalk, name = 'catwalk'),   # URL for randomly-picked stock page

]
