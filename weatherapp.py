from flet import *
import flet as ft

import requests
from PIL import ImageTk,Image

# flet weatherapp.py ->terminal code

#   anahtar değerini openweathermap sitesine üye olarak aldım // i got the key value by becoming a member of the site (openweathermap apı).

url="http://api.openweathermap.org/data/2.5/weather"
anahtar="" #kendi anahtar degerinizi yazın // write your key value

icon_url="http://openweathermap.org/img/wn/{}@2x.png"


def main(page: ft.Page):
    page.window_width=400
    page.window_height=400
    page.title="hava durumu"
    page.vertical_alignment = "center"
    page.horizontal_alignment="center"
    page.bgcolor="#9F9E9A"

    

    deger=ft.TextField(
            hint_text="şehir yaz",
            border_radius=ft.border_radius.all(30),
            filled=True,
            bgcolor="#2AC2C7"  
        )
    
    location=Text("")
    template=Text("")
    condition=Text("")
    iconrsm=ft.Image(src=" ")

    def hava(city):
        params={'q':city,'appid':anahtar,'Lang':'tr'} 
        data=requests.get(url,params=params).json()
        if data:
            city=data["name"].capitalize()
            country=data["sys"]["country"]  # data sys sütunun country değerleri
            temp=int(data["main"]["temp"]-273.15)
            ## icon kısmı
            icon=data["weather"][0]["icon"]
            condition=data["weather"][0]["description"]
            return (city,country,temp,icon,condition) #sırayla döndürcez
        
    def getir(e):
        city=deger.value
        weather=hava(city)
        location.value="{},{}".format(weather[0],weather[1])
        template.value="{}*c".format(weather[2])
        condition.value=weather[4]

        icon=icon_url.format(weather[3])
        iconrsm.src=icon

        page.update()
    
    btn=ElevatedButton("tıkla",on_click=getir)


    page.add(
        Column([deger,location,template,condition,iconrsm,btn],
                alignment="center",  
           horizontal_alignment="center",)
    )
    page.update()
   
ft.app(target=main)