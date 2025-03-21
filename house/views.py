from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView, TemplateView
from house.models import BannerHouse, House, District
from blog.models import Blog, BlogComment
from users.models import User
from django.shortcuts import redirect
from django.db.models import Q
from django.core.paginator import Paginator

import requests
from django.conf import settings
# Create your views here.
class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')
    
class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html') 



class HomeView(View):
    def get(self, request, *args, **kwargs):
        district = District.objects.all()


        context = {
            'banners': BannerHouse.objects.filter(is_active=True),
            'properties': House.objects.all().order_by('?')[:6],
            'agents': User.objects.filter(user_type=User.Agent).order_by('?')[:3],
            'blogs': Blog.objects.all(),
            'districts': district
        }
        return render(request, 'index.html', context)
    

class PropertyView(View):
    def get(self, request, *args, **kwargs):
        status = request.GET.get('status', None)
        if status == 'sotilgan':
            properties = House.objects.filter(status=House.NEW_TO_OLD)
        elif status == 'ijara_uchun':
            properties = House.objects.filter(status=House.FOR_RENT)
        elif status == 'sotuvda':
            properties = House.objects.filter(status=House.FOR_SALE)
        else:
            properties = House.objects.all()
        
        paginator = Paginator(properties, 6)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {
            'properties': page_obj,
            'status': status
        }

        return render(request, 'property-grid.html', context)


class PropertySingleView(View):
    template_name = 'property-single.html'
    def get(self, request, slug, *args, **kwargs):
        
        property = get_object_or_404(House, slug=slug)
        context = {
            'property': property
        }
        return render(request, self.template_name, context)
    

class BlogGridView(View):
    def get(self, request, *args, **kwargs):
        
        blogs = Blog.objects.all()
        
        paginator = Paginator(blogs, 3)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {
            'blogs': page_obj,
        }
        return render(request, 'blog-grid.html', context)



class BlogSingleView(DetailView):
    model = Blog
    template_name = 'blog-single.html'
    context_object_name = 'blog'
    slug_field = 'slug'
    slug_url_kwarg = 'slug' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = BlogComment.objects.filter(blog=self.get_object())
        return context


class AgentGridView(View): 
    def get(self, request, *args, **kwargs):
        agents = User.objects.filter(user_type=User.Agent)
        
        paginator = Paginator(agents, 3)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {
            'agents': page_obj
        }
        return render(request, 'agents-grid.html', context ) 

class AgentSingleView(DetailView):
    model = User
    template_name = 'agent-single.html'
    context_object_name = 'agent'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    


class FilterView(View):
    def post(self, request, *args, **kwargs):
        keywords = request.POST.get('keywords')
        status = request.POST.get('status')
        district = request.POST.get('address')
        bedrooms = request.POST.get('bedrooms')
        garages = request.POST.get('garages')
        bathrooms = request.POST.get('bathrooms')
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')

        filters = Q()
        if keywords:
            filters &= Q(name__icontains=keywords) 
        if status:
            filters &= Q(status__icontains=status)
        if district:
            filters &= Q(district__name__icontains=district)
        if bedrooms:
            filters &= Q(bed=bedrooms)
        if garages:
            filters &= Q(garage=garages)
        if bathrooms:
            filters &= Q(bath=bathrooms)
        if min_price:
            filters &= Q(price__gte=min_price)
        if max_price:
            filters &= Q(price__lte=max_price)

        print(filters)
        properties = House.objects.filter(filters)
        
        context = {
            'properties': properties
        }
        return render(request, 'property-grid.html', context)
    
    def get(self, request, *args, **kwargs):
        return redirect('/')



STABILITY_API_KEY = "sk-3ftDanfFUXRwYdqBlSrjXhYXxQTpZbeoFS7AM0AXRnlcCwt7"


import os
import requests
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

def generate_design(request):
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_image = request.FILES["image"]

        # 📌 Media kataloglarini yaratish (agar yo'q bo'lsa)
        uploads_path = os.path.join(settings.MEDIA_ROOT, "uploads")
        outputs_path = os.path.join(settings.MEDIA_ROOT, "outputs")

        os.makedirs(uploads_path, exist_ok=True)
        os.makedirs(outputs_path, exist_ok=True)

        # 📌 Yuklangan rasmni saqlash
        image_path = os.path.join(uploads_path, uploaded_image.name)
        path = default_storage.save(image_path, ContentFile(uploaded_image.read()))

        # Stability AI API ga so'rov yuborish
        url = "https://api.stability.ai/v2beta/stable-image/control/sketch"
        headers = {
            "Authorization": f"Bearer {STABILITY_API_KEY}",
            "Accept": "image/*",
        }
        files = {"image": open(image_path, "rb")}
        data = {
            "prompt": "a modern and stylish home interior design",
            "control_strength": 0.7,
            "output_format": "webp",
        }

        response = requests.post(url, headers=headers, files=files, data=data)

        if response.status_code == 200:
            # 📌 AI tomonidan yaratilgan rasmni saqlash
            output_filename = "generated_design.webp"
            output_path = os.path.join(outputs_path, output_filename)

            with open(output_path, "wb") as file:
                file.write(response.content)

            # 📌 Frontendga rasm URL'ini yuborish
            image_url = f"/media/outputs/{output_filename}"
            return render(request, "house/result.html", {"image_url": image_url})

        else:
            return render(request, "house/error.html", {"error": "AI bilan bog'lanishda xatolik yuz berdi!"})

    return render(request, "house/upload.html")


# import requests
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def generate_design(request):
#     if request.method == "POST" and request.FILES.get("image"):
#         uploaded_image = request.FILES["image"]

#         url = "https://api.stability.ai/v2beta/stable-image/control/sketch"
#         headers = {
#             "Authorization": f"Bearer {STABILITY_API_KEY}",
#             "Accept": "image/*",
#         }
#         files = {"image": uploaded_image}
#         data = {
#             "prompt": "a modern and stylish home interior design",
#             "control_strength": 0.7,
#             "output_format": "webp",
#         }

#         response = requests.post(url, headers=headers, files=files, data=data)

#         if response.status_code == 200:
#             return JsonResponse({"status": "success", "image_url": response.url})
#         else:
#             return JsonResponse({"status": "error", "message": "AI bilan bog'lanishda xatolik yuz berdi!"})

#     return JsonResponse({"status": "error", "message": "Noto'g'ri so'rov"})


# class ChatView(TemplateView):
#     template_name = "house/chat.html"


