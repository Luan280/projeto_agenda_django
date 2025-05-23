from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    # Seta como deve ser o nome da categoria tanto no plural como no singular
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    # blank torna esse campo opcional
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    password = models.CharField(max_length=50, blank=True)
    # Defini um valor padrão que pega a hora em que a pessoa foi adicionada no DB
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    # Dentro da rota de media dentro da pasta "pictures" vai ter uma pasta com ano e mês de criação
    picture = models.ImageField(blank=True, upload_to='pictures/%y/%m/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    # "on_delete" Se eu deletar a categoria, o que eu faço com o contato

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
