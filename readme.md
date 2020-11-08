# Exchange Rate Comparison Tool

## Project Overview
A tool which allows you to select two currencies within a given time frame and compare the exchanges rates over time plotting them to a graph to visulise the data. The script is written in Python 3 using the following libaries: virtualenv, json, requests, pandas, numpy and matplotlib.

## How to use (Windows)
1. Create virtual Enviroment in a new directory using:

```python
py -m venv env
```
2. Activate the virtual enviroment using:
```python
\env\Scripts\activate.bat
```
3. Install required packages using pip requirements.txt
```python
pip install -r requirements.txt --no-index --find-links file:///tmp/packages
```
4. Run script using:
```python
py script.py
```
5. The script will request input for start date and end date as well as two currencies that you would like to compare with the base rate of the Euro

## Foreign Exchange Rate Currency Conversion API
Website: https://exchangeratesapi.io/
The Foreign Exchange Rate API is a free service which provides current and historical foreign exchange rates which have been published by the European Central bank.

Latest rates API usage:
```
GET https://api.exchangeratesapi.io/latest HTTP/1.1
```
Historic rates API usage:
```
GET https://api.exchangeratesapi.io/2010-01-12 HTTP/1.1
```

## External Library References
Matplotlib - https://matplotlib.org/
Pandas - https://pandas.pydata.org/
Numpy - https://numpy.org/

# Future Improvements
Add ability to use multiple data sources for the currency conversion data and allow for the ability to change the base rate of the conversion to allow for better analyse of different currencies. Create a web application interface using the Django or Flask web libraries allowing for a user interface which would let the user have more control over the query to the API and how the data is being displayed.