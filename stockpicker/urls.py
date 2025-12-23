from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'view'),       # index page with 10x10 grid

    path('pick/',views.pick, name = 'pick'),   #  this is the picked stock page

    path('reset/',views.reset, name = 'reset'), # reset stock page

    path('catwalk/',views.catwalk, name = 'catwalk'),   # randomly-picked stock page

]
