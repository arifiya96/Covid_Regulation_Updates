from datetime import date
from bs4 import BeautifulSoup
import requests
import re

#set headers from operating system
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

#get the source url
source = requests.get('http://www.gov.uk/guidance/full-list-of-local-covid-alert-levels-by-area', headers=headers)

#parse into html
soup = BeautifulSoup(source.content, 'html.parser')

#get the last updated div
last_updated = soup.find('div', class_='app-c-published-dates')

#get todays date
the_date = date.today()
today = the_date.strftime("%d %B %Y")
test_date = '23 October 2020'

#check if todays date is in the last updated div
check_date = last_updated.find_all(text=re.compile(today))
if check_date:
    print('Updated today')
else:
    print('No updates')