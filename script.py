# Foreign exchange rate API tool

# Import required Modules / Packages
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime


# Links to the Curerency api
historical_url = 'https://api.exchangeratesapi.io/history'


def historic_request():
	# Creating varible of JSON response and return
	response = requests.get(request_url)
	historic_data = json.loads(response.text)
	return historic_data


# requesting input from the user on details of request
start_date = validate(input("What start date would you like to look at? (Date format: YYYY-MM-DD):"))
print("Choosen start date: " + start_date)
end_date = validate(input("What end date would you like to look at? (Date format: YYYY-MM-DD):"))
print("Choosen end date: " + end_date)
primary_currency = input("What is the primary currency you would like to compare? (eg. USD)").upper()
print("Choosen primary currency: " + primary_currency)
secondary_currency = input("What is the secondary currency you would like to compare? (eg. GBP)").upper()
print("Choosen secondary currency: " + secondary_currency)
# Concatenate request URL from user input data
request_url = historical_url + "?start_at=" + str(start_date) + "&end_at=" + str(end_date) + "&symbols=" + primary_currency.upper() + "," + secondary_currency.upper()
