from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import *
from .forms import RegistrationForm


class Home(View):
 def get(self,request):
  topwears=Product.objects.filter(category='TW')
  bottomwears=Product.objects.filter(category='BW')
  innerwears=Product.objects.filter(category='IW')
  
  return render(request,'app/home.html',{
   'topwears':topwears,
   'bottomwears':bottomwears,
   'innerwears':innerwears
  })
 
class ProductView(View):
 def get(self,request,pk):
  product_instance=get_object_or_404(Product,pk=pk)

  return render(request, 'app/productdetail.html',{
    'product':product_instance
  })

   
  

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

# def mobile(request):
#  return render(request, 'app/mobile.html')

class MobileView(View):
 def get(self,request,data=None):
  if data==None:
    mobile_instance=Product.objects.filter(category='M')
  elif data=='Google' or data=='Apple':
   mobile_instance=Product.objects.filter(category='M').filter(brand=data)  

  elif data=='below':
   mobile_instance=Product.objects.filter(category='M').filter(discounted_price__lt=100000)

  elif data=='above':
   mobile_instance=Product.objects.filter(category='M').filter(discounted_price__gt=100000) 



  return render(request, 'app/mobile.html',{
   'mobile':mobile_instance
  })


def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

class RegistrationView(View):
 def get(self,request):
  form=RegistrationForm()

  return render(request, 'app/customerregistration.html',{
   'form':form
  })
 
 def post(self,request):
  form=RegistrationForm(request.POST)
  if form.is_valid():
   form.save()

  return render(request, 'app/customerregistration.html',{
   'form':form
  })
 



  



def checkout(request):
 return render(request, 'app/checkout.html')
