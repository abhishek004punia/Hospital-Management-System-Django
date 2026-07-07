from django.shortcuts import render

def login_view(request):
    return render(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')