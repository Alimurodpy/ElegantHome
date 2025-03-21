from django.contrib import admin
from django.contrib.admin import ModelAdmin
from blog.models import Blog, BlogComment, BlogCategory

# Register your models here.

@admin.register(BlogCategory)
class BlogCategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class BlogCommentInline(admin.TabularInline):
    model = BlogComment 
    # readonly_fields = ('user', 'comment')
    extra = 3

@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category',)
    search_fields = ('title', 'body')   
    inlines = [BlogCommentInline]
