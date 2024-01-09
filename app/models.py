from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


District_Choices=(('Achham', 'Achham'), ('Arghakhanchi', 'Arghakhanchi'), 
                  ('Baglung', 'Baglung'), ('Baitadi', 'Baitadi'), ('Bajhang', 'Bajhang'),
                  ('Bajura', 'Bajura'), ('Banke', 'Banke'), ('Bara', 'Bara'), 
                  ('Bardiya', 'Bardiya'), ('Bhaktapur', 'Bhaktapur'), ('Bhojpur', 'Bhojpur'), 
                  ('Chitwan', 'Chitwan'), ('Dadeldhura', 'Dadeldhura'), ('Dailekh', 'Dailekh'), 
                  ('Dang', 'Dang'), ('Darchula', 'Darchula'), ('Dhading', 'Dhading'), 
                  ('Dhankuta', 'Dhankuta'), ('Dhanusa', 'Dhanusa'), ('Dholkha', 'Dholkha'), 
                  ('Dolpa', 'Dolpa'), ('Doti', 'Doti'), ('Eastern Rukum', 'Eastern Rukum'), 
                  ('Gorkha', 'Gorkha'), ('Gulmi', 'Gulmi'), ('Humla', 'Humla'), ('Ilam', 'Ilam'), 
                  ('Jajarkot', 'Jajarkot'), ('Jhapa', 'Jhapa'), ('Jumla', 'Jumla'), 
                  ('Kailali', 'Kailali'), ('Kalikot', 'Kalikot'), ('Kanchanpur', 'Kanchanpur'), 
                  ('Kapilvastu', 'Kapilvastu'), ('Kaski', 'Kaski'), ('Kathmandu', 'Kathmandu'), 
                  ('Kavrepalanchok', 'Kavrepalanchok'), ('Khotang', 'Khotang'), 
                  ('Lalitpur', 'Lalitpur'), ('Lamjung', 'Lamjung'), ('Mahottari', 'Mahottari'), 
                  ('Makwanpur', 'Makwanpur'), ('Manang', 'Manang'), ('Morang', 'Morang'), 
                  ('Mugu', 'Mugu'), ('Mustang', 'Mustang'), ('Myagdi', 'Myagdi'), 
                  ('Nawalparasi', 'Nawalparasi'), ('Nuwakot', 'Nuwakot'), ('Okhaldhunga', 'Okhaldhunga'), 
                  ('Palpa', 'Palpa'), ('Panchthar', 'Panchthar'), ('Parbat', 'Parbat'), ('Parsa', 'Parsa'),
                  ('Pyuthan', 'Pyuthan'), ('Ramechhap', 'Ramechhap'), ('Rasuwa', 'Rasuwa'), 
                  ('Rautahat', 'Rautahat'), ('Rolpa', 'Rolpa'), ('Rukum', 'Rukum'), ('Rupandehi', 'Rupandehi'), 
                  ('Salyan', 'Salyan'), ('Sankhuwasabha', 'Sankhuwasabha'), ('Saptari', 'Saptari'), ('Sarlahi', 'Sarlahi'), 
                  ('Sindhuli', 'Sindhuli'), ('Sindhupalchok', 'Sindhupalchok'), ('Siraha', 'Siraha'), ('Solukhumbu', 'Solukhumbu'), 
                  ('Sunsari', 'Sunsari'), ('Surkhet', 'Surkhet'), ('Syangja', 'Syangja'), ('Tanahu', 'Tanahu'), ('Taplejung', 'Taplejung'), 
                  ('Terhathum', 'Terhathum'), ('Udayapur', 'Udayapur'))
# Create your models here.
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    district=models.CharField(choices=District_Choices,max_length=100)

    def __str__(self):
        return str(self.id)
    
Category_Choices=(
    ('M','Mobiles'),
    ('L','Laptops'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
    ('IW','Inner Wear')
)    

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=Category_Choices,max_length=100)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id) 
    @property
    def total_cost(self):
        return str(self.quantity*self.product.discounted_price)
    
Status_Choices=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')

)  

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateField(auto_now_add=True)
    status=models.CharField(choices=Status_Choices,max_length=100,default='pending')

    def __str__(self):
        return str(self.id)