from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.
def home(request):
	return render(request, 'products/home.html')

@login_required
def new_product(request):
	if request.method == "POST":
		if request.POST['p_name'] and request.POST['p_text'] and request.FILES['p_icon'] and request.FILES['p_image']:
			product = Product()
			product.name = request.POST['p_name']
			product.description = request.POST['p_text']
			product.icon = request.FILES['p_icon']
			product.image = request.FILES['p_image']
			product.url = 'http://' + request.POST['p_name'] + '.com'
			product.pub_date = timezone.datetime.now()
			product.hunter = request.user
			product.save()
			return redirect('home')  
		else: 
			return render(request, 'products/newproduct.html'), {'error':'All fields must be filled'}
	else:
		return render(request, 'products/newproduct.html')
	