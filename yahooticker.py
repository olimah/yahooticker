import uno
import unohelper
import requests
import re

from com.olivermahmoudi.programming.yahooticker import XYahooTicker

class YahooTickerClass( unohelper.Base, XYahooTicker ):
	def __init__( self, ctx ):
		self.ctx = ctx

	def yahooticker( self, instrument ):
		"Query yahoo finance with instrument return instrument's current market value"
		yahoo_base_url = "http://finance.yahoo.com/quote/"
		url_to_query = yahoo_base_url + instrument
		try:
			ws = requests.get(url_to_query)
		except requests.exceptions.RequestException as e:
			print e
			sys.exit(1)
		content = ws.text
		regex = re.compile(r"<!--\sreact-text:\s36\s-->[0-9]+,?[0-9]*\.[0-9]+<!--\s/react-text\s-->")
		result = regex.search(content)
		if result:									# We have found something...
			regex = re.compile(r"[0-9]+,?[0-9]*\.[0-9]+")	# Extract
			result = regex.search(result.group(0))			# the price
			return result.group(0)							# and return it...
		else:
			return "Nothing found"							# Futile search
 
def createInstance( ctx ):
	return YahooTickerClass( ctx )

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation( \
	createInstance,"com.olivermahmoudi.programming.yahooticker.python.YahooTickerClass",("com.sun.star.sheet.AddIn",),)
