from .models import Banner
def active_banners(request):
    return {"banners": Banner.objects.filter(active=True)[:5]}
