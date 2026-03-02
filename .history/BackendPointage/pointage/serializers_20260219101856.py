from rest_framework import serializers
from .models import Pointage, Absence, Horaire

class PointageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pointage
        fields = '__all__'

"""
class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'
"""
"""

class AbsenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Absence
        fields = '__all__'
        read_only_fields = ['statut']
class HoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaire
        fields = '__all__'
"""
class AbsenceSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField(source="user.id", read_only=True)
    nom = serializers.CharField(source="user.nom", read_only=True)
    prenom = serializers.CharField(source="user.prenom", read_only=True)
    email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Absence
        fields = [
            "id",
            "user_id",
            "nom",
            "prenom",
            "email",
            "date_debut",
            "date_fin",
            "type_absence",
            "motif",
            "statut"
        ]