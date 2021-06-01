from django.contrib import admin
from buddies_app import models

# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Admin)
admin.site.register(models.Client)
admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Order)