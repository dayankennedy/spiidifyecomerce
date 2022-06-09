from django.db import models


# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    category=models.CharField(max_length=100)
    image=models.ImageField()
    def __str__(self):
        return self.title


class OderProduct(models.Model):
    #author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    pass



