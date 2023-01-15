from django.db import models

#Any time that you want to modify a class or a table ,this is the two cmd to insert:
# python manage.py makemigrations and  python manage.py migrate

class Products(models.Model):
    name = models.CharField(max_length=50)
    price=models.DecimalField(max_digits=1000, decimal_places=2)
    description=models.TextField()
    
    class Meta:
        verbose_name=("Product")
        verbose_name_plural=("Products")

    def __str__(self):
        return self.name