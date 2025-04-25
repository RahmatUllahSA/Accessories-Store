from django.db import models  #2 templates

class Product(models.Model):   #2 templates
    name = models.CharField(max_length=100)  #2 templates
    price = models.DecimalField(max_digits=10, decimal_places=2)  #2 templates
    description = models.TextField()   #2 templates
    image = models.ImageField(upload_to='products/')  #2 templates

    def __str__(self):  #2 templates
        return self.name  #2 templates
