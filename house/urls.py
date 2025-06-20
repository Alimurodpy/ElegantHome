from django.urls import path
from house.views import (
    HomeView,
    AboutView,
    PropertyView,
    PropertySingleView,
    AgentGridView, 
    AgentSingleView,
    BlogGridView,
    ContactView,
    BlogSingleView,
    FilterView
)
from .views import generate_design
from django.shortcuts import render
from django.http import Http404

app_name = 'house'
def my_view(request):
    raise Http404  

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


handler404 = "apps.your_app.views.custom_404_view"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('property-grid/', PropertyView.as_view(), name='property'),
    path('property-single/<slug:slug>', PropertySingleView.as_view(), name='property_single'),
    path('agents-grid/', AgentGridView.as_view(), name='agents_grid'),
    path('agent-single/<slug:slug>', AgentSingleView.as_view(), name='agent_single'),
    path('blog-grid/', BlogGridView.as_view(), name='blog_grid'),
    path('blog-single/<slug:slug>', BlogSingleView.as_view(), name='blog_single'),
    path('filter/', FilterView.as_view(), name='filter'),
    path("generate-design/", generate_design, name="generate_design"),
    # path("chat/", ChatView.as_view(), name="chat"), 
    # path('chat/', chat_view, name="chat"),
    # path('upload/', upload_image, name="upload_image"),
]

