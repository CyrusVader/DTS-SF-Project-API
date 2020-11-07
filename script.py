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


def format_historic_data():
	hist_response = historic_request()
	rates_by_date = hist_response["rates"]
	hist_data = []
	for key, value in rates_by_date.items():
		hist_dict = { 'date': key, 'primary_rate': value[primary_currency.upper()], 'secondary_rate': value[secondary_currency.upper()]}
		hist_data.append(hist_dict)
	# Sort data into date order
	hist_data.sort(key = lambda x:x['date'])
	print(hist_data)
	return hist_data


def plot_historic_data():
	formated_data = format_historic_data()
	# Set axis of plot from different data
	df = pd.DataFrame(formated_data)
	x = df['date']
	y1 = df['primary_rate']
	y2 = df['secondary_rate']
	fig = plt.figure(figsize=(15,6))
	plt.xticks(rotation=90)
	# Set labels of plot
	plt.xlabel('Date')
	plt.ylabel('Exchange Rate to Euro')
	# Plot data
	fig.suptitle(primary_currency + " compared with " + secondary_currency + " base EUR Rate", fontsize=16)
	plt.xticks(rotation=90)
	plt.xticks(np.arange(0, len(formated_data), 5))
	plt.plot(x, y1, "-b", label=primary_currency)
	plt.plot(x, y2, "-r", label=secondary_currency)
	plt.legend(loc="upper left")
	plt.show()


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


# Load function
plot_historic_data()