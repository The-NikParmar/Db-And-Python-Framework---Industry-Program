from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Product_Mst(models.Model):
    product_name= models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
    
class Product_Subcat(models.Model):
    product_id = models.ForeignKey(Product_Mst, on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_image = models.ImageField(default="",upload_to="images/")
    product_model = models.CharField(max_length=30)
    product_ram = models.CharField(max_length=30)
    
    def __str__(self):
        return self.product_id.product_name