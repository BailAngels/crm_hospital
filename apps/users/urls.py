from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.users.views import DoctorViewSet, NurseViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'nurses', NurseViewSet)


urlpatterns = router.urls
