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
   
   def __init__(mon, pokemon, moves, max, itm, stat_changes: dict = {'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status = None):
      mon.moves = moves
      mon.poke = pokemon
      mon.name = pokemon.name
      mon.move_names = [moves[0].name,moves[1].name,moves[2].name,moves[3].name]
      mon.changes = stat_changes #[atk, def, spatk, spdef, spd, acc, eve]
      mon.status = status
      mon.max = max
      mon.itm = itm
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
   rematch = True
   while rematch == True:
      stat_table = [.25, .28, .33, .40, .5, .66, 1, 1.5, 2, 2.5, 3, 3.5, 4]
      team1 = [Pokemon2(pokemon_data['rayquaza'], [move_data['extremespeed'],move_data['swordsdance'],move_data['thunderwave'],move_data['earthquake']],pokemon_data['rayquaza'].hp, 'leftovers', stat_changes={'atk':12,'def':6,'spa':6,'spd':6,'spe':12,'accuracy':6,'evasion':6}, status= None),
               Pokemon2(pokemon_data['arceus'], [move_data['extremespeed'],move_data['calmmind'],move_data['blizzard'],move_data['toxic']],pokemon_data['arceus'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status= None),
               Pokemon2(pokemon_data['gliscor'], [move_data['rockpolish'],move_data['poisonjab'],move_data['quickattack'],move_data['steelwing']],pokemon_data['gliscor'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status= None),
               Pokemon2(pokemon_data['garchomp'], [move_data['surf'],move_data['poisonjab'],move_data['fireblast'],move_data['swordsdance']],pokemon_data['garchomp'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status= None),
               Pokemon2(pokemon_data['mew'], [move_data['psychic'],move_data['ancientpower'],move_data['earthpower'],move_data['firepunch']],pokemon_data['mew'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status= None),
               Pokemon2(pokemon_data['giratina'], [move_data['earthquake'],move_data['calmmind'],move_data['aurasphere'],move_data['dragonpulse']],pokemon_data['giratina'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status= None)]
      
      team2 = [Pokemon2(pokemon_data['ninjask'], [move_data['bugbite'],move_data['shadowball'],move_data['toxic'],move_data['swordsdance']],pokemon_data['ninjask'].hp, 'leftovers', stat_changes={'atk':6,'def':0,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status= None),
               Pokemon2(pokemon_data['metagross'], [move_data['bulletpunch'],move_data['agility'],move_data['irondefense'],move_data['psychic']],pokemon_data['metagross'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status= None),
               Pokemon2(pokemon_data['infernape'], [move_data['machpunch'],move_data['closecombat'],move_data['poisonjab'],move_data['toxic']],pokemon_data['infernape'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status= None),
               Pokemon2(pokemon_data['skarmory'], [move_data['toxic'],move_data['irondefense'],move_data['drillpeck'],move_data['steelwing']],pokemon_data['skarmory'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status= None),
               Pokemon2(pokemon_data['groudon'], [move_data['swordsdance'],move_data['earthquake'],move_data['dragonclaw'],move_data['fireblast']],pokemon_data['groudon'].hp, 'leftovers', stat_changes={'atk':6,'def':0,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status= None),
               Pokemon2(pokemon_data['kyogre'], [move_data['hydropump'],move_data['blizzard'],move_data['bodyslam'],move_data['earthquake']],pokemon_data['kyogre'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status= None)]
      # team1, team2 = move_select(pokemon_select()), move_select(pokemon_select())
      p1,p2 = choose_mon(team1), choose_mon(team2)
      print('Player1:',p1.name,'\nPlayer2:',p2.name)
      while len(team1) > 0 and len(team2) > 0: #game loops until one of the teams is out of pokemon note: should never hit this because a break is applied after every death check
         print(p1.changes,p2.changes)
         p1par = 1
         p2par = 1 #will be multiplied by each mon's speed
         if p1.status == 'par': 
            p1par = .25 #speed is 25% while paralyzed
         if p2.status == 'par':
            p2par = .25
         p1starthp = p1.poke.hp
         p2starthp = p2.poke.hp
         # print('Player1 choose your action:')
         p1choice =int(input('\n1. Moves\n2. Switch\nPlayer 1, Pick what you want {0} to do: '.format(p1.name)))
         print('')
         if p1choice == 2:
            print('switch p1')
            p1 = switch(team1,p1)
         if p1choice == 1:
            p1choice = move_choice(p1)
         # print('Player2 choose your action:')
         p2choice =int(input('\n1. Moves\n2. Switch\nPlayer2, Pick what you want {0} to do: '.format(p2.name)))
         print('')
         if p2choice == 2:
            print('switch p2')
            p2 = switch(team2,p2)
         if p2choice == 1:
            p2choice = move_choice(p2)
         if p1choice !=2 and p2choice !=2:
            if p1choice.priority == p2choice.priority:
               if p1.poke.spd*p1par*stat_table[p1.changes['spe']] > p2.poke.spd*p2par*stat_table[p2.changes['spe']]:
                  p1, p1choice, team1,p2,p2choice,team2 = resolve_attacking_turn(p1, p1choice, team1,p2,p2choice,team2)
                  if p2 == 0 or p2 == 1:
                     break 
                  
               elif p1.poke.spd*p1par*stat_table[p1.changes['spe']] < p2.poke.spd*p2par*stat_table[p2.changes['spe']]:
                  p2,p2choice,team2,p1, p1choice, team1 = resolve_attacking_turn(p2,p2choice,team2,p1, p1choice, team1)
                  if p2 == 0 or p2 == 1:
                     break               
               else:
                  if random.randint(1,2) == 1: #if there is a speed and priority tie its a coin flip of who goes first.
                     p1, p1choice, team1,p2,p2choice,team2 = resolve_attacking_turn(p1, p1choice, team1,p2,p2choice,team2)
                     if p1 == 0 or p1 == 1:
                        break
                  else:
                     p2,p2choice,team2,p1, p1choice, team1 = resolve_attacking_turn(p2,p2choice,team2,p1, p1choice, team1)
                     if p2 == 0 or p2 == 1:
                        break
                     
            elif p1choice.priority > p2choice.priority:
               p1, p1choice, team1,p2,p2choice,team2 = resolve_attacking_turn(p1, p1choice, team1,p2,p2choice,team2)
               if p1 == 0 or p1 == 1:
                  break
            elif p1choice.priority < p2choice.priority:
               p2,p2choice,team2,p1, p1choice, team1 = resolve_attacking_turn(p2,p2choice,team2,p1, p1choice, team1)
               if p2 == 0 or p2 == 1:
                  break
         elif p1choice != 2 and p2choice == 2:
            damage, clear= damage_calc(p1choice, p1, p2)
         
            if clear == 1:
               p1.status = None
            if clear == 2:
               p1.status['slp'] += 1
            p2.poke.hp = new_health(damage, p2)
            dead = check_dead(team2, p2)
            if dead != None:
               p2=dead
            if p1choice.recoil != None:
               if damage > p2starthp:
                  damage = p2starthp
               recoil = damage*(p1choice.recoil[0]/p1choice.recoil[1])
               p1.poke.hp = new_health(recoil, p1)
               dead = check_dead(team1, p1)
               if dead == True:
                  print('Player 2 wins')
                  break
               if dead != None:
                  p1=dead
         elif p2choice != 2 and p1choice == 2:
            damage, clear= damage_calc(p2choice, p2, p1)
            print(clear)
            if clear == 1:
               p2.status = None
            if clear == 2:
               p2.status['slp'] += 1
            p1.poke.hp = new_health(damage, p1)
            dead = check_dead(team1, p1)
            if dead != None:
               p1=dead
            if p2choice.recoil != None:
               if p1starthp > damage:
                  damage = p1starthp
               recoil = damage*(p2choice.recoil[0]/p2choice.recoil[1])
               p2.poke.hp = new_health(recoil, p2)
               dead = check_dead(team2, p2)
               if dead == True:
                  print('Player 1 wins')
                  break
               if dead != None:
                  p2=dead
         #end of turn effects for all variations
         p1 = end_of_turn_effects(p1)
         p1lose = check_dead(team1, p1)
         if p1lose == True:
            print('Player 2 wins')
            break
         if p1lose != None:
            p1 = p1lose
         p2 = end_of_turn_effects(p2)
         p2lose = check_dead(team2,p2)
         if p2lose == True:
            print("player 1 wins")
            break
         if p2lose != None:
            p2 = p2lose  
         print(p1.status)
         print(p2.status) 
      print("game over")
      re = input("would you like to play again? (y/n) ")
      if re == 'n':
         rematch = False


# print(move_data['dracometeor'].self)

# print(bulbasaur.moves[0].type)


# with open('test1.pickle', 'wb') as file: #pickle, unlike json, can store python class objects by default
# 	pickle.dump(bulbasaur,file)




def resolve_attacking_turn(firstmon, firstmove, firstteam, secondmon, secondmove, secondteam):
   nosecondturn = False
   firstmaxrec = firstmon.poke.hp
   secmaxrec = secondmon.poke.hp
   print("{0}'s turn:\n".format(firstmon.name))
   damage, clear = damage_calc(firstmove, firstmon,secondmon)
   if clear == 1:
      firstmon.status = None
   if clear == 2:
      firstmon.status['slp'] += 1
   secondmon.poke.hp = new_health(damage, secondmon)
   dead = check_dead(secondteam, secondmon)
   if dead == True:
      print('first Wins')
      return 0,0,0,0,0,0
   if dead != None:
      secondmon = dead
      nosecondturn = True
   if firstmove.recoil != None:
      if damage > secmaxrec:
         damage = secmaxrec
      recoil = math.trunc(damage*(firstmove.recoil[0]/firstmove.recoil[1]))
      print("{0} took recoil".format(firstmon.name))
      firstmon.poke.hp = new_health(recoil, firstmon)
      recdead = check_dead(firstteam,firstmon)
      if recdead == True:
         print('second Wins')
         return 1,1,1,1,1,1
      if recdead != None:
         firstmon = dead
   if nosecondturn != True:
      print("{0}'s turn:\n".format(secondmon.name))
      damage, clear = damage_calc(secondmove, secondmon,firstmon)
      if clear == 1:
         secondmon.status = None
      if clear == 2:
         secondmon.status['slp'] += 1
      firstmon.poke.hp = new_health(damage, firstmon)
      dead = check_dead(firstteam,firstmon)
      if dead == True:
         print('second Wins')
         return 1,1,1,1,1,1
      if dead != None:
         firstmon = dead
      if secondmove.recoil != None:
         if firstmaxrec > damage:
            damage = firstmaxrec
         recoil = math.trunc(damage*(secondmove.recoil[0]/secondmove.recoil[1]))
         print("{0} took recoil".format(secondmon.name))
         secondmon.poke.hp = new_health(recoil, secondmon)
         dead = check_dead(secondteam,secondmon)
         if dead == True:
            print('Player 1 Wins')
            return 0,0,0,0,0,0
         if dead != None:
            secondmon = dead
   return(firstmon, firstmove, firstteam, secondmon, secondmove, secondteam)

def switch(team, mon):
   if len(team) > 1:
      team.remove(mon)
      new = choose_mon(team)
      mon.changes = {'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6} #stat changes get reset when switching out.
      try:
         mon.status['tox'] = 1 #toxic counter gets reset on switch out unlike sleep
         team.append(mon)
         return new
      except:
         team.append(mon)
         return new
   else:
      print('you need another pokemon to switch to')
      return mon



def check_dead(team, mon):
   if mon.poke.hp == 0:
      team.remove(mon)
      if len(team) == 0:
         return True
      else:
         return choose_mon(team)
   else: 
      return None

def pokemon_select(): #function to pick a pokemon then their moves. will be repeated 6 times per player
   pkm_team = []
   pkm_team_names = []
   while len(pkm_team) < 6:
      print("Current team:", pkm_team_names)
      choice = input('Type the pokemon you want up to Gen 4: ').lower()
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
   for x in range(1,len(team)+1):
      print("{0}. {1} {2}hp {3}".format(x, team[x-1].name,team[x-1].poke.hp, team[x-1].status))
   p1 = int(input("choose your Pokemon number: "))
   return(team[p1-1])

def move_choice(p):
   for x in range(1,len(p.moves)+1):
      print("{0}. {1}".format(x, p.moves[x-1].name))
   print('')
   choice = int(input('Pick {0}\'s move: '.format(p.name)))
   print('')
   return p.moves[choice-1]

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
            # print(move)
            # print(choice)
            if choice in moves:
               print('Only 1 copy of a move is allowed')
            if move in mon.learn:
               moves.append(choice)
               move_names.append(choice.name)
            else:
               print('Pick a move in the learnset')
         except:
            print('enter a valid move')
      print(move_names)
      pkm_with_moves = Pokemon2(mon, moves, mon.hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'accuracy':6,'evasion':6}, status=None) #if stat_changes uses the default each class seems to be referencing the same dictionary
      combined.append(pkm_with_moves)
   return(combined)

# sample_team = move_select(pokemon_select())

# print(sample_team)
# print(sample_team[0].name,sample_team[0].move_names)

# print('your team:')
# for mon in sample_team:
#    print(mon.name,mon.move_names)

def end_of_turn_effects(mon):
   # print('end of turn effects')
   if mon.status in ['brn','psn']:
      dam = math.trunc((mon.max*(1/8)))#psn and brn do 1/8 total hp per turn
      print("{0} was hurt by {1} ({2})".format(mon.name,mon.status,dam))
      mon.poke.hp = new_health(dam, mon)
   if type(mon.status) == type({'ex':1}): #checking if it's slp or tox, probably a better way
      if 'tox' in mon.status.keys():
         dam = math.trunc((mon.max*(mon.status['tox']/16))) #tox does increasing damage for every turn the mon is on the field
         mon.status['tox'] += 1 #slp counter ticks when mon attempts attacking where tox ticks when it deals damage
         print("{0} was hurt by tox ({1})".format(mon.name, dam))
         mon.poke.hp = new_health(dam,mon)
   if mon.poke.hp !=0 and mon.poke.hp != mon.max:
      if mon.itm == 'leftovers':
         heal = math.trunc(mon.max/16)
         print("{0}'s leftovers healed it by {1}".format(mon.name, heal))
         mon.poke.hp = new_health(heal*-1,mon)
   return mon

def new_health(damage, recieveing_mon):
   remaining = recieveing_mon.poke.hp-damage
   if remaining > recieveing_mon.max:
      remaining=recieveing_mon.max
   if remaining<0:
        remaining = 0
        print("{0} has fainted".format(recieveing_mon.name))
   if damage != 0:
      print("{0} has {1} health remaining\n".format(recieveing_mon.name,remaining))
   return(remaining)

def status_move(move, dodge, att_mon, def_mon):
   if move.target == 'self':
      if dodge in [1,4]:
         for x in move.opp.keys():
            att_mon.changes[x] += move.opp[x]
            if att_mon.changes[x] > 12:
               att_mon.changes[x] = 12
            if att_mon.changes[x] < 0:
               att_mon.changes[x] = 0
   else:
      if dodge in [1,4]:
         try:
            for x in move.opp.keys():
               print(def_mon.name,x, move.opp[x])
               def_mon.changes[x] += move.opp[x]
               if def_mon.changes[x] > 12:
                  def_mon.changes[x] = 12
               if def_mon.changes[x] < 0:
                  def_mon.changes[x] = 0
         except:
            print("")
         try:
            if def_mon.status == None:
               if move.self in ['par', 'brn','psn','frz']:
                  def_mon.status = move.self
               elif move.self in ['slp', 'tox']:
                  def_mon.status = {move.self:1}
         except:
            print('')



def dodge_chance(move, att_mon, def_mon):
   eva_acc_table = [.33, .36, .43, .50, .60, .75, 1, 1.33, 1.66, 2, 2.5, 2.66, 3]
   att_acc = eva_acc_table[att_mon.changes['accuracy']]
   def_eva = eva_acc_table[def_mon.changes['evasion']]
   att_status = att_mon.status
   hit_chance = move.acc
   if att_status == 'par':
      if random.randint(1,4) == 1:
         print('it was paralyzed and unable to move')
         return(0)
   if att_status == 'frz':
      if random.randint(1,5) == 1:
         print("{0} thawed out".format(att_mon.name))
         return(4)
      else:
         print('{0} is frozen solid'.format(att_mon.name))
         return(0)
   if type(att_status) == type({'ex':1}):
      if 'slp' in att_status.keys():
         if att_status['slp'] == 1:
            if random.randint(1,4) == 1: #first turn has a 1/4 chance to wake with all the rest having 1/8
               print("{0} woke up".format(att_mon.name))
               return(4)
            else:
               print("{0} is fast asleep".format(att_mon.name))
               return(3)
         if att_status['slp'] < 5:
            if random.randint(1,8) == 1: 
               print("{0} woke up".format(att_mon.name))
               return(4)
            else:
               print("{0} is fast asleep".format(att_mon.name))
               return(3)
         else:
            print("{0} woke up".format(att_mon.name))
            return(4)
   if att_acc == True:
      return(1)
   rand = random.randint(1,100)
   rand = (rand*def_eva)/att_acc
   if rand>hit_chance:
      print("It missed")
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
   if effect == 'boost':
      if 'boosts' in move.opp.keys():
         for boost in move.opp['boosts'].keys():
            print("{0}, {1} {2}".format(def_mon.name,boost,move.opp['boosts'][boost]))
            def_mon.changes[boost] += move.opp['boosts'][boost]
            if def_mon.changes[boost] > 12:
               def_mon.changes[boost] = 12
            if def_mon.changes[boost] < 0:
               def_mon.changes[boost] = 0
      elif 'self' in move.opp.keys():
         for boost in move.opp['self']['boosts'].keys():
            print("{0}, {1} {2}".format(att_mon.name,boost,move.opp['self']['boosts'][boost]))
            att_mon.changes[boost] += move.opp['self']['boosts'][boost]
            if att_mon.changes[boost] > 12:
               att_mon.changes[boost] = 12
            if att_mon.changes[boost] < 0:
               att_mon.changes[boost] = 0
   elif effect in ['brn','par','slp','frz','psn','tox']:
      print('{0} was {1}'.format(def_mon.name, effect))
      if def_mon.status == None:
         if effect in ['brn','par','psn','frz']:
            def_mon.status = effect
         elif effect in ['slp', 'tox']:
            def_mon.status = {effect:1} #tox and slp need to have a turn counter to determine damage and wake chance

      
def self_effect_apply(move, effect, att_mon, def_mon):
   if effect == 'boost':
      for boost in move.self['boosts'].keys():
         att_mon.changes[boost] += move.self['boosts'][boost]
         if att_mon.changes[boost] > 12:
            att_mon.changes[boost] = 12
         if att_mon.changes[boost] < 0:
            att_mon.changes[boost] = 0

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
   clear =0
   power = move.power
   move_type = move.type
   attack_type = move.attack
   hit = 1
   attacking_type1 = attacking_mon_stats.type1
   attacking_type2 = attacking_mon_stats.type2
   defending_type1 = defending_mon_stats.type1
   defending_type2 = defending_mon_stats.type2
   super_effective = super_effective_dict[move.type][defending_type1]*super_effective_dict[move.type][defending_type2] #checks if the move will do extra damage based on type weaknesses
   atk = attacking_mon_stats.atk*stat_table[attacking_mon.changes['atk']]
   spatk = attacking_mon_stats.spatk*stat_table[attacking_mon.changes['spa']]
   defence = defending_mon_stats.defence*stat_table[defending_mon.changes['def']]
   spdef = defending_mon_stats.spdef*stat_table[defending_mon.changes['spd']]
   print("{0} used {1}".format(attacking_mon.name, move.name))
   if move.type == attacking_type1 or move.type == attacking_type2: #if the move type and pokemon type are the same it does 1.5x damage
      stab = 1.5
   else:
      stab = 1
   rand = damage_roll() #random number between .85 and 1
   crit = critical() #1 in 24 chance to deal 1.5x damage
   dodge = dodge_chance(move, attacking_mon, defending_mon)
   if dodge == 4:
      clear = 1
   if dodge == 3:
      return(0,2)
   if attack_type == 'Status':
      status_move(move, dodge, attacking_mon, defending_mon)
      return(0,clear)
   if dodge in [0,3]:
      hit = 0
   if attacking_mon.status == 'brn':
      burn = .5
   if attack_type == "Special":
      damage = (((42*power*(spatk/spdef))/50)+2)*super_effective*stab*crit*rand*hit #the actual calculation
   else:
      damage = (((42*power*burn*(atk/defence))/50)+2)*super_effective*stab*crit*rand*hit #the actual calculation. Only atk is changed by burn status
   
   if dodge == 1 or dodge == 4:
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
   return(math.trunc(damage),clear)



main()
# team1 =Pokemon2(pokemon_data['groudon'], [move_data['swordsdance'],move_data['earthquake'],move_data['firepunch'],move_data['doubleedge']])
# team2 = Pokemon2(pokemon_data['arceus'], [move_data['extremespeed'],move_data['leafstorm'],move_data['icebeam'],move_data['doubleedge']])
# print(team1.status)
# print(damage_calc(team2.moves[2], team2, team1))
# print(team1.status)
# print(damage_calc(bulbasaur.moves[1], bulbasaur, mankey))
# print(mankey.changes)
# team1 = [Pokemon2(pokemon_data['kyogre'], [move_data['growl'],move_data['willowisp'],move_data['tackle'],move_data['hydropump']],pokemon_data['kyogre'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'acc':6,'eva':6}),
#              Pokemon2(pokemon_data['groudon'], [move_data['swordsdance'],move_data['earthquake'],move_data['firepunch'],move_data['doubleedge']],pokemon_data['groudon'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'acc':6,'eva':6})]
# team2 = [Pokemon2(pokemon_data['caterpie'], [move_data['calmmind'],move_data['toxic'],move_data['icebeam'],move_data['doubleedge']],pokemon_data['caterpie'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'acc':6,'eva':6}, status =None),
#              Pokemon2(pokemon_data['wooper'], [move_data['ancientpower'],move_data['aquatail'],move_data['quickattack'],move_data['hydropump']],pokemon_data['wooper'].hp, 'leftovers', stat_changes={'atk':6,'def':6,'spa':6,'spd':6,'spe':6,'acc':6,'eva':6})]
   
# print(pokemon_data['caterpie'].all)
# print(team2[0].max, team2[0].poke.hp)
# print(pokemon_data['kyogre'].all)
# print(pokemon_data['wooper'].all)




# print(move_data['harden'].all)
# print(move_data['growl'].all)
# print(move_data['leafstorm'].all)
# print(move_data['ancientpower'].all)



