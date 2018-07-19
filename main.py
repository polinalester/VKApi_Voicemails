import sys, urllib2, sqlite3
uids = sys.argv[1:]

with open('tokens.cfg', 'r') as f: # TODO: make cfg prettier
	access_token = f.read()
aid = 6637896 # TODO: add to cfg?

from voicemails import get_voicemails
vmails = get_voicemails(uids, aid, access_token)

db_vmails = {}
for uid, vmlinks in vmails.iteritems():
	names = []
	for vmlink in vmlinks:
		mp3file = urllib2.urlopen(vmlink)
		name = vmlink.rsplit('/', 1)[1]
		names.append(name)
		name = 'voicemails/' + name
		with open(name,'wb') as f:
			f.write(mp3file.read())
	db_vmails[uid] = ', '.join(names)

conn = sqlite3.connect('voicemails.db3')
c = conn.cursor()

for uid, vmfiles in db_vmails.iteritems():
	if vmfiles:
		c.execute("INSERT INTO voicemails VALUES (" + uid + ", '" + vmfiles + "')")

conn.commit()
conn.close()