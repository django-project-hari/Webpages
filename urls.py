from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    #path('concat',views.concat,name='concat')
]