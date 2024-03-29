from itertools import product
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views import View
from .models import *
from .forms import RegistrationForm,CustomerForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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
  items_in_cart=False
  items_in_cart=Cart.objects.filter(Q(product=product_instance.id) &
                                    Q(user=request.user))

  return render(request, 'app/productdetail.html',{
    'product':product_instance,
    'items_in_cart':items_in_cart
  })

@login_required
def add_to_cart(request):
 user=request.user
 product_id=request.GET.get('product_id')
 product=Product.objects.get(id=product_id)
 Cart(user=user,product=product).save()

 return redirect('/showcart')

@login_required
def showcart(request):
 if request.user.is_authenticated:
  user=request.user
  cart=Cart.objects.filter(user=user)
  amount=0
  shipping_amount=70
  total_amount=0

  cart_list=[p for p in Cart.objects.all() if p.user==user]
  if len(cart_list)!=0:
   for items in cart_list:
    amt=items.quantity*items.product.discounted_price
    amount+=amt
    total_amount=amount+shipping_amount
  else:
   return render(request,'app/emptycart.html') 

  return render(request,'app/addtocart.html',{
   'carts':cart,
   'total_amount':total_amount,
   'amount':amount,
   'shipping_amount':shipping_amount
   })

@login_required
def pluscart(request):
 if request.GET:
  user=request.user
  product_id=request.GET.get('product_id')
  c=Cart.objects.get(Q(product=product_id) & Q(user=request.user))
  c.quantity+=1
  c.save()

  amount=0
  shipping_amount=70
  total_amount=0

  c_list=[p for p in Cart.objects.all() if p.user==user]

  for items in c_list:
   amt=items.quantity*items.product.discounted_price
   amount+=amt
   total_amount=amount+shipping_amount
  data={
        'quantity':c.quantity,
      'amount':amount,
      'total_amount':total_amount,
      'shipping_amount':shipping_amount
  }
  return JsonResponse(data)

@login_required    
def minuscart(request):
 if request.GET:
  user=request.user
  product_id=request.GET.get('product_id')
  c=Cart.objects.get(Q(product=product_id) & Q(user=user))
  c.quantity=c.quantity-1
  c.save()

  amount=0
  shipping_amount=70
  total_amount=0

  c_list=[p for p in Cart.objects.all() if p.user==user]

  for items in c_list:
   amt=items.quantity*items.product.discounted_price
   amount+=amt
   total_amount=amount+shipping_amount

  data={
    'amount':amount,
    'total_amount':total_amount,
    'shipping_amount':shipping_amount,
    'quantity':c.quantity
  }

  return JsonResponse(data)
 
@login_required 
def removecart(request):
  if request.GET:
    user=request.user
    product_id=request.GET.get('product_id')
    c=Cart.objects.get(Q(product=product_id) & Q(user=user))
    c.delete()
    amount=0
    shipping_amount=70
    total_amount=0

    c_list=[p for p in Cart.objects.all() if p.user==user]

    for items in c_list:
      amt=items.quantity*items.product.discounted_price
      amount+=amt
      total_amount=amount+shipping_amount

    data={
    'amount':amount,
    'shipping_amount':shipping_amount,
    'total_amount':total_amount
    }   
    return JsonResponse(data)

def buy_now(request):
 return render(request, 'app/buynow.html')



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
   return redirect('address')
   

  return render(request,'app/profile.html',{
   'form':form,
   'active':'btn-primary',
   
  }) 


class AddressView(View):
 def get(self,request):
   address=Customer.objects.filter(user=request.user)

   return render(request, 'app/address.html',{
      'address':address

  })
 

@login_required
def orders(request):
 if request.user.is_authenticated:
  user=request.user
  order=Order.objects.filter(user=user)
  amount=0
  shipping_amount=70
  total_amount=0

  cart_list=[p for p in Order.objects.all() if p.user==user]

  for items in cart_list:
   amt=items.quantity*items.product.discounted_price
   amount+=amt
   total_amount=amount+shipping_amount
   

 return render(request, 'app/orders.html',{
  'amount':amount,
  'total_amount':total_amount,
  'shipping_amount':shipping_amount,
  'orders':order
 })

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
 

@login_required
def checkout(request):
 user=request.user
 customers=Customer.objects.filter(user=user)
 carts=Cart.objects.filter(user=user)
 amount=0
 total_amount=0
 shipping_amount=70

 cart_list=[p for p in Cart.objects.all() if p.user==user]

 for items in cart_list:
  amt=items.quantity*items.product.discounted_price
  amount+=amt
  total_amount=amount+shipping_amount

  
 return render(request, 'app/checkout.html',{
  'amount':amount,
  'total_amount':total_amount,
  'customers':customers,
  'carts':carts,
  'shipping_amount':shipping_amount,

 })

@login_required
def paymentView(request):
 user=request.user
 customer_id=request.GET.get('customer_id')
 customer=Customer.objects.get(id=customer_id)
 cart=Cart.objects.filter(user=user)

 for c in cart:
  Order(customer=customer,user=user,quantity=c.quantity,product=c.product).save()
  c.delete()

 return redirect('/orders')
