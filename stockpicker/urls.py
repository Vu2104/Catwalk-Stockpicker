from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'view'),       # index page with 10x10 grid

<<<<<<< HEAD
    path('pick/',views.pick, name = 'pick'),   #  this is the picked stock page
=======
    path('stockpicker/',views.stockPickerPage, name = 'stockpicker'),   #  URL for stockpicker

    path('pickstock/', views.pickStock, name = 'pickstock'), # URL for pickStock view
>>>>>>> origin/final-project-version

    path('reset/',views.reset, name = 'reset'), # URL for resetting the page

    path('catwalk/',views.catwalk, name = 'catwalk'),   # URL for randomly-picked stock page

]
