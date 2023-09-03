from django.db import models

# Create your models here.


class Crud(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    dis = models.TextField()


    def __str__(self):
        return self.title