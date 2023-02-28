from category.models import *

def menu(request):
    links = Category.objects.all()
    return dict(links = links)