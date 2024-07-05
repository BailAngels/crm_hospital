from rest_framework.routers import DefaultRouter

from apps.patients.views import PatientCardViewSet, DiseaseHistoryViewSet


router = DefaultRouter()
router.register(r'patient-cards', PatientCardViewSet)
router.register(r'disease-histories', DiseaseHistoryViewSet)


urlpatterns = router.urls