import json
import requests
def react(status_id, access_token):

    # See http://stackoverflow.com/a/37239851 for Reactions parameters
        # Reactions are only accessable at a single-post endpoint

    base = "https://graph.facebook.com/v2.6"
    node = "/%s" % status_id
    reactions = "/?fields=" \
            "reactions.type(LIKE).limit(0).summary(total_count).as(like)" \
            ",reactions.type(LOVE).limit(0).summary(total_count).as(love)" \
            ",reactions.type(WOW).limit(0).summary(total_count).as(wow)" \
            ",reactions.type(HAHA).limit(0).summary(total_count).as(haha)" \
            ",reactions.type(SAD).limit(0).summary(total_count).as(sad)" \
            ",reactions.type(ANGRY).limit(0).summary(total_count).as(angry)"
    parameters = "&access_token=%s" % access_token
    url = base + node + reactions + parameters

    # retrieve data
    data = json.loads(requests.get(url).text)

    return data

def share(status_id,access_token):
	base = "https://graph.facebook.com/v2.8"
	node = "/%s" % status_id
	shr = "?fields=shares"
	parameters = "&access_token=%s" % access_token
	url = base + node + shr + parameters
	data = json.loads(requests.get(url).text)
	return data

def statistics(status_id,access_token):
	r = react(status_id,access_token)
	s = share(status_id,access_token)
	list_statics = []
	for i in r:
		if i != 'id':
			d = {}
#			print(r[i])
			try:
				d[i] = r[i]['summary']['total_count']
				list_statics.append(d)
			except:
				pass
#	print(s.keys())i
	if len(s.keys()) > 1:
		d = {}
		d['shares'] = s['shares']['count']
		list_statics.append(d)
	else:
		d ={}
		d['shares'] = 0
		list_statics.append(d)
	return list_statics

