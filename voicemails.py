def get_voicemails(uids, aid, access_token, count=200):
	
	import requests, time

	vmails = {}
	for uid in uids:
		offset = 0
		if uid not in vmails:
			vmails[uid] = []
		more_messages = True
		while more_messages:
			req_params = {'user_id' : str(uid), #add date
			'count' : str(count), 
			'offset' : str(offset), 
			'v' : str(5.52), 
			'access_token' : access_token}
			req = 'https://api.vk.com/method/messages.getHistory'
			time.sleep(0.4)
			response = requests.get(req, params = req_params)

			if not (len(response.json()['response']['items'])):
				more_messages = False
			else:
				items = response.json()['response']['items']
				mid = items[-1]['id']
				for msg in items:
					if 'attachments' in msg:
						for msg_att in msg['attachments']:
							if ('doc' in msg_att and 'preview' in msg_att['doc'] and 'audio_msg' in msg_att['doc']['preview']):
								vmails[uid].append(msg_att['doc']['preview']['audio_msg']['link_mp3'])
				offset = offset + count

	return vmails