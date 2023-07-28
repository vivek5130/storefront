from django.db import models

#makemigrations -> to detect changes made in model.py or fields and store it in a file
#migrate -> to apply pending change created by makemigrations


class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id =  models.CharField(max_length=20)
    product_name = models.CharField(max_length=40)
    price = models.CharField(max_length=50, default =0)
    product_quantity = models.CharField(max_length=20)
    product_discount = models.CharField(max_length=20)
    image = models.ImageField(upload_to = "home/images", default = "")

    def __str__(self):
        return self.product_name
    

