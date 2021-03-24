from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'first_name', 'last_name', 'email', 'bio', 'role')
    search_fields = ('user',)
    empty_value_display = '-НИЧЕГО-'


admin.site.register(User, UserAdmin)
