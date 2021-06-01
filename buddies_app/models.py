from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Client"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Admin(models.Model):
    main_id = models.AutoField(primary_key=True)
    user_design = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=True)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    profile_pic = models.FileField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

class Client(models.Model):
    main_id = models.AutoField(primary_key=True)
    user_design = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=True)
    contact = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)
    profile_pic = models.FileField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

class Category(models.Model):
    main_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

class Product(models.Model):
    main_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    featured_image = models.ImageField(default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)
    price = models.CharField(max_length=10)
    lesson_purpose = models.CharField(max_length=50)
    student_age = models.CharField(max_length=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()

class Order(models.Model):
    main_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=True)
    description = models.TextField()
    delivery_time = models.CharField(max_length=20)
    no_of_lessons = models.CharField(max_length=10)
    lesson_len_in_hours = models.CharField(max_length=10)
    status = models.CharField(max_length=15)
    review = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=True)
    price = models.CharField(max_length=10)

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(user_design=instance, contact="", address="", profile_pic="",
                                 created_at=datetime.now(), updated_at=datetime.now())
        else:
            Client.objects.create(user_design=instance, contact="", address="", profile_pic="",
                                    created_at=datetime.now(), updated_at=datetime.now())


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.clients.save()