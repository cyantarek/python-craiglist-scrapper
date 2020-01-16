import scrapy
from scrapy.http import Request
from time import strftime, localtime, gmtime
from datetime import datetime


class CarsSpider(scrapy.Spider):
	def __init__(self, q, mini, maxi, *args, **kwargs):

		super(CarsSpider, self).__init__(*args, **kwargs)
	#
		self.model = q
	#
	#
		with open("states_2.csv", "r+") as file:
			lines = (line.rstrip() for line in file)
			# lines = ''.join("%s".join(line for line in lines if line) % "Ford")
			# lines = list(line.append("Ford") for line in lines if line)
			lines = [(line.format(mini, maxi, q)) for line in lines if line]
			self.start_urls = lines[:200]

	name = "cars"
	allowed_domains = ['craigslist.org']

	# start_urls = ["https://gadsden.craigslist.org/search/cta?postedToday=1&min_prisce=2000&max_price=2500"]
	# start_urls = "https://shoals.craigslist.org/search/cta?postedToday=1&min_price=2000&max_price=2500&query=Ford"

	# start_urls = lines

	def parse(self, response):
		pass
		cars = []

		hxs = scrapy.selector.HtmlXPathSelector(response)
		items = hxs.select("//p[@class='result-info']")[:1]

		for item in items:
			# car = CraigslistSampleCars
			car = {}
			# link = "https://houston.craigslist.org/cto/d/2001-chevy-express-2500/6494745184.html"
			# print(car["link"])
			# yield Request(url=link, callback=self.parse_cars, meta={"car": car, "link": link})

			t1 = item.select("time[@class='result-date']/@datetime").extract()[0]
			fmt = "%Y-%m-%d %H:%M"
			t2 = strftime(fmt, gmtime())
			td = datetime.strptime(t2, fmt) - datetime.strptime(t1, fmt)
			minutes = td.total_seconds()//60

			offset_time = int(minutes) - 360

			print(offset_time)

			if 5 >= offset_time > 0:
				car["title"] = item.select("a/text()").extract()[0]
				car["query"] = self.model
				car["price"] = item.select("span[@class='result-meta']/span[@class='result-price']/text()").extract()[0]

				car["link"] = item.select("a/@href").extract()[0]

				cars.append(car)
				return cars

	def parse_cars(self, response):
		hxs = scrapy.selector.HtmlXPathSelector(response)
		item = hxs.select("//time[@class='date timeago']/text()").extract()[0].replace("\n", "")


		# if "2" in item:
		#     print(item)
		# if hxs.select("time/text()").extract() == "about an hour ago":
		#     car["link"] = link
		#     return car

		pass
