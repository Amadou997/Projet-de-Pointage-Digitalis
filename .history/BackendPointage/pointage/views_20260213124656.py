from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from .models import Pointage


@api_view(["GET"])
def global_report(request):
    data = Pointage.objects.values("type").annotate(total=Count("id"))
    return Response(data)