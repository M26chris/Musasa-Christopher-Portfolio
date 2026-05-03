from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ['title', 'category', 'is_featured', 'date']
    list_filter   = ['category', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']