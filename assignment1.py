###################################

####  Python Assignment Code   ####

###################################

#execfile( 'c:/Users/Sean Ankenbruck/Desktop/MSA/Python/assignment1.py' )

#Import appropriate packages 
import urllib2
import json
import csv
import time


# List of cities to query 
# Cities must be entered as '(Country or State abrev.)/City.json' to append to API request 
location = [\
 'GH/Accra.json',\
  'DE/Burghausen.json',\
  'AR/Buenos-Aires.json',\
  'IN/Chennai.json',\
  'CN/Lengshuijiang.json',\
  'PE/Lima.json',\
  'GB/London.json',\
  'MX/Mexico_City.json',\
  'RU/Moscow.json',\
  'CA/Nanaimo.json',\
  'ES/Pamplona.json',\
  'AU/Perth.json',\
  'NC/Cary.json',\
  'zmw:00000.1.78486.json',\
  'UZ/Tashkent.json',\
  'GR/Thessaloniki.json',\
  'PL/Gliwice.json'\
]


# Create CSV file with headers
with open( 'c:/Users/.../Python/temp.csv', 'wb' ) as fp:
	out = csv.writer( fp )
	out.writerow(["City","Min 1","Max 1","Min 2","Max 2","Min 3","Max 3","Min 4","Max 4","Min 5","Max 5"])
	# Obtain location and temperature data for each city in our list
	for i in location:
		# Limit number of requests to 10 per minute
		time.sleep(6)
		# API Request	
		f = urllib2.urlopen( 'http://api.wunderground.com/api/api_key/forecast10day/conditions/q/'+ i)
		json_string = f.read()
		parsed_json = json.loads( json_string )
		# Extract Necessary Data
		# Full Location Description
		loc = parsed_json['current_observation']['display_location']['full']
		# Forecast min and max (in celsius) for current day + 1 to 5
		results = []
		for i in range( 5 ):
			mini = parsed_json['forecast']['simpleforecast']['forecastday'][i]['low']['celsius']
			maxi = parsed_json['forecast']['simpleforecast']['forecastday'][i]['high']['celsius']
			results.append(mini)
			results.append(maxi)
			i = i + 1
		# Write each response to a new row in the csv file
		out.writerow( [loc] + results )
	# Close URL connection 
	f.close()
# Close CSV file
fp.close()
# Status : Passed
