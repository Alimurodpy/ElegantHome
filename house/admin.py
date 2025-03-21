from django.contrib import admin
from house.models import (
    House, 
    HouseComment, 
    HouseType, 
    Gallery,
    Amenities,
    BannerHouse,
    District
)

# Register your models here.

class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 3   

@admin.register(HouseType)
class HouseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at')


@admin.register(HouseComment)
class HouseCommentAdmin(admin.ModelAdmin):
    list_display = ('house', 'name', 'email')

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'agent', 'status', 'house_type')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'desc')
    list_filter = ('create_at', 'agent', 'house_type', 'status')
    inlines = [GalleryInline]
    filter_horizontal = ('amenity',)

@admin.register(BannerHouse)
class BannerHouseAdmin(admin.ModelAdmin):
    list_display = ('house', 'is_active')

