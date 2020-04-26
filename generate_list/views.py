from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'generate_list/home.html', {'sausage':'this text will appear whenever you write sausage'})

def list(request):

	thelist = []

	list_fishing = ['rod', 'reel', 'squid']
	list_work = ['macbook', 'ipad']
	list_bike = ['helmet', 'water', 'glasses']
	list_overnight = ['toothbrush', 'vitamins']

	if request.GET.get("I'm going fishing"):
		thelist.extend(list_fishing)

	if request.GET.get("I'm staying overnight"):
		thelist.extend(list_overnight)

	if request.GET.get("I'm travelling by bike"):
		thelist.extend(list_bike)

	if request.GET.get("I'm going to work"):
		thelist.extend(list_work)

	# thelist = ("[{0}]".format(', '.join(map(str, thelist))))

	return render(request, 'generate_list/list.html', {'list':thelist})