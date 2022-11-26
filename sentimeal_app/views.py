from django.shortcuts import render
#from .models import Items
# Create your views here.
def home(request):
    #if request.method == 'POST':
        #Items.objects.create(name = request.POST['name'])

    #all_items = Items.objects.filter('restaurant name')

    return render(request, 'home.html')