#importing necessary python-3 modules
import time
import requests



class handwriting_recognition(object):
	def __init__(self,path_to_file):
		self.path_to_file = path_to_file
		self.url = 'https://centralindia.api.cognitive.microsoft.com/vision/v2.0/recognizeText'
		self.key1 = 'b7907519b5f24b749f598472e4b50fa8' #centralindia
		self.key2 = '09f630895e9941f9ae055fca7258fcb2' #centralindia
		self.max_retries = 5
		
	def processRequest(self,json,data,headers,params):
		'''
			sending request to Microsoft Azure API and returning the 
			status-code and Operation-Location header, which gives the
			address to obtain the result
		'''
		retries = 0
		result = None
		while True:
			response = requests.request('post',self.url,json=json,data=data,headers=headers,params=params)
			if response.status_code==429:
				print(response.json())
				if retries<=self.max_retries:
					time.sleep(1)
					retries+=1
					continue
				else:
					print('Failed')
					break
			elif response.status_code==202:
				result = response.headers["Operation-Location"]
			else:
				print("Error:",response.status_code)
				print("Message:",response.json())
			break
		return result

	def OCRTextResult(self,operation_location,headers):
		'''
			function to access the text result, i.e., the json object
			which is obtained using the Operation-Location header
		'''
		retries = 0
		result = None
		while True:
			response = requests.request('get',operation_location,json=None,data=None,headers=headers,params=None)
			if response.status_code==429:
				print(response.json())
				if retries<=self.max_retries:
					time.sleep(1)
					retries+=1
					continue
				else:
					print('Failed')
					break
			elif response.status_code==200:
				result = response.json()
			else:
				print("Error:",response.status_code)
				print("Message:",response.json())
			break
		return result