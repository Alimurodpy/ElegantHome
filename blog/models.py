from django.db import models
from config.models import BaseModel
from django.db.models import CASCADE
from ckeditor.fields import RichTextField

# Create your models here.

class BlogCategory(BaseModel):
    name = models.CharField(max_length=100, verbose_name='name')
    slug = models.SlugField(unique=True, verbose_name='slug')

    class Meta:
        db_table = 'blog_category'

    def __str__(self):
        return self.name

class Blog(BaseModel):
    title = models.CharField(max_length=100, verbose_name='title')
    slug = models.SlugField(unique=True, verbose_name='slug')
    category = models.ForeignKey('blog.BlogCategory', CASCADE, related_name='blogs')
    card = models.ImageField(upload_to='blog/card/', verbose_name='card')
    banner = models.ImageField(upload_to='blog/banner/', verbose_name='banner')
    autor = models.ForeignKey('users.User', CASCADE, related_name='blogs')
    body = RichTextField()

    class Meta:
        db_table = 'blog'

    def __str__(self):
        return self.title
    
class BlogComment(BaseModel):
    user = models.ForeignKey('users.User', CASCADE)
    blog = models.ForeignKey('blog.Blog', CASCADE)
    comment = models.TextField(verbose_name='Comment')

    class Meta:
        db_table = 'blog_comment'

    def __str__(self):
        return self.user.first_name
    