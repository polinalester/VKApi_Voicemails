# VKApi_Voicemails

# Info:

Downloads all recent voicemails from VK sent by selected users.

## How to use:

1. Get your **access token** for **messages** (scope = messages):

https://vk.com/dev/first_guide?f=3.%20User%20authorization

Replace acces token in **tokens.cgf** with *your* access token.

2. Create additional subdirectory **voicemails**.

3. Run:

```
python main.py [uid1] [uid2] ... [uidN]
```
where uid1, uid2, ..., uidN are user ids.

Database **voicemails.db3** stores voice messages' names in **'voicemails'** table:

| uid      | list voicemail files' names  |
| -------- |:----------------------------:|
| uid1     | vm_name11, ..., vm_name1M    |
| ...      | ...                          |
| uidN     | vm_nameN1, ..., vm_nameNK    |

All voice messages files (mp3) are stored in **'voicemails'** folder.
