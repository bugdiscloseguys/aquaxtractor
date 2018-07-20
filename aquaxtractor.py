import re , pyperclip , os
from random import randint
print('Usage: Just copy the host file text by ctrl + A and run this script.')
sitename = input('Please let me know the name of the site you scanned for: \n')
ip = re.compile(r'''
(
(\d+)
\.
(\d+)
\.
(\d+)
\.
\d\d
)
''',re.VERBOSE)
copy = pyperclip.paste()
results = ip.findall(copy)
finalresults = []
for i in results:
    finalresults.append(i[0])
random_file = randint(0,9)
txt = sitename
ext = ('.txt')
file = txt + str(random_file) + ext
current = os.getcwd()
print('File have been save on ' + os.path.join(current,file))
save = open(file , 'w')
save.write(str(finalresults))
save.close()
