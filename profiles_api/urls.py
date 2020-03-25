from django.urls import path

from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), #first check the path from project file then search here if the url exists or not then load it to the browser

]