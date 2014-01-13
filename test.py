import flightmod
import scraper
import config

flights = scraper.readFlights(config.url)

for flight in flights:
	print flight
