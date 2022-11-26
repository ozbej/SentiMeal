from django.shortcuts import render
from django.conf import settings
from ..app.mixins import Directions
#from .models import Items
# Create your views here.
def home(request):
    #if request.method == 'POST':
        #Items.objects.create(name = request.POST['name'])

    #all_items = Items.objects.filter('restaurant name')

    return render(request, 'home.html')




'''
Basic view for routing 
'''
def route(request):

	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'main/route.html', context)


'''
Basic view for displaying a map 
'''
def map(request):

	lat_a = request.GET.get("lat_a")
	long_a = request.GET.get("long_a")
	lat_b = request.GET.get("lat_b")
	long_b = request.GET.get("long_b")
	directions = Directions(
		lat_a= lat_a,
		long_a=long_a,
		lat_b = lat_b,
		long_b=long_b
		)

	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"lat_a": lat_a,
	"long_a": long_a,
	"lat_b": lat_b,
	"long_b": long_b,
	"origin": f'{lat_a}, {long_a}',
	"destination": f'{lat_b}, {long_b}',
	"directions": directions,

	}
	return render(request, 'main/map.html', context)