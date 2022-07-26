from django.contrib import admin

# Register your models here.
from discuss.models import Comments
from first.models import Food, Category, Order

admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Comments)