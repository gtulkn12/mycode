#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2018-06-01'  ## start date for data
#    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    enddate = '&end_date=' + input("Enter an End Date: example - 2018-06-01")
    mykey = '&api_key=0Mf8VKcRihe8T2UJn3CweDCu3b03vYGRrsfdgWku' ## replace this with our API key

    neourl = neourl + startdate + enddate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()
