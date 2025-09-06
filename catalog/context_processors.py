from .models import Category
def menu_categories(request):
    cats = Category.objects.filter(menu=True, parent__isnull=True).order_by("name")
    return {"menu_categories": cats}
