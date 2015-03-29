from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sleep/index.html')

# @login_required
def record(request):
    return render(request, 'sleep/record.html')

def stats(request):
    return render(request, 'sleep/stats.html')
