from datetime import datetime

from tornado.http1connection import parse_int

now = datetime.now().replace(microsecond=0)

print('Hello student! you have cloned your first repository.')
print(f'Note this historic moment: {now}.')
print("Congratulations! Now it's time to produce repositories of your own!")
print('ich war in deinem code :)')