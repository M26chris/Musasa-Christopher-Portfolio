from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ['title', 'category', 'is_published', 'created_at']
    list_filter   = ['is_published', 'category']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']