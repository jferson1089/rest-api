from django.db import models

# Create your models here.
class System(models.Model):
    name= models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    price = models.IntegerField(max_length=None)
    production = models.BooleanField(default= True)

    class Meta:
        verbose_name = "System"
        verbose_name_plural = "Systems"

    def __str__(self):
        return self.name + ' ' + self.company + ' ' + self.price

class Games(models.Model):
    title=models.CharField(max_length=100)
    year=models.IntegerField(max_length=4)
    developer=models.CharField(max_length=50)
    system= models.ForeignKey( System, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural= "Games"

    def __str__(self):
        return self.title + ' ' + self.year + ' ' + self.developer