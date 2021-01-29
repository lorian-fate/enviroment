from django.contrib import admin
from MANAGE_MPP.models import UserOver

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    user_ad = 'username'

admin.site.register(UserOver, UserAdmin)
