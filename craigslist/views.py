# from django.shortcuts import render
# from scrapy_app import emails
# import os
# from craigslist.utils import start_urls_maker
#
# def index(request):
# 	return render(request, "home.html")
#
# def action(request):
# 	model = request.POST.get("model")
# 	email = request.POST.get("email")
# 	mini = request.POST.get("min")
# 	maxi = request.POST.get("max")
# 	urls = start_urls_maker(model)
# 	# os.system("cd.. & cd scrappy_app & dir")
# 	os.system("cd scrapy_app & rm ./cars.csv & scrapy crawl cars -o cars.csv -t csv -a mini={0} -a maxi={1} -a model={2}".format(mini, maxi, model))
# 	os.system("cd scrapy_app & python ./emails.py %s" % email)
# 	return render(request, "success.html")


from django.shortcuts import render
import os
from craigslist.utils import start_urls_maker
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
	return render(request, "home.html")


@csrf_exempt
def action(request):
	ip = request.META.get('REMOTE_ADDR')
	model = request.POST.get("model")
	mini = request.POST.get("min")
	maxi = request.POST.get("max")

	# os.system("cd.. & cd scrappy_app & dir")
	#   print(os.system("pwd"))

	os.system(
		"cd scrapy_app & del cars.csv & scrapy crawl cars -o cars.csv -t csv -a q={0} -a mini={1} -a maxi={2}".format(model, mini, maxi))

	# os.system("cd. & cd scrapy_app & dir")
	# with open("cars.csv", "r") as file:
	# 	lines = file.readlines()
	# 	print(lines)
	# os.system("cd scrapy_app & python emails.py %s" % email)
	return render(request, "success.html")
