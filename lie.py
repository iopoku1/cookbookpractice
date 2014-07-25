a = """Wash, peel and pound the ripe plantains in a mortar until free from lumps. 
Put into a bowl and add unripe plantain flour, salt, pepper and chopped onions. 
Mix well. 
Wash plantain leaves and wrap in mixture in 4 tablespoonfuls at a time. 
Put into a saucepan, add boiling water and cook for 2 hours. 
Serve hot or cold.
"""

m = a.split("\n")
x = []
for sentence in m:
	x.append(sentence.strip())

for i in range(len(x)):
	if x[i] == '':
		x.remove(x[i])

print x