from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from.views import JobApplicationViewSet, JobViewSet


router = DefaultRouter()
router.register('jobs', JobViewSet )
router.register('applications', JobApplicationViewSet)


# URL Configurations
urlpatterns = router.urls
