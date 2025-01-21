from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    firts_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True) # blank torna esse campo opcional
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    password = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now) # Defini um valor padrão que pega a hora em que a pessoa foi adicionada no DB
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%y/%m/') # Dentro da rota de media dentro da pasta "pictures" vai ter uma pasta com ano e mês de criação


    def __str__(self):
        return f"{self.firts_name} {self.last_name}"
