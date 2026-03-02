# accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginView, MeView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),  # POST /api/auth/login
    path('auth/me/', MeView.as_view(), name='me'),           # GET /api/auth/me
    path('', include(router.urls)),                          # GET / POST / PUT / DELETE / PATCH users
]

POST http://127.0.0.1:8000/api/users/