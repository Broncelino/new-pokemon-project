import json
import pickle

class Move:
    #Class that makes the moves for each pokemon
    def __init__(move, name, power, type, accuracy, attack_type, priority,  _self, _opp, _recoil, target):
        move.power = power
        move.type = type
        move.acc = accuracy
        move.attack = attack_type
        move.name = name
        move.priority = priority
        move.self = _self
        move.opp = _opp
        move.recoil = _recoil
        move.target = target
        move.all = [name, power, type, accuracy, attack_type, priority,  _self, _opp, _recoil, target]

        #pp


with open("move.json", mode="r", encoding="utf-8") as read_file:
    move_data = json.load(read_file)
# with open("movesets.json", mode="r", encoding="utf-8") as read_file:
#      moveset_data = json.load(read_file)

# print(type(data))
moves_class = {}
for move in move_data:
    moves_class[move] = Move(move_data[move][0], move_data[move][1],move_data[move][2],move_data[move][3],move_data[move][4],move_data[move][7],move_data[move][5],move_data[move][6],move_data[move][8],move_data[move][9])

# print(type(moveset_data))

with open('move_data.pickle', 'wb') as file: #pickle, unlike json, can store python class objects by default
	pickle.dump(moves_class,file)
     
# with open('movesets_data.pickle', 'wb') as file:
# 	pickle.dump(moveset_data,file)
     