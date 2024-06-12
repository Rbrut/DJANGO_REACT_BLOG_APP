from django.contrib import admin
from api.models.post import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'slug', 'created', 'modified']

admin.site.register(Post, PostAdmin)