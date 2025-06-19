from house.models import District

def districts_context(request):
    return {
        'districts': District.objects.all()
    }
