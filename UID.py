import requests

# 定义URL
a=input("请输入你想要伪造的国家代号：例如cn，hk....")
url = 'https://generator.addressgenerator.net/api/generator?url=%2F'
url=url+a
# 发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析JSON响应
    data = response.json()
    
    # 整理输出
    address = data.get('Address', 'N/A')
    telephone = data.get('Telephone', 'N/A')
    city = data.get('City', 'N/A')
    zip_code = data.get('Zip_Code', 'N/A')
    state = data.get('State', 'N/A')
    expires = data.get('Expires', 'N/A')
    credit_card_type = data.get('Credit_Card_Type', 'N/A')
    credit_card_number = data.get('Credit_Card_Number', 'N/A')
    cvv2 = data.get('CVV2', 'N/A')
    full_name = data.get('Full_Name', 'N/A')
    gender = data.get('Gender', 'N/A')
    birthday = data.get('Birthday', 'N/A')
    title = data.get('Title', 'N/A')
    
    # 打印输出
    print(f"Address: {address}")
    print(f"Telephone: {telephone}")
    print(f"City: {city}")
    print(f"Zip Code: {zip_code}")
    print(f"State: {state}")
    print(f"Expires: {expires}")
    print(f"Credit Card Type: {credit_card_type}")
    print(f"Credit Card Number: {credit_card_number}")
    print(f"CVV2: {cvv2}")
    print(f"Full Name: {full_name}")
    print(f"Gender: {gender}")
    print(f"Birthday: {birthday}")
    print(f"Title: {title}")
else:
    print("Failed to retrieve data")
