import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'State_of_Country':0, 'Market_Category':103, 'Product_Category':0, 'Grade':1, 'High_Cap_Price':9669})

print(r.json())