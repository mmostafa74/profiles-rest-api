from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()    #config new router to the new viewset class
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') #generates a list of urls (functions) that assciated for viewset
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), #first check the path from project file then search here if the url exists or not then load it to the browser
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))  #path in the list of urls and include right function
]