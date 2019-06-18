#importing necessary python-3 modules
import time
import requests
from apiKeys import keys

keys = keys()

url = 'https://centralindia.api.cognitive.microsoft.com/vision/v2.0/recognizeText'
key1 = keys[0] #Insert your first api key here
key2 = keys[1] #Insert your second api key here
max_retries = 5
		
def processRequest(json,data,headers,params):
	'''
		sending request to Microsoft Azure API and returning the 
		status-code and Operation-Location header, which gives the
		address to obtain the result
	'''
	retries = 0
	result = None
	while True:
		response = requests.request('post',url,json=json,data=data,headers=headers,params=params)
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

def OCRTextResult(operation_location,headers):
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


def processImage(path):
	'''
      function that takes the path to the image as a parameter, and
      prints the handwritten text recognized.
    '''
	pathToImage = path
	with open(pathToImage, 'rb') as f:
		data = f.read()

	#setting parameters for API
	params = {'mode':'Handwritten'}
	headers = dict()
	headers['Ocp-Apim-Subscription-Key']=key1
	headers['Content-Type'] = 'application/octet-stream'
	json = None

	#Posting request to Microsoft Azure server
	operation_location = processRequest(json,data,headers,params)

	#Getting JSON object from MS Azure server
	result = None
	if(operation_location!=None):
		while True:
			time.sleep(1)
			result = OCRTextResult(operation_location,headers)
			if result['status']=='Succeeded' or result['status']=='Failed':
				break

	#retrieving text as a complete string, line-wise
	detected_text = result['recognitionResult']['lines']
	lines = []
	for i in range(0,len(detected_text)):
		line_text = detected_text[i]['text']
		lines.append(line_text)

	for j in lines:
		print(j)

processImage("./image1.jpeg")
processImage("./image2.jpeg")