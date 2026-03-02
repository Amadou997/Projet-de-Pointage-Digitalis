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

class ReportViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response({"message": "Rapports globaux ou mensuels"})
    
    def retrieve(self, request, pk=None):
        return Response({"message": f"Rapport détail pour ID: {pk}"})
    
    def create(self, request):
        return Response({"message": "Rapport créé", "data": request.data})
    
    def update(self, request, pk=None):
        return Response({"message": f"Rapport {pk} mis à jour", "data": request.data})
    
    def destroy(self, request, pk=None):
        return Response({"message": f"Rapport {pk} supprimé"})