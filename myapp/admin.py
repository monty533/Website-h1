from django.contrib import admin
from myapp.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone']

admin.site.register(Contact,ContactAdmin)