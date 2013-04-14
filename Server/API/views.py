from API.models import *
from django.http import HttpResponse
from django.utils import simplejson
import datetime
from bs4 import BeautifulSoup
import urllib
from time import strptime

def getEvents(request, year, month, day):
	date_string = year+month+day
	date_search_query = datetime.datetime.strptime(date_string, '%Y%m%d').date()
	event_for_day = Event.objects.filter(date=date_search_query).order_by('-going_count')
	event_list = []
	for event in event_for_day:
		date_fix = event.date.strftime('%m/%d/%Y')
		time_fix = event.time.strftime('%H:%M:%S')
		event_dict = {'identifier': event.pk, 'title': event.title, 'description': event.description, 'time': time_fix, 'date': date_fix, 'address': event.address}
		event_list.append(event_dict)
	json_returned = simplejson.dumps(event_list)
	return HttpResponse(json_returned)

def getEvent(request, identifier):
	event = Event.objects.get(pk=identifier)
	date_fix = event.date.strftime('%m/%d/%Y')
	time_fix = event.time.strftime('%H:%M:%S')
	event_dict = {'identifier': event.pk, 'title': event.title, 'description': event.description, 'time': time_fix, 'date': date_fix, 'address': event.address, 'org': event.org, 'going_count': event.going_count, 'hashtag': event.hashtag}
	json_returned = simplejson.dumps(event_dict)
	return HttpResponse(json_returned)

def scrapeCalendars(request):
	url1 = "http://visitlongmont.org/event/"
	page_source = urllib.urlopen(url1).read()

	soup = BeautifulSoup(page_source, "html5lib")
	events = soup.find_all("div", class_="result-details-wrapper")

	dates = []
	for event in events:
		eventdate = event.select(".date")
		eventdate = eventdate[0].contents
		date_s = eventdate[0]
		date_s = date_s[:-3]

		date_a = []
		date_a = date_s.split(' ')
		month_number = strptime(date_a[1], '%b').tm_mon
		day = int(date_a[0])
		year = int(date_a[2])
		date_obj = datetime.date(year, month_number, day)
		time_obj = datetime.datetime.time(datetime.datetime.now())

		title = event.select(".title")
		title_link = title[0].find_all('a')
		title = title_link[0].contents
		title = title[0]

		description = event.select(".line-container")
		description = description[1].p.contents
		description = description[0]

		address = event.select(".line-container")
		address = address[0].div.contents
		address = address[0]


		new_event = Event.objects.create(title=title, date=date_obj, time=time_obj, description=description, address=address)
		new_event.save()

	return HttpResponse(dates)