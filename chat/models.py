from django.db import models

class ChatImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    processed_image = models.ImageField(upload_to='processed/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} - {self.timestamp}"
