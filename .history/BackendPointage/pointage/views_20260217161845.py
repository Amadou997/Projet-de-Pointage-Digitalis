from rest_framework import viewsets
from .models import Pointage, Absence, Horaire
from .serializers import PointageSerializer, AbsenceSerializer, HoraireSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class PointageViewSet(viewsets.ModelViewSet):
    queryset = Pointage.objects.all()
    serializer_class = PointageSerializer
    permission_classes = [IsAuthenticated]
"""
class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    #permission_classes = [IsAuthenticated]
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Absence
from .serializers import AbsenceSerializer
from .permissions import IsManagerOrAdmin

class AbsenceViewSet(viewsets.ModelViewSet):

    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    permission_classes = [IsAuthenticated]

    # 👇 Valider une absence
    @action(detail=True, methods=['put'], permission_classes=[IsManagerOrAdmin])
    def valider(self, request, pk=None):
        absence = self.get_object()
        absence.statut = 'VALIDE'
        absence.save()
        return Response({'message': 'Absence validée'})

    # 👇 Rejeter une absence
    @action(detail=True, methods=['put'], permission_classes=[IsManagerOrAdmin])
    def rejeter(self, request, pk=None):
        absence = self.get_object()
        absence.statut = 'REJETE'
        absence.save()
        return Response({'message': 'Absence rejetée'})
    

class HoraireViewSet(viewsets.ModelViewSet):
    queryset = Horaire.objects.all()
    serializer_class = HoraireSerializer
    permission_classes = [IsAuthenticated]

class ReportViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response({"message": "Rapports globaux ou mensuels"})
    