from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'view'),       # index page with 10x10 grid

    path('pick/',views.pick, name = 'pick'),   #  this is the picked stock page

    path('reset/',views.reset, name = 'reset'), # URL for resetting the page

    path('catwalk/',views.catwalk, name = 'catwalk'),   # URL for randomly-picked stock page

]
