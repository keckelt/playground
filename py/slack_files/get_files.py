from slacker import Slacker
import csv
import itertools
import datetime as dt


slack = Slacker('xoxp-your-code-here')

pages = slack.files.list(page=1).body['paging']['pages']

all_the_files = list(itertools.chain(*[slack.files.list(page=i).body['files'] for i in range(1,pages + 1)]))

users = slack.users.list().body['members']
usermap = {}
for u in users:
  usermap[u['id']] = u['name']


# sort by filesize
biggest_first = sorted(all_the_files, key=lambda f: f['size'], reverse=True)
filtered = []

# timestamp to YYYYMMDD
for f in biggest_first:
  f['created'] = dt.datetime.utcfromtimestamp(f['created']).strftime("%Y%m%d")
  f['size [mb]'] = f['size']/1024/1024
  f['username'] = usermap[f['user']]
  filtered.append({your_key: f[your_key] for your_key in ['id', 'created', 'name', 'filetype', 'size [mb]', 'mode', 'title', 'user', 'username', 'channels', 'groups', 'permalink'] })

print(filtered[0])

with open("out.csv", "w") as f:
    wr = csv.DictWriter(f, delimiter=';', fieldnames=list(filtered[0].keys()), extrasaction='ignore')
    wr.writeheader()
    wr.writerows(filtered)