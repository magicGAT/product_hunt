from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
	return render(request, 'accounts/login.html')

def sign_up(request):
	if request.method == 'POST':
	# user has info and wants an account
		if request.POST['password'] == request.POST['conf_password']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
				auth.login(request, user)
				return redirect('home')
		else:
			return render(request, 'accounts/signup.html', {'error': 'Passwords are not a match'})
	else:
	# user wants to enter info
		return render(request, 'accounts/signup.html')

def logout(request):
	# TO-DO route to homepage upon logout
	return render(request, 'accounts/logout.html')

