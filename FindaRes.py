import json, requests
CLIENT_ID = "LBZZAKKU0NECPFNDANYP5CFHC1SZN3X0OIIS15Y11KG5UQO2"
CLIENT_SECRET = "PB0MEXGSDSRWDM50ZRJBWEK5AT1PBJYNYFCUUWXNOW331I1O"


def getGeocodeLocation(inputString):
	
	GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
	address = inputString
	params = {
		'address': address,
		'sensor': 'false',
		'region': 'uk'
		}
	# Do the request and get the response data
	req = requests.get(GOOGLE_MAPS_API_URL, params=params)
	res = req.json()
	# Use the first result
	result = res['results'][0]
	geodata = dict()
	geodata['lat'] = result['geometry']['location']['lat']
	geodata['lng'] = result['geometry']['location']['lng']
	return (geodata['lat'],geodata['lng'])
	#return
def findARestaurant(food,address):
	
	# Call getGeocodeLocation to get the long and lat	
	long_lat= getGeocodeLocation(address)
	
	FourSquare_API_URL = 'https://api.foursquare.com/v2/venues/explore'
	long_lat = str(long_lat[0]) + "," + str(long_lat[1])
	params = dict( client_id=CLIENT_ID, client_secret=CLIENT_SECRET,v='20170801', ll= long_lat,query=food,limit=1)
	resp = requests.get(url=FourSquare_API_URL, params=params)
	data = resp.json()
	print("Restaurant Name 	: 	", data['response']['groups'][0]['items'][0]['venue']['name'])
	print("Restaurant Phone 	: 	", data['response']['groups'][0]['items'][0]['venue']['contact']['phone'])
	print("Restaurant Address   :	", data['response']['groups'][0]['items'][0]['venue']['location']['address'])
	print (" ")
	return
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Indian", "Seattle, USA")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")


