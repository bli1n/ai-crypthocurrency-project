#!/usr/bin/env python

import time
import hmac
from requests import Request, Session

ts = int(time.time() * 1000)
request = Request('GET', 'https://ftx.com/api/wallet/balances')
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
signature = hmac.new('QxzwsPRc6cKtR4nYKyEk36mG6FRKMjhafWlnm_Ww'.encode(), signature_payload,'sha256').hexdigest()

prepared.headers['FTX-KEY'] = '5iNH-_70FBz5oI-WuFwUbMJjOPrRKOCp4l6IikDp'
prepared.headers['FTX-SIGN'] = signature
prepared.headers['FTX-TS'] = str(ts)

my_session=Session()
response=my_session.send(prepared)
print( response.json())

request = Request('GET', 'https://ftx.com/api/orders?market=BTC-PERP')
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
signature = hmac.new('QxzwsPRc6cKtR4nYKyEk36mG6FRKMjhafWlnm_Ww'.encode(), signature_payload,'sha256').hexdigest()

prepared.headers['FTX-KEY'] = '5iNH-_70FBz5oI-WuFwUbMJjOPrRKOCp4l6IikDp'
prepared.headers['FTX-SIGN'] = signature
prepared.headers['FTX-TS'] = str(ts)

my_session=Session()
response=my_session.send(prepared)
print( response.json()

