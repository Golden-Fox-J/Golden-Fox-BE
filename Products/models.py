from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, null=True, blank=True)
    category_type = models.CharField(max_length=256)

    def __str__(self):
        return self.category_type


class Product(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    Title = models.CharField(max_length=256)
    image= models.ImageField(upload_to='uploads/', blank=True,null=True)
    description = models.TextField(default="", null=True, blank=True)
    price = models.IntegerField()
    contact_info = models.CharField(max_length=256)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('Product_detail', args=[str(self.id)])
    

class Comment(models.Model):
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, null=True, blank=True)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.body
    

class Favourite_product(models.Model):
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, null=True, blank=True)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Product.Title

    
class Cart(models.Model):
   
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.owner) 
    
    
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total
    
    
      
    
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product.Title
    
    
    def price(self):
        new_price = self.product.price * self.quantity
        return new_price
  
        
    







    