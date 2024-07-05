from rest_framework import viewsets
from apps.users.models import Doctor, Nurse, IsChiefDoctorOrReadOnly, IsDoctorOrChiefDoctor
from apps.users.serializers import DoctorSerializer, NurseSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsChiefDoctorOrReadOnly]

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    permission_classes = [IsChiefDoctorOrReadOnly]


