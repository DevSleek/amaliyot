from django.contrib import admin
from .models import UserModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    search_fields = ('first_name', 'phone_number')
    list_filter = ('first_name', )


admin.site.register(UserModel, UserModelAdmin)
