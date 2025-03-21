from django.contrib import admin
from django.contrib.admin import ModelAdmin
from users.models import User, Contact
# Register your models here.

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('username', 'phone', 'is_staff', 'user_type')
    prepopulated_fields = {'slug': ('username',)}


@admin.register(Contact)        
class ContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject')

