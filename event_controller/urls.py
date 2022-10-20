from rest_framework.routers import DefaultRouter
from .views import EventMainView, EventAttenderView
from django.urls import path, include


router = DefaultRouter()
router.register('event-attender', EventAttenderView)
router.register('event', EventMainView)

urlpatterns = [
    path('', include(router.urls)),
]
