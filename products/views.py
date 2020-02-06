from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.
def home(request):
	return render(request, 'products/home.html')

@login_required
def new_product(request):
	if request.method == "POST":
		if request.POST['p_name'] and request.POST['p_text'] and request.POST['p_icon'] and request.POST['p_image']:
			product = Product()
			product.name = request.POST['p_name']
			product.text = request.POST['p_text']
			product.icon = request.POST['p_icon']
			product.image = request.POST['p_image']
		else: 
			return render(request, 'products/newproduct.html'), {'error':'All fields must be filled'}
	else:
		return render(request, 'products/newproduct.html')
	