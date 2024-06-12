from django.contrib import admin
from api.models.user import User

# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'joined']

admin.site.register(User, UserAdmin)