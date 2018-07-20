import sys, urllib2, sqlite3, os, configparser
uids = sys.argv[1:]

config = configparser.ConfigParser()
config.read('config/conf.ini')
access_token = config['User']['AccessToken']
aid = config['User']['AppID']

from voicemails import get_voicemails
vmails = get_voicemails(uids, aid, access_token)

if not os.path.exists('voicemails'):
    os.makedirs('voicemails')

db_vmails = {}
for uid, vmlinks in vmails.iteritems():
	if not os.path.exists('voicemails/' + uid):
		os.makedirs('voicemails/' + uid)
	names = []
	for vmlink in vmlinks:
		mp3file = urllib2.urlopen(vmlink)
		name = vmlink.rsplit('/', 1)[1]
		names.append(name)
		name = 'voicemails/' + uid + '/' + name
		with open(name,'wb') as f:
			f.write(mp3file.read())
	db_vmails[uid] = ', '.join(names)

conn = sqlite3.connect('voicemails.db3')
c = conn.cursor()

for uid, vmfiles in db_vmails.iteritems():
	if vmfiles:
		c.execute("SELECT uid FROM voicemails WHERE uid = " + uid + " LIMIT 1")
		row=c.fetchone()
		if row is None:
			c.execute("INSERT INTO voicemails VALUES (" + uid + ", '" + vmfiles + "')")
		else:
			c.execute("UPDATE voicemails SET vmfiles = '" + vmfiles + "' WHERE uid =" + uid)

conn.commit()
conn.close()
