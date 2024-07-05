from rest_framework import serializers

from apps.users.models import User, Doctor, Nurse


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'photo', 'gender']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'photo', 'gender', 'is_chief_doctor', 'speciality']

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'photo', 'gender', 'is_busy']
