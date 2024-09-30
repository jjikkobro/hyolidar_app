from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def home_view(request):
    return render(request, 'home/home.html')

def get_status(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT status FROM home_status WHERE user=1")  # Adjust query as needed
        status = cursor.fetchone()[0]  # Fetch the status column value

    # Map status values to status messages
    if status == 0:
        status_message = "비어있음"
    elif status == 1:
        status_message = "사용중"
    elif status == 2:
        status_message = "넘어짐"
    else:
        status_message = "Unknown"

    return JsonResponse({'status': status_message})