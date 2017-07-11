def group(posts,n):
	t = 0
	temp_l = []
	re_l = []
	for i in posts:
		if t < n :
			temp_l.append(i)
		else:
			re_l.append(temp_l)
			temp_l = []
			temp_l.append(i)
			t = 0	
		t += 1
	if len(temp_l) > 0:
		re_l.append(temp_l)
	return re_l
 
