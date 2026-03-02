from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

# CRUD utilisateurs
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # seul admin peut gérer les users

# Login JWT
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Email ou mot de passe invalide'}, status=status.HTTP_401_UNAUTHORIZED)

# Récupérer utilisateur connecté
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)
    
    from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .accounts.services.qr_service import generate_qr_for_user
from accounts.models import User


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def generate_qr(request):

    user_id = request.data.get("user_id")

    try:
        user = User.objects.get(id=user_id)

        qr_url = generate_qr_for_user(user)

        return Response({
            "message": "QR Code généré",
            "qr_code_url": qr_url
        })

    except User.DoesNotExist:
        return Response({"error": "User introuvable"}, status=404)