from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def lidar_view(request):
    print(request)
    lidar_source = ""
    return JsonResponse({'lidar_source':lidar_source})