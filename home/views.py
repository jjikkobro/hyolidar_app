from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

def home_view(request):    
    return render(request, 'home/home.html')

def test_view(request):
    # 사용자가 이미 로그인된 상태인지 확인
    if not request.user.is_authenticated:
        # 특정 사용자로 자동 로그인 처리
        user = User.objects.get(username='jung')  # 'jung'를 원하는 사용자로 변경
        login(request, user)
    
    # 로그인 후 '/home'으로 리다이렉트
    return redirect('home:home')

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