#Format testing as to not have to work on the list of 400

mons = [
    bulbasaur:= {
		"num": 1,
		"name": "Bulbasaur",
		"types": ["Grass", "Poison"],
		"genderRatio": {"M": 0.875, "F": 0.125},
		"baseStats": {"hp": 45, "atk": 49, "def": 49, "spa": 65, "spd": 65, "spe": 45},
		"abilities": {"0": "Overgrow", "H": "Chlorophyll"},
		"heightm": 0.7,
		"weightkg": 6.9,
		"color": "Green",
		"evos": ["Ivysaur"],
		"eggGroups": ["Monster", "Grass"]
},
ivysaur:= {
		"num": 2,
		"name": "Ivysaur",
		"types": ["Grass", "Poison"],
		"genderRatio": {"M": 0.875, "F": 0.125},
		"baseStats": {"hp": 60, "atk": 62, "def": 63, "spa": 80, "spd": 80, "spe": 60},
		"abilities": {"0": "Overgrow", "H": "Chlorophyll"},
		"heightm": 1,
		"weightkg": 13,
		"color": "Green",
		"prevo": "Bulbasaur",
		"evolevel": 16,
		"evos": ["Venusaur"],
		"eggGroups": ["Monster", "Grass"],
	}]
# bulbasaur = {
# 		"num": 1,
# 		"name": "Bulbasaur",
# 		"types": ["Grass", "Poison"],
# 		"genderRatio": {"M": 0.875, "F": 0.125},
# 		"baseStats": {"hp": 45, "atk": 49, "def": 49, "spa": 65, "spd": 65, "spe": 45},
# 		"abilities": {"0": "Overgrow", "H": "Chlorophyll"},
# 		"heightm": 0.7,
# 		"weightkg": 6.9,
# 		"color": "Green",
# 		"evos": ["Ivysaur"],
# 		"eggGroups": ["Monster", "Grass"]
# }
# ivysaur:= {
# 		"num": 2,
# 		"name": "Ivysaur",
# 		"types": ["Grass", "Poison"],
# 		"genderRatio": {"M": 0.875, "F": 0.125},
# 		"baseStats": {"hp": 60, "atk": 62, "def": 63, "spa": 80, "spd": 80, "spe": 60},
# 		"abilities": {"0": "Overgrow", "H": "Chlorophyll"},
# 		"heightm": 1,
# 		"weightkg": 13,
# 		"color": "Green",
# 		"prevo": "Bulbasaur",
# 		"evolevel": 16,
# 		"evos": ["Venusaur"],
# 		"eggGroups": ["Monster", "Grass"],
# 	}

mons2 = [test:="1",test2:="2"]
# print(bulbasaur['baseStats']['hp'])
print(mons[0]['baseStats']['hp'])