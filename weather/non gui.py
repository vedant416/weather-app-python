from tkinter import *
import requests
import bs4

def weather():
    global l2
    global cityname
    global days
    global lw
    cityname=input("Enter city name: ")
    days="today"
    
    url='https://www.google.com/search?q=%s+weather+%s'%(cityname,days)

    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',}
    css='#wob_tm'
    
    request=requests.get(url,headers=headers)
    request.raise_for_status()
    soup=bs4.BeautifulSoup(request.text,"html.parser")
    
    temperature=soup.select('#wob_tm')
    timedate=soup.select('#wob_dts')
    location=soup.select('#wob_loc')
    weathercondition=soup.select('#wob_dc')
    
    l=location[0].text
    t=timedate[0].text
    w=weathercondition[0].text
    temp=temperature[0].text

    a="\nLocation: %s\n\nDay: %s\n\nWeather: %s\n\nTemperature: %s degree celsius\n\n"%(l,t,w,temp)
    
    print(a)

weather()
