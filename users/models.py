from django.db import models
from django.contrib.auth.models import AbstractUser
from config.models import BaseModel

# Create your models here.

class User(AbstractUser):
    USER = 'user'
    Agent = 'agent'
    USER_TYPE = (
        (USER, 'User'),
        (Agent, 'Agent'),
    )
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to='agent/%Y/%m/%d/', verbose_name='photo')
    desc = models.CharField(max_length=255, verbose_name='Bio')
    phone = models.CharField(max_length=50, verbose_name='Tel', default="+998935199999")
    mobile = models.CharField(max_length=50, verbose_name='Mobile', null=True, blank=True)
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    skype = models.CharField(max_length=50, verbose_name='Skype', null=True, blank=True)
    telegram = models.CharField(max_length=50, verbose_name='Telegram', null=True, blank=True, default="https://telegram.org/" )
    instagram = models.CharField(max_length=50, verbose_name='Instagram', null=True, blank=True, default="https://www.instagram.com/")
    facebook = models.CharField(max_length=50, verbose_name='Facebook', null=True, blank=True, default='https://www.facebook.com/')
    twitter = models.CharField(max_length=50, verbose_name='Twitter', null=True, blank=True, default='https://x.com/')
    user_type = models.CharField(max_length=30, choices=USER_TYPE, verbose_name='User Type')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # def save(self, *args, **kwargs):
    #     self.slug = self.first_name + ' ' + self.last_name
    #     super(User, self).save(*args, **kwargs)
    
class Contact(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=255, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')

    class Meta:
        db_table = 'contact'
        verbose_name = 'Kontakt'
        verbose_name_plural = 'Kontaktlar'    
    def __str__(self):
        return self.name