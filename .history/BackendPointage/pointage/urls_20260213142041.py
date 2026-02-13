# pointage/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PointageViewSet, AbsenceViewSet, HoraireViewSet, ReportViewSet

router = DefaultRouter()
router.register(r'pointages', PointageViewSet, basename='pointages')
router.register(r'absences', AbsenceViewSet, basename='absences')
router.register(r'horaires', HoraireViewSet, basename='horaires')
router.register(r'reports', ReportViewSet, basename='reports')

urlpatterns = [
    path('', include(router.urls)),
]