from math import sqrt

critics = {
	'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, 
	'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
	'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
	'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
	'You, Me and Dupree': 3.5},
	'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
	'Superman Returns': 3.5, 'The Night Listener': 4.0},
	'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
	'The Night Listener': 4.5, 'Superman Returns': 4.0,
	'You, Me and Dupree': 2.5},
	'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
	'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
	'You, Me and Dupree': 2.0},
	'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
	'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
	'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

#lista alternativa de pessoas e seus gostos com bandas
teste = {
	'Karen': {'Blind Guardian': 5.0, 'Metallica': 1.0, 'Black Sabbath': 4.9},
	'Patricio': {'Blind Guardian': 1.2, 'Metallica': 4.7, 'Black Sabbath': 4.3},
	'Filomeno': {'Blind Guardian': 4.5, 'Metallica': 1.1, 'Black Sabbath': 5},
	'Zelao': {'Blind Guardian': 0, 'Metallica': 1.5, 'Black Sabbath': 4.9},
}

def sim_distance(prefs, person1, person2):

	#faz uma lista dos itens em comum
	si = {}

	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1

	#se nao ha itens em comum, retorna 0
	if len(si) == 0: return 0

	#soma as raizes
	sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) 
		for item in prefs[person1] if item in prefs[person2]])

	return 1 / (1 + sqrt(sum_of_squares))


#parametro indica que o rating deve ser maior do que criteria
def get_all(criteria = 0, prefs=critics):
	people = [p for p in prefs]

	res = [(p1, p2, sim_distance(prefs, p1, p2)) 
	for p1 in people 
	for p2 in people 
	if p1 != p2
	and sim_distance(prefs, p1, p2) > criteria]

	return res
