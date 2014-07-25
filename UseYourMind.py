#Take in multi line ingredients string pasted from Google Doc & split into list
def ingredientize(ingredients):
	ingredients_list_init = ingredients.split('\n')
	ingredients_list_final = []
	for item in ingredients_list_init:
		ingredients_list_final.append(item.strip())

	#remove empty strings from final list
	for i in range(len(ingredients_list_final)):
		if ingredients_list_final[i] == '':
			ingredients_list_final.remove(ingredients_list_final[i])
	return ingredients_list_final

#Take in multi line method string pasted from Google Doc & split into list
def methodize(method):
	method_list_init = method.split('\n')
	method_list_final = []
	for item in method_list_init:
		method_list_final.append(item.strip())

	#remove empty strings from final list
	for i in range(len(method_list_final)):
		if method_list_final[i] == '':
			method_list_final.remove(method_list_final[i])

	return method_list_final

#Take in int for number of people food's cooked for & turn it into a string to return
def peoplize(people):
	people_string = ""
	if people == 1:
		people_string = "For %r person" % people
		return people_string
	else:
		people_string = "For %r people" % people
		return people_string

#Take in multi line notes string pasted from Google Doc & split into list
def notify(notes):
	notes_list_init = notes.split('\n')
	notes_list_final = []
	for item in notes_list_init:
		notes_list_final.append(item.strip())

	#remove empty strings from final list
	for i in range(len(notes_list_final)):
		if notes_list_final[i] == '':
			notes_list_final.remove(notes_list_final[i])

	return notes_list_final



class recipe(object):

	def __init__(self, name, category, people, ingredients, method, notes):
		self.name = name
		self.category = category
		self.people = people
		self.ingredients = ingredients
		self.method = method
		self.notes = notes


	def JSONify(self):
		JSONed = '{\n"dish": "%s",\n "category": "%s",\n "people": "%s",\n "ingredients": %s,\n "method": %s,\n "notes":%s\n},\n' % (self.name, self.category, self.people, self.ingredients, self.method, self.notes)
		return JSONed