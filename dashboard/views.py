from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/web/accounts/login/')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')