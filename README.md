# VKApi_Voicemails

# Info:

Downloads all recent voicemails from VK sent by selected users.

## How to use:

1. Get your **access token** for **messages** (scope = messages):

https://vk.com/dev/first_guide?f=3.%20User%20authorization

Replace access token in **config/conf.ini** with your access token.

2. Run:

```
python db.py
python main.py [uid1] [uid2] ... [uidN]
```
where uid1, uid2, ..., uidN are user ids.

Database **voicemails.db3** stores filenames of voice messages in **'voicemails'** table:

| uid      | list of mp3filenames         |
| -------- |:----------------------------:|
| uid1     | vm_name11, ..., vm_name1M    |
| ...      | ...                          |
| uidN     | vm_nameN1, ..., vm_nameNK    |

All voice message files (mp3) are stored in **'voicemails/{UID}'** folder.
