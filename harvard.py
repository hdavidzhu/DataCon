# Ryan Louie and David Zhu
# 8/8/2015
# ryan.louie@students.olin.edu | hdavidzhu@gmail.com

# Requirements.
import requests
import time
from bs4 import BeautifulSoup

# First, import the whole page.
base_url = 'http://news.harvard.edu/gazette/harvard-events/'
# unique_href = ''

# Loooking in `event-block`, we have:
# img_wrapper: For the image thumbnail location.
# date_stamp: When the event is happening.
# h2: The title of the event.
  # event_info: A short description.
  # event_date: The exact date. 
    # TODO; Not sure how its different from date_stamp

translation = {
  
}

request = requests.get(base_url)
soup = BeautifulSoup(request.content, 'lxml')

events = []
for index, event_block in \
  enumerate(soup.find_all('div', class_="event-block")):
  # print event_block

  # Define the actual data.
  event = {}

  event_info = event_block.find('div', class_="event_info")
  event_info = event_info.text.lstrip().rstrip()
  print "Info: " + event_info

  event_date= event_block.find('div', class_="event-date")
  event_date = event_date.text.lstrip().rstrip()
  # TODO: Convert into a date object.
  # event_date = time.strptime(event_date, "")
  print "Date: " + event_date

# print request
# print soup
