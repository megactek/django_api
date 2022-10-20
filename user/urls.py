from rest_framework.routers import DefaultRouter
from .views import CustomUserView, UserProfileView, AddressView
from django.urls import path, include
 


router = DefaultRouter()
router.register('user', CustomUserView)
router.register('user-profile', UserProfileView)



urlpatterns = [
    path('', include(router.urls)),
    path('add_address', AddressView.as_view()),
]
