# Handwriting-Recognition
This is a python module to use Micrsoft Azure's Computer Vision API for handwriting recognition.

The Computer Vision API of Microsoft Cognitive Services is a REST based service. Images in JPEG/PNG/BMP format can be submitted, with dimensions between 50x50 to 3200x3200 pixels, and a file size smaller than 4 MB.
It returns information about the visual content in the image as a JSON object.

## Description

```
  def processRequest(json,data,headers,params):
    '''
      sending request to Microsoft Azure API and returning the 
      status-code and Operation-Location header, which gives the
      address to obtain the result
    '''
```

```
  def OCRTextResult(operation_location,headers):
    '''
      function to access the text result, i.e., the json object
      which is obtained using the Operation-Location header
    '''
```

```
  def processImage(path):
    '''
      function that takes the path to the image as a parameter, and
      prints the handwritten text recognized.
    '''
```

## Sample Input and Output
### Sample Image 1:
![Alt text](https://github.com/BhavyaC16/Handwriting-Recognition/blob/master/image1.jpeg)

### Output

```
The quick brown fox jumps over the lazy dog.
```

### Sample Image 2:
![Alt text](https://github.com/BhavyaC16/Handwriting-Recognition/blob/master/image2.jpeg)

### Output

```
0 1 2 3 4 5 6 7 8 9
```
