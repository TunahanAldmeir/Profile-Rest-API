from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello-viewset',views.helloviewset,basename='hello-viewset')
router.register('profile',views.UserProfileViewset)
router.register('Login',views.LoginViewSet,basename='Login')
router.register('Feed',views.UserProfileFeedViewset)

urlpatterns=[
    path('hello-view',views.HelloApiView.as_view()),
    path('',include(router.urls))
]