from account.models import CustomUser 
from django.db import models
from django.urls import reverse




class Category(models.Model):
    owner = models.ForeignKey(CustomUser(),on_delete=models.CASCADE, null=True, blank=True)
    category_type = models.CharField(max_length=256)

    def __str__(self):
        return self.category_type


class Product(models.Model):
    owner = models.ForeignKey(CustomUser(), on_delete=models.CASCADE, null=True, blank=True)
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
    owner = models.ForeignKey(CustomUser(),on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255,default="Unknown")
    Product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.body
    

class Favourite_product(models.Model):
    owner = models.ForeignKey(CustomUser(),on_delete=models.CASCADE, null=True, blank=True)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('owner', 'Product')
    
    def __str__(self):
        return self.Product.Title






    
