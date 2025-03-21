from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatImage
import requests
import os

def chat_view(request):
    images = ChatImage.objects.all().order_by('-timestamp')[:10]  # Oxirgi 10 ta rasm
    return render(request, "chat/chat.html", {"images": images})

def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]
        chat_image = ChatImage.objects.create(image=image)

        # AI orqali rasmni yaxshilash
        ai_processed_image_url = process_with_ai(chat_image.image.path)
        if ai_processed_image_url:
            chat_image.processed_image = ai_processed_image_url
            chat_image.save()

        return JsonResponse({"image_url": chat_image.image.url, "processed_image_url": chat_image.processed_image.url if chat_image.processed_image else None})

    return JsonResponse({"error": "No image uploaded"}, status=400)

def process_with_ai(image_path):
    """ AI orqali rasmni yaxshilash uchun API chaqirish """
    api_url = "https://api.stability.ai/v2beta/stable-image/edit"
    api_key = "sk-3ftDanfFUXRwYdqBlSrjXhYXxQTpZbeoFS7AM0AXRnlcCwt7"  # Stability AI API kalitingizni kiriting

    with open(image_path, "rb") as image_file:
        files = {"image": image_file}
        headers = {"Authorization": f"Bearer {api_key}"}

        response = requests.post(api_url, headers=headers, files=files)

        if response.status_code == 200:
            result = response.json()
            return result.get("output_url")

    return None
