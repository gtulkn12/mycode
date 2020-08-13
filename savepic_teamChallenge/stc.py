#!/usr/bin/python3
import requests
import wget


#Jeffrey
def api_pull():
    choice = input("What Pokemon would you like a picture of? ").lower()
    url = "https://pokeapi.co/api/v2/pokemon/" + choice + "/"
    return url

#Wonil
def json_conv(poke_api):
   # send a get request to poke_api
    try:
        json2python = requests.get(poke_api).json()
        # the value of json2python is the whole dictionary of bulbasaur!
        return json2python
    except:
        print("Invalid URL provided. Please try again.")


#Malik
def api_slice(json2python):
    poke_pic= json2python["sprites"]["front_default"]
    return poke_pic

#Joe
def wget_pic(imagelink):
    wget.download(imagelink, "/home/student/mycode")



def main():
    wget_pic(api_slice(json_conv(api_pull())))

main()
