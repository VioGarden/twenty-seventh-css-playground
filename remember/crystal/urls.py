from django.urls import path
from . import views

urlpatterns = [
    path('', views.quick_home, name='quick-home'),
    path('css1', views.css1, name='css1'),
]
