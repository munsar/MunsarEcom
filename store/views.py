from django.shortcuts import render, redirect
from .models import Product, Category, SubCategory, Shop, CartItem
from blog.models import BlogPost
from django.http import HttpResponse
from django.core.mail import EmailMessage
# Create your views here.
def home(request):
	products = Product.objects.all()
	templates = 'index.html'
	blog = BlogPost.objects.all()
	context = {'products':products, 'blog':blog}
	return render(request, templates, context)


def about(request):
	return render(request,'about.html')

def shop(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	shop = Shop.objects.all()
	templates = "shop.html"
	context = {'products':products, 'categories': categories,'shop':shop}
	return render(request, templates, context)
		
def form(request):
	if request.method=="GET":
		return render(request, 'form.html')

	elif request.method=='POST':
		Name= request.POST['Name']
		Email = request.POST['Email']
		Quantity = int(request.POST['Quantity'])
		subject = "Reply for Quotation Request"
		body = "Contents of Body"
		from_email = "electrostorenepal@gmail.com"
		to = [Email]
		

		msg = EmailMessage(subject, body, from_email, to,)
		if Quantity<=30:
			msg.attach_file('static/img/gallery.jpg')
		else:
			msg.attach_file('static/img/logo.png')

		if msg.send(fail_silently=False):
			return HttpResponse("Success")
		else:
			return HttpResponse("failed")









	
def contact(request):
	return render(request,'contact.html')

def services(request):
	return render(request,'services.html')


def details(request, id):
	categories = Category.objects.all()
	
	return render(request, 'shop-item.html', {'products':Product.objects.get(pk=id), 'categories':	categories })

def subcategory(request, id):
	
	categories = Category.objects.all()
	subcat = SubCategory.objects.get(id = id)

	return render(request, 'shop.html', {'products':subcat.reference.all() , 'categories':	categories })

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user = request.user

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(product=product, user=user)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def update_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    new_quantity = request.POST.get('quantity')

    if new_quantity:
        cart_item.quantity = int(new_quantity)
        cart_item.save()

    return redirect('cart')

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()

    return redirect('cart')

def cart(request):
    user = request.user
    #cart_items = CartItem.objects.filter(user=user)
    cart_items = CartItem.objects.all()
    context = {
        'cart_items': cart_items,
    }

    return render(request, 'cart.html', context)