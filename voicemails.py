def get_voicemails(uids, aid, access_token):
	
	import requests

	vmails = {}
	for uid in uids:
		if uid not in vmails:
			vmails[uid] = []
		req = 'https://api.vk.com/method/messages.getHistory?user_id=' + str(uid) + '&count=200&v=5.52&access_token=' + access_token # TODO: increase max count
		response = requests.get(req)
		items = response.json()['response']['items']
		for msg in items:
			if 'attachments' in msg:
				for msg_att in msg['attachments']:
					if ('doc' in msg_att and 'preview' in msg_att['doc'] and 'audio_msg' in msg_att['doc']['preview']):
						vmails[uid].append(msg_att['doc']['preview']['audio_msg']['link_mp3'])
	return vmails