import requests
import json
import time
# 定义URL
#url = "https://weibo.com/ajax/statuses/searchProfile?uid=1669134634&page=10&q=%E6%A8%A1%E6%8B%9F%E9%A2%98&hasori=1&hastext=1&haspic=1&hasvideo=1&hasmusic=1&hasret=1&endtime=1728316800"


mblogids = []
for i in range(20):
	url = "https://weibo.com/ajax/statuses/searchProfile?uid=1669134634&page="
	a="&q=%E6%A8%A1%E6%8B%9F%E9%A2%98&hasori=1&hastext=1&haspic=1&hasvideo=1&hasmusic=1&hasret=1&endtime=1728316800"
	url=url+str(i)+a
	cookies = {'A': '1','B': '2'}
	# 发送GET请求
	response = requests.get(url, cookies=cookies)

	#print(response.text)
	# 检查响应状态码
	if response.status_code == 200:
	    # 将响应内容解析为JSON
		data = response.json()
	    #print(data)
	    # 提取所有mblogid
	    
		if 'data' in data and 'list' in data['data']:
	    		for status in data['data']['list']:
		    		if 'mblogid' in status:
		        		mblogids.append(status['mblogid'])
		
	else:
		print("Failed to retrieve data, status code:", response.status_code)
#print(mblogids)


# 打印所有mblogid
for mblogid in mblogids:
	url1 = 'https://weibo.com/ajax/statuses/longtext?id='
# 请求参数
	url1=url1+mblogid
# 发送GET请求
	response1 = requests.get(url1,cookies=cookies)
	if response1.status_code == 200:
# 解析JSON响应
		data1 = response1.json()
# 获取longTextContent的内容
		long_text_content = data1.get('data', {}).get('longTextContent', '')
		print(long_text_content)
		time.sleep(1)
	else:
		print('请求失败，状态码：', response.status_code)
