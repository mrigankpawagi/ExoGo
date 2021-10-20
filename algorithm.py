import json

checks = [
	'PlanetaryMassJpt',
	'RadiusJpt',
	'PeriodDays',
	'SemiMajorAxisAU',
	'Eccentricity',
	'PeriastronDeg',
	'LongitudeDeg',
	'AscendingNodeDeg',
	'InclinationDeg',
	'SurfaceTempK',
	'AgeGyr',
	# 'RightAscension',
	# 'Declination',
	'HostStarMassSlrMass',
	'HostStarRadiusSlrRad',
	'HostStarMetallicity',
	'HostStarTempK',
	'HostStarAgeGyr'
]
Earth = {
	"PlanetaryMassJpt": 0.00315,
	"RadiusJpt": 0.0911301511922301,
	"PeriodDays": 365,
	"SemiMajorAxisAU": 1.00000102,
	"Eccentricity": 0.0167086,
	"PeriastronDeg": 102.93005885,
	"LongitudeDeg": 100.46691572,
	"AscendingNodeDeg": -11.26064,
	"InclinationDeg": -0.00054346,
	"SurfaceTempK": 288,
	"AgeGyr": 4.543,
	# "RightAscension": ,
	# "Declination": ,
	"HostStarMassSlrMass": 1,
	"HostStarRadiusSlrRad": 1,
	"HostStarMetallicity": 0.0122,
	"HostStarTempK": 5778,
	"HostStarAgeGyr": 4.603
}
Mars = {
	"PlanetaryMassJpt": 0.00034,
	"RadiusJpt": 0.048483071333552,
	"PeriodDays": 687,
	"SemiMajorAxisAU": 1.523679,
	"Eccentricity": 0.0934,
	"PeriastronDeg": -23.91744784,
	"LongitudeDeg": -4.56813164,
	"AscendingNodeDeg": 49.558,
	"InclinationDeg": 1.85181869,
	"SurfaceTempK": 210,
	"AgeGyr": 4.603,
	# RightAscension: ,
	# Declination: ,
	"HostStarMassSlrMass": 1,
	"HostStarRadiusSlrRad": 1,
	"HostStarMetallicity": 0.0122,
	"HostStarTempK": 5778,
	"HostStarAgeGyr": 4.603
}
solar = [
	'Mercury',
	'Venus',
	'Earth',
	'Mars',
	'Jupiter',
	'Saturn',
	'Uranus',
	'Neptune',
	'Pluto'
]
def avg(prop):
	return (Earth[prop] + Mars[prop]) / 2

f = open("db.json", "r+")

planets = json.load(f)
f.seek(0)
planets_temp = json.load(f)

for i in range(len(checks)):
	sortVal = [] 
	sortIndex = [] 
	sortValFinal = [] 
	sortIndexFinal = [] 
	sortValEND = [] 
	sortIndexEND = []
	for x in range(len(planets)):        
		if planets[x][checks[i]] != '':
			planets[x][checks[i] + '_difference'] = abs(avg(checks[i]) - float(planets[x][checks[i]]))
			if len(sortVal) == 0:
				sortVal.append(planets[x][checks[i] + '_difference'])
				sortIndex.append(x)	
			else:
				for a in range(len(sortVal)):
					if planets[x][checks[i] + '_difference'] < sortVal[a]:
						sortVal.insert(a, planets[x][checks[i] + '_difference'])
						sortIndex.insert(a, x)
						break			
					if a == len(sortVal) - 1:
						sortVal.append(planets[x][checks[i] + '_difference'])
						sortIndex.append(x)
						break		
		else:
			planets[x][checks[i] + '_difference'] = float('inf')
			sortValEND.append(planets[x][checks[i] + '_difference'])
			sortIndexEND.append(x)

		sortValFinal = sortVal + sortValEND
		sortIndexFinal = sortIndex + sortIndexEND
		
	for m in range(len(sortIndexFinal)):
		if planets[sortIndexFinal[m]][checks[i]] == '':
			planets[sortIndexFinal[m]][checks[i] + '_rank'] = len(sortIndexFinal) - 1
			continue
		planets[sortIndexFinal[m]][checks[i] + '_rank'] = m
overallSort = []
overallSortVals = []
for p in range(len(planets)):
	score = 0
	for q in range(len(checks)):
		score += planets[p][checks[q] + '_rank']
	planets[p]['overallScore'] = score
	if len(overallSortVals) == 0:
		overallSortVals.append(score)
		overallSort.append(p)
	else:
		for r in range(len(overallSortVals)):
			if score < overallSortVals[r]:
				overallSortVals.insert(r, score)
				overallSort.insert(r, p)
				break				
			if r == len(overallSortVals) - 1:
				overallSortVals.append(score)
				overallSort.append(p)
				break
scores = dict()
for w in range(len(overallSort)):
	if planets[overallSort[w]]['PlanetIdentifier'] in solar:
		continue
	scores[planets[overallSort[w]]['PlanetIdentifier']] = planets[overallSort[w]]['overallScore']

for i, e in enumerate(planets_temp):
	if planets_temp[i]['PlanetIdentifier'] in solar:
		del planets_temp[i]
		continue
	planets_temp[i]['score'] = scores[planets_temp[i]['PlanetIdentifier']]

f.seek(0)
json.dump(planets_temp, f)
f.close()