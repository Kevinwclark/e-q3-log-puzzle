import requests

r = requests.get('https://code.google.com/edu/languages/google-python-class/images/puzzle/a-babf.jpg')
print(r.text)