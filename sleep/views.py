import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sleep/index.html')

# @login_required
def record(request):
    return render(request, 'sleep/record.html')

def stats(request):
    return render(request, 'sleep/stats.html')

def parse(string):
	string = string.encode('utf8')
	parts = string.split(':')
	if len(parts) == 2:
		return parts

def login(request):
	print 'Got a request to login'
	return render(request, 'sleep/login.html')

def loginUser(request):
	# Check for name and email fields in GET
	# If present, a person is properly logging in. Otherwise, just display a default login page.
	if len(request.GET) > 0:
		fields = {}
		for x in request.GET:
			(key, value) = parse(x)
			fields[key] = value
		print 'Received a login request with email', fields['email'], 'and name', fields['name']
		# TODO(lahuang4): Register or authenticate user here
		return HttpResponse(status=200)
	else:
		return render(request, 'sleep/login.html')
