from django.db import models


class Product(models.Model):
    title = models.CharField( max_length=300)
    category = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    description
    # Like = models.ForeignKey(Like, on_delete=models.CASCADE)

    def __str__(self):
        return self.title








