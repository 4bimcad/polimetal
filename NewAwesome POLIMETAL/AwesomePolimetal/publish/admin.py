from django.contrib import admin
from .models import Company, Category, Advert, AdvertCategory


admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Advert)
admin.site.register(AdvertCategory)
