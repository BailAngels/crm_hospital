from rest_framework import viewsets

from apps.patients.models import PatientCard, DiseaseHistory
from apps.patients.serializers import PatientCardSerializer, DiseaseHistorySerializer
from apps.users.models import IsChiefDoctorOrReadOnly, IsDoctorOrChiefDoctor

class PatientCardViewSet(viewsets.ModelViewSet):
    queryset = PatientCard.objects.all()
    serializer_class = PatientCardSerializer
    permission_classes = [IsDoctorOrChiefDoctor]

class DiseaseHistoryViewSet(viewsets.ModelViewSet):
    queryset = DiseaseHistory.objects.all()
    serializer_class = DiseaseHistorySerializer
    permission_classes = [IsDoctorOrChiefDoctor]

    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user)