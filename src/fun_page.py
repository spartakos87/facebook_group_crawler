from comments import comments as c
from react import statistics as s
from posts import post as p
from group import group
import json
from multiprocessing import Pool
import time
from facepy import utils
import credits

def fun_page(page_id,onoma):
	pp= Pool(50)
	mega_list = []
	start = time.time()
	pst = p(page_id,access_token)
	n = 50 
	group_post = group(pst,n)
	temp = 0 
	for j in group_post:
		temp += len(j)
		print(str(temp)+'/'+str(len(pst)))
		re = pp.map(pros,list(j))
		for jj in re:
			mega_list.append(jj)
	duration = (time.time()-start)/float(60)
	print ("Time:"+str(duration)+'min')
	with open(onoma,'w') as f:
		json.dump(mega_list,f)
	return mega_list
def pros(i):
	st = s(i['id'],access_token)
	comm = c(i['id'],access_token,1)
	d = {}
	d['post'] = i
	d['statistics'] = st
	d['comments'] = comm
	return d

"""
check time of last element ff[0]['post']['created_time']
"""


if __name__ == '__main__':
	page_id = input("Give group id: \n")
	global access_token
	app_id =int(input("Give app id: \n"))
	app_secret =("Give app secret: \n") 
	access_token =  utils.get_application_access_token(app_id, app_secret)[0]
	onoma = input("Give name of file to save data: \n")
	fun_page(page_id,onoma)

