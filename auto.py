import time
import requests
import os

BASE_DIR = "E:\Development World\Development World Resources Backup 14-1-18\Projects\Others\craigslist"
email = "log***4@gmail.com"

with open("query.csv", "r") as file:
	lines = file.readlines()

	for line in lines[:25]:
		try:
			query, mini, maxi = line.split(",")
			requests.post("http://127.0.0.1:8000/action/",
						  data={
							  "model": query,
							  "min": mini,
							  "max": maxi
						  })
		except:
			pass

# os.system("cd. & cd scrapy_app & dir")

with open(BASE_DIR + "\scrapy_app\cars.csv", "r") as file:
	lines = file.readlines()
	if len(lines) > 0:
		os.system("cd scrapy_app & python emails.py %s" % (email))

# que = "bmw 745,300,3000"
#
# query = que.split(",")
#
# model = query[0]
# mini = query[1]
# maxi = query[2]
#
#
# requests.post("http://127.0.0.1:8000/action/", data={"model": model, "min": mini, "max": maxi, "email": "logformat4@gmail.com"})
