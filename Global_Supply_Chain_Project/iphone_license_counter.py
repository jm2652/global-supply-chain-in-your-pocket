import re

collection = []
licenses = []

def license_count():
	prevBlank = False
	doubleBlank = False

	### Use the double blank line break to identify components
	for line in f.readlines():
		if line == '\n' and prevBlank == False:
			prevBlank = True
# 			print("Blank line")
			continue  

		if line == '\n' and prevBlank == True:
			doubleBlank = True
# 			print("Double blank line")            
			continue    

		if line != '\n' and doubleBlank == True:
			collection.append(line)
		
		else:
			prevBlank = False         # Is this
			doubleBlank = False	      # necessary?
		prevBlank = False
		doubleBlank = False
# 		print("End of line")        
	
	### Split up the lines with multiple projects
	# groupregex = re.compile(r')
	# mo = groupregex.search('My number is 415-555-4242.')
	for line in collection:
		if ',' not in line:
			licenses.append(line)            
		elif ". Inc" in line:
			fixed = line.replace(', et al', ' et al')
			licenses.append(fixed)
			continue
		elif " et. al" in line:
			fixed = line.replace(', Inc.', ' Inc.')
			licenses.append(fixed)
			continue
		elif ',' in line:
			splits = line.split(',')
			list(splits)
			for component in splits:
				licenses.append(component)
			print("Splits:\n", splits)

	print("Licenses:\n",licenses)

readfile = 'apple-iphone-full-legal-notes.txt'
with open(readfile, 'r') as f:
	license_count()

print("Number of licenses:", len(licenses))
####Exceptions: "et al.", "Inc."



license_list = open('license_list.txt', 'w')
for line in licenses:
	license_list.write(line)

# github_file = open('github_file.txt', 'w')
# for github in github_list:
# 	github_file.write(github)