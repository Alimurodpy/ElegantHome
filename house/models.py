from django.db import models
from config.models import BaseModel
from django.db.models import CASCADE, SET_NULL
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Gallery(BaseModel):
    photo = models.ImageField(upload_to='banner/%Y/%m/%d/', verbose_name='photo')
    house = models.ForeignKey('house.House', CASCADE, verbose_name='house', related_name='gallery')
    
    class Meta:
        db_table = 'gallery'

class HouseType(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(unique=True, verbose_name='Slug')

    class Meta:
        db_table = 'house_type'
        verbose_name = 'Uy_turi'
        verbose_name_plural = 'Uy_turlari' 

    def __str__(self):
        return self.name

class Amenities(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Name')

    class Meta:
        db_table = 'amenities'
        verbose_name = 'Qulaylik'
        verbose_name_plural = 'Qulayliklar '

    def __str__(self):
        return self.name
        
class House(BaseModel):
    # NEW_TO_OLD = 'new to old'
    # FOR_RENT = 'for rent'
    # FOR_SALE = 'for sale'
    # STATUS = (
    #     (NEW_TO_OLD, 'new to old'),
    #     (FOR_RENT, 'for rent'),
    #     (FOR_SALE, 'for sale'),
    # )
    NEW_TO_OLD = 'sotilgan'
    FOR_RENT = 'ijara uchun'
    FOR_SALE = 'sotuvda'
    STATUS = (
        (NEW_TO_OLD, 'sotilgan'),
        (FOR_RENT, 'ijara uchun'),
        (FOR_SALE, 'sotuvda'),
    )
    agent = models.ForeignKey('users.User', SET_NULL, null=True, verbose_name='Agent', related_name='house')
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=255, verbose_name='Address')
    card = models.ImageField(upload_to='house/card/', verbose_name='card') 
    price = models.PositiveIntegerField(verbose_name='Price')
    desc = models.TextField(verbose_name='Description')
    house_type = models.ForeignKey('house.HouseType', CASCADE, verbose_name='house_type', related_name='houses_type')
    district = models.ForeignKey('house.District', CASCADE, verbose_name='district', null=True, blank=True, related_name='houses_district')
    status = models.CharField(max_length=20, choices=STATUS, verbose_name='Status')
    area = models.FloatField(default=0, verbose_name='Area')
    bed = models.PositiveIntegerField(default=0, verbose_name='Bed')
    bath = models.PositiveIntegerField(default=0, verbose_name='Room')
    garage = models.PositiveIntegerField(default=0, verbose_name='Garage')
    amenity = models.ManyToManyField('house.Amenities', verbose_name='amenities')
    video = models.FileField(upload_to='video/', verbose_name='video', null=True, blank=True)
    plan = models.ImageField(upload_to='plan/', verbose_name='plan', null=True, blank=True, default='plan/plan2.jpg')
    location = models.TextField(verbose_name='locations')


    class Meta:
        db_table = 'house'
        verbose_name = 'Uy'
        verbose_name_plural = 'Uylar'

    def __str__(self):      
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class HouseComment(BaseModel):
    house = models.ForeignKey('house.House', CASCADE, verbose_name='house')
    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    comment = models.TextField(verbose_name='Comment')

    class Meta:
        db_table = 'house_comment'

    def __str__(self):      
        return self.name
    
class BannerHouse(BaseModel):
    is_active = models.BooleanField(default=False)
    house = models.ForeignKey('house.House', CASCADE, verbose_name='house', related_name='houses')


    class Meta:
        db_table = 'house_banner'

    def __str__(self):      
        return self.house.name
    
class District(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(unique=True, verbose_name='Slug')

    class Meta:
        db_table = 'district'
        verbose_name = 'Tuman'
        verbose_name_plural = 'Tumanlar' 

    def __str__(self):
        return self.name