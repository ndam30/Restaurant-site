from django.contrib import admin

# Register your models here.
from accounts.models import Reserve, Table

admin.site.register(Reserve)
admin.site.register(Table)