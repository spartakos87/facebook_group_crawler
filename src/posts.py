# Scrap all posts from Facebook fun page
import requests

def post(page_id,access_token):
	post_list = []
	base = 'https://graph.facebook.com/v2.8/'
	page_id =str(page_id)
	fields ='?fields=posts.limit(1)&'
	access = 'access_token='+str(access_token)
	url = base + page_id + fields + access
	data = requests.get(url).json()
	try:
		print(data['error'])
	except:
		pass
	try:
		post_list.append(data['posts']['data'][0])
	except:
		print(data)
	try:
		print(post_list[-1]['message'])
	except:
		pass
	next = data['posts']['paging'].get('next',None)
	if next != None:
		temp = 1
	else:
		temp = 0
	while temp != 0:
#		try:
			data = requests.get(next).json()
			next = data.get('paging',None)
			if next != None:
				next =data['paging'].get('next',None)
				if next != None:
					temp = 1
				else:
					temp = 0
			else:
				temp = 0
			if len(data['data']) > 0:
				post_list.append(data['data'][0])
#				print(post_list[-1].keys())
				try:
					# message or story
					print(post_list[-1]['message'])
				except:
					pass
#		except:
#			temp = 0
	return post_list
