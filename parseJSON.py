import json

with open('new_dumps.txt') as f:
    data = f.read()

new = eval(data)


parsed_json = json.dumps(new)

#print parsed_json
"""json_file = open('new_dumps.txt')
data = json.load(json_file)
do = data['dataObjects'][0]
print do['identifier']
print do['description']
json_file.close()"""


print(new['textOriginal'])

#print(parse[0][0])

""" for key, value in new.items():
    print "%s key has the value %s " % (key, value) """

"""for key, value in new:
	if key == 'etag':
		print key, value"""