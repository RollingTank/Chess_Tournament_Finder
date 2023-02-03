import requests
from bs4 import BeautifulSoup
import pandas
from datetime import datetime
import re

#state_abb = input("Enter the State Abbreviation or enter 'All': ")
def state_abb2(state_abb):
    if state_abb == "":
        state_abb = 'All'
        return state_abb
    else:
        state_abb = state_abb
        return state_abb
#onlinecheck = input("Enter  if you online; enter x if you want in-person: ")
def onlinecheck2(oneorTwo):
    if oneorTwo.lower() == 'o':
        oneorTwo = str(1)
        return str(oneorTwo)
    elif oneorTwo.lower() == 'in':
        oneorTwo = str(2)
        return str(oneorTwo)
    else:
        oneorTwo = 'All'
        return str(oneorTwo)
month = str(datetime.now().month)
day = str(datetime.now().day)
year = str(datetime.now().year)
#mile_radius = input("Enter miles from your zip code that you want to search: ")
def mile_radius2(mile_radius):
    if mile_radius == '':
        mile_radius = 50
        return str(mile_radius)
    else:
        mile_radius = mile_radius
        return str(mile_radius)
#zip_code = input("Enter your United States ZipCode: ")
def zip_code2(zip_code):
    if zip_code == "":
        zip_code = ""
        return str(zip_code)
    else:
        zip_code = zip_code
        return str(zip_code)

def main(state0, online0, zipcode0, mile_rad0):
    l = []
    for x in range(0, 3):
        page_num = str(x)
        r = requests.get("https://new.uschess.org/upcoming-tournaments?combine=&field_event_address_administrative_area={}&field_online_event_value={}&field_event_dates_occurrences%5Bmin%5D={}%2F{}%2F{}&field_event_dates_occurrences%5Bmax%5D=&field_geofield_proximity%5Bvalue%5D={}&field_geofield_proximity%5Bsource_configuration%5D%5Borigin_address%5D={}&field_fide_rated_value=0&page={}".format(state0, online0, month, day, year, mile_rad0, zipcode0, page_num))

        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        all = soup.find_all("span", {"class":"field-content"})
        for y in all:
            d = {}
            try:
                d["Name"]=y.find("h3", {"class":"title3"}).text
            except:
                d["Name"]=None
            try:
                d["Location"]=y.find("div", {"class":"address"}).text
            except:
                d["Location"]=None
            try:
                d["Date"]=y.find("div", {"class":"date-recur-interpretaton"}).text
            except:
                d["Date"]=None
            try:
                d["Organizer"]=y.find("div", {"class":"organizer-name"}).text
            except:    
                d["Organizer"]=None
            try:
                d["Information"]=y.find("div", {"class":"event-information"}).text
            except:
                d["Information"]=None
            try:
                attribute={"href": re.compile("^https://new.uschess.org/")}
                d["Link"]=y.get('href')
                #d["Link"]=y.find("a", {"class":"more-link"}).text
            except:
                d["Link"]=None
            l.append(d)

    df = pandas.DataFrame(l)
    df.to_csv("C:/Users/kulta/Desktop/UserchessTourney.csv")
