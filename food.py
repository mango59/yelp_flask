from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

##Function to formats the phone number 
def format_phone(phone_number):
	phone_number = str(phone_number)
	area_code = phone_number[0:3]
	first_phone = phone_number[3:7]
	last_phone = phone_number[7:10]
	phone_number = "({})-{}-{}".format(area_code, first_phone, last_phone)
	return phone_number

##Function to setup a yelp search, returns a dictionary of searched results 
def yelp_Search(term, location):
	auth = Oauth1Authenticator(
	    consumer_key=os.environ['CONSUMER_KEY'],
	    consumer_secret=os.environ['CONSUMER_SECRET'],
	    token=os.environ['TOKEN'],
	    token_secret=os.environ['TOKEN_SECRET']
	)
	client = Client(auth)

	params = {
		'term': term,
		'lang': 'en',
		'limit': 3
	}

	response = client.search(location, **params)

	businesses = []

	for business in response.businesses:
		businesses.append({"name": business.name, "rating": business.rating, "phone": business.phone})
	return (businesses)


