from django.db import models

class Size(models.Model):
    title = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title
    

class Pizza(models.Model):
    topping1 = models.CharField(max_length=50)
    topping2 = models.CharField(max_length=50)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.topping1} {self.topping2} {self.size}"
