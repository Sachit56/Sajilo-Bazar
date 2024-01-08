from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import *
from .forms import RegistrationForm,CustomerForm
from django.contrib import messages

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

class ProfileView(View):
 def get(self,request):
  form=CustomerForm()

  return render(request,'app/profile.html',{
   'form':form,
   'active':'btn-primary'
  })
 def post(self,request):
  form=CustomerForm(request.POST)

  if form.is_valid():
   user=request.user
   name=form.cleaned_data['name']
   locality=form.cleaned_data['locality']
   city=form.cleaned_data['city']
   district=form.cleaned_data['district']
   zipcode=form.cleaned_data['zipcode']

   reg=Customer(user=user,name=name,locality=locality,city=city,district=district,zipcode=zipcode)

   reg.save()
   messages.success(request,'Profile Updated Sucessfully!')

  return render(request,'app/profile.html',{
   'form':form,
   'active':'btn-primary',
   
  }) 





def address(request):
 address=Customer.objects.filter(user=request.user)

 return render(request, 'app/address.html',{
  'address':address
 })

def orders(request):
 return render(request, 'app/orders.html')

def passdone(request):
 return render(request,'app/passwordchangedone.html')

def ResetPasswordDoneView(request):
 return render(request,'app/resetpassworddone.html')

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


class RegistrationView(View):
 def get(self,request):
  form=RegistrationForm()
  

  return render(request, 'app/customerregistration.html',{
   'form':form,
   
  })
 
 def post(self,request):
  form=RegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request,'Registered Successfully!')
   form.save()

  return render(request, 'app/customerregistration.html',{
   'form':form
  })
 



  



def checkout(request):
 return render(request, 'app/checkout.html')
