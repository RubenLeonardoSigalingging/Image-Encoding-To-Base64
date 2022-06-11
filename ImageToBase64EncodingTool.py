#!/usr/bin/env python3


# Created By: Ruben Leonardo Sigalingging.
# Created On: Saturday, June 11, 2022, 09:34 AM.
# Using: Python Programming Language Version 3.8.10

# Function: To Encode Image Into Base64 String, Using Python Programming Language Version 3.8.10

# This Tool Using: Indonesia Language.

# Dibuat Oleh: Ruben Leonardo Sigalingging.
# Dibuat Pada: Sabtu, 11 Juni 2022, 09:34.
# Menggunakan: Bahasa Pemrograman Python Versi 3.8.10

# Fungsi : Untuk Mengkodekan Gambar Menjadi String Base64, Menggunakan Bahasa Pemrograman Python Versi 3.8.10

# Alat Ini Menggunakan: Bahasa Indonesia.

def image_to_base64(created_by = "Ruben Leonardo Sigalingging"):
	# LANGKAH PERTAMA IMPORT MODULE PYTHON
	import base64
	import pyfiglet
	import requests
	import sys
	import time
	import datetime
	import os
	print("[!] Created By: Ruben Leonardo Sigalingging.")
	print("[!] Created On: Saturday, June 11, 2022, 09:48 AM.")
	print("[!] Using: Python Programming Language Version 3.8.10")
	print("----- IMAGE TO BASE64 -----")
	print("\n")


	import json
	import urllib
	from urllib import request
	json_data = "http://ip-api.com/json/"
	api_ipify = requests.get("https://api.ipify.org/").text
	print("---IP ADDRESS---\n")
	print(f"[!] Your Public IP Address: {api_ipify}")
	http_requests = request.urlopen(json_data)
	# parse json data
	# URAIKAN DATA JSON
	parse_json_data = json.loads(http_requests.read())
	# print(parse_json_data)
	print(f"[!] Status: {parse_json_data['status']}")
	print(f"[!] Country: {parse_json_data['country']}")
	print(f"[!] Country Code: {parse_json_data['countryCode']}")
	print(f"[!] Region Name: {parse_json_data['regionName']}")
	print(f"[!] City: {parse_json_data['city']}")
	print(f"[!] Zip: {parse_json_data['zip']}")
	print(f"[!] Latitude: {parse_json_data['lat']}")
	print(f"[!] Longitude: {parse_json_data['lon']}")
	print(f"[!] Timezone: {parse_json_data['timezone']}")
	print(f"[!] Internet Service Provider: {parse_json_data['isp']}")
	print(f"[!] Organization: {parse_json_data['org']}")
	print(f"[!] Autonomous System Number: {parse_json_data['as']}")
	print(f"[!] Query: {parse_json_data['query']}")
	print("\n\n\n")
	# ip_address = requests.get("http://ip-api.com/json/").text


	image = input("[!] Enter Image File Name: ") 
	# ---Mengetahui ada tidaknya suatu file---
	# ---Knowing whether a file exists---
	if os.path.isfile(image)==True:
		print("\n")
		print("[!] Files Can Be Found!")
	else:
		print("[!] File Not Found!")

		
	open_and_read_image_file = open(image,"rb")
	reading = open_and_read_image_file.read()
	print("\n")
	base64_strings = base64.b64encode(reading)
	print(f"[!] Image Encoding Result To Base64: \n{base64_strings}")
	print("\n\n\n")
# image_to_base64()


import pyfiglet
tema = pyfiglet.figlet_format("Base64",font="slant")
print(tema)
ask = "Y"
while (ask == "Y"):
	image_to_base64()
	answer = input("[!] Do You Want To Try Again? (Y/n): ")
	if answer != "Y":
		break