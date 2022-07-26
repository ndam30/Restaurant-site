from django.shortcuts import render

# Create your views here.
from first.models import Category, Food


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def smeal(request):
    return render(request, 'special.html')

def teams(request):
    return render(request, 'team.html')

def menus(request):
    caty = Category.objects.all()
    return render(request, 'menu.html', {'cat':caty})

def foods(request,id):
    foody = Food.objects.filter(category_id= id)
    return render(request, 'food.html', {'food':foody})

def search(request):
    if 'key' in request.GET:
        print(1)
        key = request.GET['key']
        keys =Food.objects.filter(name__icontains=key)
        print(key)

    else:
        keys = Food.objects.all()
    return render(request, 'search.html',{'key':keys })