import requests
from bs4 import BeautifulSoup
import pandas
from datetime import datetime
import re
from ics import Calendar, Event


def split(list_input, split_char):
    lnew1 = []
    l = []
    for x in list_input:
        if (x == split_char):
            l.append(lnew1)
            lnew1 = []
            continue
        lnew1.append(x)
    l.append(lnew1)
    return l


def returnBeginningDate(df, s):
    l = s.split()
    l1 = split(l, "-")
  #  print(l1)
    d = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    dayStart = l[2].split(",")[0]
    monthStart = d[l[1].split(" ")[0]]
    yearStart = l[3]
    return f"{yearStart}-{monthStart}-{dayStart}"


def returnEndDate(df, s):
    l = s.split()
    l1 = split(l, "-")
  #  print(l1)
    d = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    if (len(l1) > 1):
        dayEnd = l1[1][2].split(",")[0]
        monthEnd = d[l1[1][1].split(" ")[0]]
        yearEnd = l1[1][3]
        return f"{yearEnd}-{monthEnd}-{dayEnd}"


# state_abb = input("Enter the State Abbreviation or enter 'All': ")
def state_abb2(state_abb):
    if state_abb == "":
        state_abb = 'All'
        return state_abb
    else:
        state_abb = state_abb
        return state_abb
# onlinecheck = input("Enter  if you online; enter x if you want in-person: ")


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
# mile_radius = input("Enter miles from your zip code that you want to search: ")


def mile_radius2(mile_radius):
    if mile_radius == '':
        mile_radius = 50
        return str(mile_radius)
    else:
        mile_radius = mile_radius
        return str(mile_radius)
# zip_code = input("Enter your United States ZipCode: ")


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

        all = soup.find_all("span", {"class": "field-content"})
        for y in all:
            d = {}
            try:
                d["Name"] = y.find("h3", {"class": "title3"}).text
            except:
                d["Name"] = None
            try:
                d["Location"] = y.find("div", {"class": "address"}).text
            except:
                d["Location"] = None
            try:
                d["Date"] = y.find("div", {"class": "dates"}).text
            except:
                d["Date"] = None
            try:
                d["Organizer"] = y.find(
                    "div", {"class": "organizer-name"}).text
            except:
                d["Organizer"] = None
            try:
                d["Information"] = y.find(
                    "div", {"class": "event-information"}).text
            except:
                d["Information"] = None
            try:
                attribute = {"href": re.compile("^https://new.uschess.org/")}
                d["Link"] = y.get('href')
                # d["Link"]=y.find("a", {"class":"more-link"}).text
            except:
                d["Link"] = None
            l.append(d)

    df = pandas.DataFrame(l)
    df.to_csv("C:/Users/kulta/Desktop/chessTourney.csv")


def createICSEvent():
    df = pandas.read_csv("C:/Users/kulta/Desktop/chessTourney.csv")
    c = Calendar()
    for index, row in df.iterrows():
        e = Event()
        e.name = row["Name"]
        e.location = row["Location"]
        e.description = row["Information"]
        e.begin = returnBeginningDate(df, row["Date"])
        e.end = returnEndDate(df, row["Date"])
        e.make_all_day()
        c.events.add(e)
    with open("C:/Users/kulta/Desktop/chessTourney.ics", "w") as f:
        f.writelines(c)


if __name__ == "__main__":
    createICSEvent()
