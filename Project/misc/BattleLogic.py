import pickle
import random
import math

class Pokemon:
    #class that makes the pokemon with their stats typing and moves
  def __init__(mon, name, type1, type2, health, atk, defence, spatk, spdef, spd, learnset):
    #'mon' is an abreviation of Pokemon
    mon.type = type1, type2
    mon.type1 = type1
    mon.type2 = type2
    mon.name = name
    mon.hp = health
    mon.atk = atk
    mon.defence = defence
    mon.spatk = spatk
    mon.spdef = spdef
    mon.spd = spd
    mon.learn = learnset
    # mon.display_name = name
    mon.all = name, type1, type2, health, atk, defence, spatk, spdef, spd


class Pokemon2:
   
   def __init__(mon, pokemon, moves, stat_changes = {'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'acc':6,'eva':6}, status = None):
      mon.moves = moves
      mon.poke = pokemon
      mon.name = pokemon.name
      mon.move_names = [moves[0].name,moves[1].name,moves[2].name,moves[3].name]
      mon.changes = stat_changes #[atk, def, spatk, spdef, spd, acc, eve]
      mon.status = status
class Move:
    #Class that makes the moves for each pokemon
    def __init__(move, name, power, type, accuracy, attack_type, priority,  _self, _opp, _recoil, target):
        move.power = power
        move.type = type
        move.acc = accuracy
        move.attack = attack_type
        move.name = name
        move.priority = priority
        move.self = _self #status for status moves
        move.opp = _opp #boosts for status moves
        move.recoil = _recoil
        move.target = target
        move.all = [name, power, type, accuracy, attack_type, priority,  _self, _opp, _recoil, target]
        #pp

with open('pokemon_data.pickle', 'rb') as file:
    pokemon_data = pickle.load(file)
with open('move_data.pickle', 'rb') as file:
    move_data = pickle.load(file)

# print(pokemon_data['Bulbasaur'])

# print(move_data)

def main():
   stat_table = [.25, .28, .33, .40, .5, .66, 1, 1.5, 2, 2.5, 3, 3.5, 4]
   team1 = [Pokemon2(pokemon_data['kyogre'], [move_data['waterspout'],move_data['tackle'],move_data['tackle'],move_data['doubleedge']]),
             Pokemon2(pokemon_data['groudon'], [move_data['quickattack'],move_data['tackle'],move_data['tackle'],move_data['doubleedge']])]
   team2 = [Pokemon2(pokemon_data['arceus'], [move_data['leafstorm'],move_data['tackle'],move_data['tackle'],move_data['doubleedge']]),
             Pokemon2(pokemon_data['wooper'], [move_data['rocksmash'],move_data['tackle'],move_data['tackle'],move_data['doubleedge']])]
   # team1, team2 = move_select(pokemon_select()), move_select(pokemon_select())
   p1,p2 = choose_mon(team1), choose_mon(team2)
   print('Player1:',p1.name,'\nPlayer2:',p2.name)
   while len(team1) > 0 and len(team2) > 0: #game loops until one of the teams is out of pokemon
      p1par = 1
      p2par = 1 #will be multiplied by each mon's speed
      if p1.status == 'par': 
         p1par = .25 #speed is 25% while paralyzed
      if p2.status == 'par':
         p2par = .25
      print('Player1 choose your action:')
      p1choice =int(input('0. Switch \n1.Moves'))
      if p1choice == 0:
         print('switch p1')
      if p1choice == 1:
         p1choice = move_choice(p1)
      print('Player2 choose your action:')
      p2choice =int(input('0. Switch \n1.Moves'))
      if p2choice == 0:
         print('switch p2')
      if p2choice == 1:
         p2choice = move_choice(p2)
      if p1choice !=0 and p2choice !=0:
         if p1choice.priority == p2choice.priority:
            if p1.poke.spd*p1par*stat_table[p1.changes['spe']] > p2.poke.spd*p2par*stat_table[p2.changes['spe']]:
               damage, stat = damage_calc(p1choice, p1,p2)
               p2.poke.hp = new_health(damage, p2)
               dead = check_dead(team2,p2)
               if dead == True:
                  print('Player 1 Wins')
                  break
               if dead != None:
                  p2 = dead
               if p1choice.recoil != 0:
                  recoil = damage*(p1choice.recoil[0]/p1choice.recoil[1])
                  print("{p1.name} took recoil")
                  p1.poke.hp = new_health(recoil, p1)
                  dead = check_dead(team1,p1)
                  if dead == True:
                     print('Player 2 Wins')
                     break
                  if dead != None:
                     p1 = dead
               damage, stat = damage_calc(p2choice, p2,p1)
               p1.poke.hp = new_health(damage, p1)
               dead = check_dead(team1,p1)
               if dead == True:
                  print('Player 2 Wins')
                  break
               if dead != None:
                  p1 = dead
               if p2choice.recoil != 0:
                  recoil = damage*(p2choice.recoil[0]/p2choice.recoil[1])
                  print("{p2.name} took recoil")
                  p2.poke.hp = new_health(recoil, p2)
                  dead = check_dead(team2,p2)
                  if dead == True:
                     print('Player 1 Wins')
                     break
                  if dead != None:
                     p2 = dead

            elif p1.poke.spd*p1par*stat_table[p1.changes['spe']] < p2.poke.spd*p2par*stat_table[p2.changes['spe']]:
               print('4th if')
               damage, stat = damage_calc(p2choice, p2,p1)
               p1.poke.hp = new_health(damage, p1)
               dead = check_dead(team1,p1)
               if dead == True:
                  print('Player 2 Wins')
                  break
               if dead != None:
                  p1 = dead
               if p2choice.recoil != None:
                  recoil = damage*(p2choice.recoil[0]/p2choice.recoil[1])
                  print("{p2.name} took recoil")
                  p2.poke.hp = new_health(recoil, p2)
                  dead = check_dead(team2,p2)#check p2 dead
                  if dead == True:
                     print('Player 1 Wins')
                     break
                  if dead != None:
                     p2 = dead
               damage, stat = damage_calc(p1choice, p1,p2)
               p2.poke.hp = new_health(damage, p2)
               dead = check_dead(team2,p2)
               if dead == True:
                  print('Player 1 Wins')
                  break
               if dead != None:
                  p2 = dead
               if p1choice.recoil != None:
                  recoil = damage*(p1choice.recoil[0]/p1choice.recoil[1])
                  print("{p1.name} took recoil")
                  p1.poke.hp = new_health(recoil, p1)
                  dead = check_dead(team1,p1)
                  if dead == True:
                     print('Player 2 Wins')
                     break
                  if dead != None:
                     p1 = dead
   print("game over")
      


# print(move_data['dracometeor'].self)

# print(bulbasaur.moves[0].type)


# with open('test1.pickle', 'wb') as file: #pickle, unlike json, can store python class objects by default
# 	pickle.dump(bulbasaur,file)

def resolve_attacking_turn(firstmon, firstmove, firstteam, secondmon, secondmove, secondteam):
   damage, stat = damage_calc(firstmove, firstmon,secondmon)
   secondmon.poke.hp = new_health(damage, secondmon)
   dead = check_dead(secondteam, secondmon)
   if dead == True:
      print('first Wins')
      return 'first wins'
   if dead != None:
      secondmon = dead
   if firstmove.recoil != 0:
      recoil = damage*(firstmove.recoil[0]/firstmove.recoil[1])
      print("{firstmon.name} took recoil")
      firstmon.poke.hp = new_health(recoil, firstmon)
      recdead = check_dead(firstteam,firstmon)
      if recdead == True:
         print('second Wins')
         return 'secondmon wins'
      if recdead != None:
         firstmon = dead
   damage, stat = damage_calc(secondmove, secondmon,firstmon)
   firstmon.poke.hp = new_health(damage, firstmon)
   dead = check_dead(firstteam,firstmon)
   if dead == True:
      print('second Wins')
      return 'secondmon wins'
   if dead != None:
      firstmon = dead
   if secondmove.recoil != 0:
      recoil = damage*(secondmove.recoil[0]/secondmove.recoil[1])
      print("{secondmon.name} took recoil")
      secondmon.poke.hp = new_health(recoil, secondmon)
      dead = check_dead(secondteam,secondmon)
      if dead == True:
         print('Player 1 Wins')
         return 'p1 wins'
      if dead != None:
         secondmon = dead



def check_dead(team, mon):
   if mon.poke.hp == 0:
      print(len(team))
      team.remove(mon)
      print(len(team))
      if len(team) == 0:
         return True
      else:
         return choose_mon(team)
   else: 
      return None

def pokemon_select(): #function to pick a pokemon then their moves. will be repeated 6 times per player
   pkm_team = []
   pkm_team_names = []
   while len(pkm_team) < 2:
      print("Current team:", pkm_team_names)
      choice = input('Type the pokemon you want: ').lower()
      try:
         mon = pokemon_data[choice]
         if mon in pkm_team:
            print('no duplicates try again')
         else:
            pkm_team.append(mon)
            pkm_team_names.append(mon.name)
      except:
         print('try again')
   return([pkm_team,pkm_team_names])
# pokemon_select(pkm_team1)


# while len(pkm_team1) < 6: #teams consist of 6 pokemon
#    pokemon_select(pkm_team1)

def choose_mon(team):
   for x in range(0,len(team)):
      print("{0}. {1}".format(x, team[x].name))
   p1 = int(input("choose your Pokemon number: "))
   return(team[p1])

def move_choice(p):
   for x in range(0,len(p.moves)):
      print("{0}. {1}".format(x, p.moves[x].name))
   choice = int(input('Pick your move'))
   return p.moves[x]

test_list = [[pokemon_data['bulbasaur'],pokemon_data['wooper'],pokemon_data['gliscor']], ['bulbasaur','wooper','gliscor']]
# choose_mon(test_list)
def move_select(pkm_list):
   combined = []
   for mon in pkm_list[0]:
      moves = []
      move_names = []
      print(mon.learn)
      while len(moves) < 4:  
         print(mon.name,"current moves:", move_names)
         try:
            move = input("What move do you want to select: ")
            choice = move_data[move]
            if choice in moves:
               print('Only 1 copy of a move is allowed')
            if choice in mon.learn:
               moves.append(choice)
               move_names.append(choice.name)
            else:
               print('Pick a move in the learnset')
         except:
            print('enter a valid move')
      print(move_names)
      pkm_with_moves = Pokemon2(mon, moves)
      combined.append(pkm_with_moves)
   return(combined)

# sample_team = move_select(pokemon_select())

# print(sample_team)
# print(sample_team[0].name,sample_team[0].move_names)

# print('your team:')
# for mon in sample_team:
#    print(mon.name,mon.move_names)


def new_health(damage, recieveing_mon):
    remaining = recieveing_mon.poke.hp-damage
    if remaining<0:
        remaining = 0
    print("{0} has {1} health remaining".format(recieveing_mon.name,remaining))
    return(remaining)

def dodge_chance(move, att_acc, def_eva):
    hit_chance = move.acc
    rand = random.randint(1,100)
    rand = (rand*def_eva)/att_acc
    if rand>hit_chance:
        hit = 0
    else:
        hit = 1
    return(hit)

def effect_chance(move):
   rand = random.randint(1,100)
   if move.opp['chance'] >= rand:
      if 'status' in move.opp.keys():
         if move.opp['status'] == 'brn':
            return('brn')
         elif move.opp['status'] == 'frz':
            return('frz')
         elif move.opp['status'] == 'slp':
            return('slp')
         elif move.opp['status'] == 'par':
            return('par')
         elif move.opp['status'] == 'psn':
            return('psn')
         elif move.oppo['status'] == 'tox':
            return('tox')
      elif 'volatileStatus' in move.opp.keys():
         if move.opp['volatileStatus'] == 'flinch':
            return('flinch')
         elif move.opp['volatileStatus'] == 'confusion':
            return('confusion')
      elif 'boosts' in move.opp.keys() or 'self' in move.opp.keys():
         return('boost')

def apply_effects(move, effect, att_mon, def_mon):
   print('1')
   if effect == 'boost':
      if 'boosts' in move.opp.keys():
         for boost in move.opp['boosts'].keys():
            def_mon.changes[boost] += move.opp['boosts'][boost]
      elif 'self' in move.opp.keys():
         for boost in move.opp['self']['boosts'].keys():
            att_mon.changes[boost] += move.opp['self']['boosts'][boost]
   elif effect in ['brn','par','slp','frz','psn','tox']:
      print('')
      if def_mon.status == None:
         def_mon.status = effect
      # elif 'boosts' in move.self.keys():
      #    for boost in move.self['boosts'].keys():
      #       att_mon.changes[boost] += move.self['boosts'][boost]
      
def self_effect_apply(move, effect, att_mon, def_mon):
   if effect == 'boost':
      for boost in move.self['boosts'].keys():
         att_mon.changes[boost] += move.self['boosts'][boost]

def self_effect(move):
   if 'boosts' in move.self.keys():
      return('boost')

def damage_roll():
    num = random.randint(85,100)
    num = num/100
    return(num)

def critical():
    num = random.randint(1,16)
    
    if num == 16:
        crit = 1.5
    else:
        crit = 1.0
    
    return(crit)
def damage_calc(move, attacking_mon, defending_mon):
   attacking_mon_stats = attacking_mon.poke
   defending_mon_stats = defending_mon.poke
   eva_acc_table = [.33, .36, .43, .50, .60, .75, 1, 1.33, 1.66, 2, 2.5, 2.66, 3]
   stat_table = [.25, .28, .33, .40, .5, .66, 1, 1.5, 2, 2.5, 3, 3.5, 4]
   super_effective_dict = {
   'Normal':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':0.5, 'Ghost':0.0, 'Dragon':1.0, 'Dark':1.0, 'Steel':0.5,'Fairy':1.0},
   'Fire': {'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 2.0, 'Water': 0.5, 'Electric':1.0, 'Ice':2.0, 'Fighting':1.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':2.0, 'Rock':0.5, 'Ghost':1.0, 'Dragon':0.5, 'Dark':1.0, 'Steel':2.0,'Fairy':1.0}, 
   'Water': {'none':1.0,'Normal':1.0, 'Fire': 2.0, 'Grass': 0.5, 'Water': 0.5, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':1.0, 'Ground':2.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':2.0, 'Ghost':1.0, 'Dragon':0.5, 'Dark':1.0, 'Steel':1.0,'Fairy':1.0}, 
   'Grass': {'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 0.5, 'Water': 2.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':0.5, 'Ground':2.0, 'Flying':0.5, 'Psychic':1.0, 'Bug':0.5, 'Rock':2.0, 'Ghost':1.0, 'Dragon':0.5, 'Dark':1.0, 'Steel':0.5,'Fairy':1.0},
   'Electric':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 0.5, 'Water': 2.0, 'Electric':0.5, 'Ice':1.0, 'Fighting':1.0,'Poison':1.0, 'Ground':0.0, 'Flying':2.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':1.0, 'Dragon':0.5, 'Dark':1.0, 'Steel':1.0,'Fairy':1.0},
   'Ice':{'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 2.0, 'Water': 0.5, 'Electric':1.0, 'Ice':0.5, 'Fighting':1.0,'Poison':1.0, 'Ground':2.0, 'Flying':2.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':2.0, 'Ghost':1.0, 'Dragon':2.0, 'Dark':1.0, 'Steel':0.5,'Fairy':1.0},
   'Fighting':{'none':1.0,'Normal':2.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':2.0, 'Fighting':1.0,'Poison':0.5, 'Ground':1.0, 'Flying':0.5, 'Psychic':0.5, 'Bug':0.5, 'Rock':2.0, 'Ghost':0.0, 'Dragon':0.5, 'Dark':2.0, 'Steel':2.0,'Fairy':0.5},
   'Poison':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 2.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':0.5, 'Ground':0.5, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':0.5, 'Ghost':0.5, 'Dragon':1.0, 'Dark':1.0, 'Steel':0.0,'Fairy':2.0},
   'Ground':{'none':1.0,'Normal':1.0, 'Fire': 2.0, 'Grass': 0.5, 'Water': 1.0, 'Electric':2.0, 'Ice':1.0, 'Fighting':1.0,'Poison':2.0, 'Ground':1.0, 'Flying':0.0, 'Psychic':1.0, 'Bug':0.5, 'Rock':2.0, 'Ghost':1.0, 'Dragon':1.0, 'Dark':1.0, 'Steel':2.0,'Fairy':1.0},
   'Flying':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 2.0, 'Water': 1.0, 'Electric':0.5, 'Ice':1.0, 'Fighting':2.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':2.0, 'Rock':0.5, 'Ghost':1.0, 'Dragon':1.0, 'Dark':1.0, 'Steel':0.5,'Fairy':1.0},
   'Psychic':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':2.0,'Poison':2.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':0.5, 'Bug':1.0, 'Rock':1.0, 'Ghost':1.0, 'Dragon':0.5, 'Dark':0.0, 'Steel':0.5,'Fairy':1.0},
   'Bug':{'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 2.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':0.5,'Poison':0.5, 'Ground':1.0, 'Flying':0.5, 'Psychic':2.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':0.5, 'Dragon':1.0, 'Dark':2.0, 'Steel':0.5,'Fairy':0.5},
   'Rock':{'none':1.0,'Normal':1.0, 'Fire': 2.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':2.0, 'Fighting':0.5,'Poison':1.0, 'Ground':0.5, 'Flying':2.0, 'Psychic':1.0, 'Bug':2.0, 'Rock':1.0, 'Ghost':1.0, 'Dragon':1.0, 'Dark':1.0, 'Steel':0.5,'Fairy':1.0},
   'Ghost':{'none':1.0,'Normal':0.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':2.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':2.0, 'Dragon':1.0, 'Dark':0.5, 'Steel':1.0,'Fairy':1.0},
   'Dragon':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':1.0, 'Dragon':2.0, 'Dark':1.0, 'Steel':0.5,'Fairy':0.0},
   'Dark':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':0.5,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':2.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':2.0, 'Dragon':1.0, 'Dark':0.5, 'Steel':1.0,'Fairy':0.5},
   'Steel':{'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 0.5, 'Water': 0.5, 'Electric':1.0, 'Ice':2.0, 'Fighting':1.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':2.0, 'Ghost':1.0, 'Dragon':1.0, 'Dark':1.0, 'Steel':0.5,'Fairy':2.0},
   'Fairy':{'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':2.0,'Poison':0.5, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':1.0, 'Dragon':2.0, 'Dark':2.0, 'Steel':0.5,'Fairy':1.0},}
   effect = None
   burn = 1
   power = move.power
   move_type = move.type
   attack_type = move.attack
   attacking_type1 = attacking_mon_stats.type1
   attacking_type2 = attacking_mon_stats.type2
   defending_type1 = defending_mon_stats.type1
   defending_type2 = defending_mon_stats.type2
   super_effective = super_effective_dict[move.type][defending_type1]*super_effective_dict[move.type][defending_type2] #checks if the move will do extra damage based on type weaknesses
   atk = attacking_mon_stats.atk*stat_table[attacking_mon.changes['atk']]
   spatk = attacking_mon_stats.spatk*stat_table[attacking_mon.changes['spa']]
   defence = defending_mon_stats.defence*stat_table[defending_mon.changes['def']]
   spdef = defending_mon_stats.spdef*stat_table[defending_mon.changes['spd']]
   if move.type == attacking_type1 or move.type == attacking_type2: #if the move type and pokemon type are the same it does 1.5x damage
      stab = 1.5
   else:
      stab = 1
   rand = damage_roll() #random number between .85 and 1
   crit = critical() #1 in 24 chance to deal 1.5x damage
   dodge = dodge_chance(move, eva_acc_table[attacking_mon.changes['acc']], eva_acc_table[defending_mon.changes['eva']])
   if attacking_mon.status == 'brn':
      burn = .5
   if attack_type == "Special":
      damage = (((42*power*(spatk/spdef))/50)+2)*super_effective*stab*crit*rand*dodge #the actual calculation
   else:
      damage = (((42*power*(burn*atk/defence))/50)+2)*super_effective*stab*crit*rand*dodge #the actual calculation. Only atk is changed by burn status
   if dodge == 0:
      print("The attack missed")
   else:
      print("{0} used {1}".format(attacking_mon.name, move.name))
      if crit == 1.5:
         print("Its a Critical Hit! ")
      if super_effective>1:
         print("It's Super Effective")
      elif super_effective <1:
         print("It's Not Very Effective")
      print("It did {0} damage".format(math.trunc(damage)))
      if move.opp != None:
         effect = effect_chance(move)
         apply_effects(move, effect, attacking_mon, defending_mon)
      if move.self != None:
         effect = self_effect(move)
         self_effect_apply(move, effect, attacking_mon, defending_mon)
   return(math.trunc(damage),effect)



main()

# print(mankey.status)
# print(damage_calc(bulbasaur.moves[1], bulbasaur, mankey))
# print(mankey.status)
# # print(damage_calc(bulbasaur.moves[1], bulbasaur, mankey))
# # print(mankey.changes)


# print(move_data['ember'].all)
# # print(move_data['leafstorm'].all)
# print(move_data['ancientpower'].all)



