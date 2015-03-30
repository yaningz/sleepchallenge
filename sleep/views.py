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

def login(request):
	print 'got a request to login'
	# A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing a user registration.
	if request.method == 'POST':
		# print stuff to see what we got
		print request.POST
		for x in request.POST:
			print 'got a thing:', x
	else:
		# not an HTTP POST, just display the page
		pass

	return render(request, 'sleep/login.html')