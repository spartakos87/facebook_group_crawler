import requests

def comm(status_id, access_token,limit):
	base = 'https://graph.facebook.com/v2.8/'
	node = str(status_id)
	fields = '?fields=comments.limit('+str(limit)+'){like_count%2Cmessage%2Cfrom%2Ccomment_count%2Ccreated_time}&'
	#limit = 'limit('+str(limit)+')'
	par = 'access_token=' + str(access_token)
	url = base + node + fields + par
	return requests.get(url).json()

def comments(status_id,access_token,limit):
	big_list = []
	data = comm(status_id,access_token,limit)
#	print(type(data))
#	print(data)
#	print(data.keys())
	try:
		big_list.append(data['comments']['data'][0])
		big_list[-1]['comments'] = comments_of_comment(big_list[-1]['id'],access_token)
		next = data['comments']['paging'].get('next',None)
		if next != None: 
			temp =1
		else:
			temp = 0
		while temp != 0:
			#url = data['comments']['paging']['next']
			#print(url)
			data = requests.get(next).json()
			next = data.get('paging',None)
			if next != None:
				next =data['paging'].get('next',None)
				if next != None:
					temp = 1
				else:
					temp =0
			else:
				temp = 0
			if data.get('data',None) != None:
				if len(data['data'] ) > 0:
					big_list.append(data['data'][0])
					big_list[-1]['comments'] = comments_of_comment(big_list[-1]['id'],access_token)
#				print(big_list[-1])
	except:
		pass
	return big_list
def comments_of_comment(c_id,access_token):
	comm_lst =[]
	base ='https://graph.facebook.com/v2.8/'
	node = str(c_id)
	fields ='?fields=comments,likes.limit(1)&'
	token = 'access_token='+str(access_token)
	url =base+node+fields+token
	data = requests.get(url).json()
	try:
		comm_lst.append(data['comments']['data'][0])
		next = data['comments']['paging'].get('next',None)
		if next != None:
			temp = 1
		else:
			temp = 0
		while temp != 0:
#			data = requests.get(url).json()
#			print(data.keys())
#			comm_lst.append(data['data'][0])
#			url = data['paging'].get('next',None)
			data = requests.get(next).json()
			next = data.get('paging',None)
			if next != None:
				next = data['paging'].get('next',None)
#				comm_lst.append(data['data'][0])
				if next != None:
					temp = 1
				else:
					temp = 0	
#				comm_lst.append(data['data'][0])
			else:
				temp = 0
			if len(data['data']) > 0:
				comm_lst.append(data['data'][0])
		return comm_lst
	except:
		pass
