from rest_framework import viewsets
from .models import Pointage, Absence, Horaire
from .serializers import PointageSerializer, AbsenceSerializer, HoraireSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class PointageViewSet(viewsets.ModelViewSet):
    queryset = Pointage.objects.all()
    serializer_class = PointageSerializer
    permission_classes = [IsAuthenticated]

class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    permission_classes = [IsAuthenticated]

class HoraireViewSet(viewsets.ModelViewSet):
    queryset = Horaire.objects.all()
    serializer_class = HoraireSerializer
    permission_classes = [IsAuthenticated]

c