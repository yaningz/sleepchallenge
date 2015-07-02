from django.contrib.auth import authenticate
# login is imported as auth_login to prevent naming problems with the login view
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from models import UserProfile, Wing

# Helper functions.
def parse(string):
	string = string.encode('utf8')
	parts = string.split(':')
	if len(parts) == 2:
		return parts

def get_first_name(name):
	return name.split(' ')[0]

def get_last_name(name):
	return name.split(' ')[-1]

# Create your views here.
def index(request):
    return render(request, 'sleep/index.html')

@login_required
def record(request):
    return render(request, 'sleep/record.html')

def stats(request):
    return render(request, 'sleep/stats.html')

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

		if 'email' not in fields or 'name' not in fields:
			print 'Error: Email or name missing in login'
			return HttpResponse(status=500)
		email = fields['email']
		name = fields['name']
		print 'Received a login request with email', email, 'and name', name

		# Attempt to authenticate the user
		user = authenticate(username=email, password='')

		if not user:
			print 'Creating new user', email
			# User does not yet exist, they need to be registered
			user = User.objects.create_user(email, email, '')
			user.first_name = get_first_name(name)
			user.last_name = get_last_name(name)
			user.save()
			profile = UserProfile.objects.create(user=user, wing='', zs='')
			profile.save()

		# User exists, they can be logged in
		print 'Logging in user', email
		auth_login(request, user)
		return HttpResponse(status=200)

	else:
		return render(request, 'sleep/login.html')
