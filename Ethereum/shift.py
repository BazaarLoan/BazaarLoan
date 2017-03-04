#!/usr/bin/python27
## Name: 		Shapeshifting Contract
## Description: Exchange BTC to ETH and add or create a contract
#
# Imports
import requests
import json
from bitcoin import *

# Get Exchange Rate
def shift(btc_addr):
	url = "shapeshift.io/shift"
	payload = {"withdrawl": "", "pair": "btc_eth", "returnAddress": btc_addr}
	r = requests.get(url)
	if r.status_code != 200:
		print "Can't contact Server."
		return
	
	rate_data = json.loads(r.text)
	return rate_data

# Genereate bitcoin address
def genPub():
	
	priv = random_key()		# This could be a security concern. Find best solution.
	pub = privtopub(priv)
	addr = pubtoaddr(pub)
	return addr

rtn_addr = genPub()
shift(rtn_addr)