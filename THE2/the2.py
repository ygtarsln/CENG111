#
# WRITE YOUR CODE HERE AND SEND ONLY THIS FILE TO US.
#
# DO NOT DEFINE get_data() here. Check before submitting

import math
import random
from evaluator import *    # get_data() will come from this import

whole_info = get_data()


def new_pst(mv,pst): # finding the new position : mv = 2, pst = (x,y) for instance
	if mv == 0:
		return pst[0],pst[1]+1
	elif mv == 1:
		return pst[0]-1,pst[1]+1
	elif mv == 2:
		return pst[0]-1,pst[1]
	elif mv == 3:
		return pst[0]-1,pst[1]-1
	elif mv == 4:
		return pst[0],pst[1]-1
	elif mv == 5:
		return pst[0]+1,pst[1]-1
	elif mv == 6:
		return pst[0]+1,pst[1]
	elif mv == 7:
		return pst[0]+1,pst[1]+1


def new_move():
	m = whole_info[0]
	n = whole_info[1]
	Dis = whole_info[2]
	ka = whole_info[3]
	lamda = whole_info[4]
	mu = whole_info[5]
	universal_state = whole_info[6]
	people = len(whole_info[6])
	moves = []
	new_positions = []
	old_positions = []

	def prob_move(individual):  # computing the next position of individual

		lst_move = individual
		green = 0.5 * mu
		yellow = 0.125 * mu
		blue = 0.5 * (1 - mu - mu ** 2)
		purple = 0.4 * (mu ** 2)
		gray = 0.2 * (mu ** 2)

		if lst_move == 0:
			res_ls = random.choices([0, 1, 2, 3, 4, 5, 6, 7],weights=[green, yellow, blue, purple, gray, purple, blue, yellow], k=1)
			return res_ls[0]  # direction 5 , for example
		elif lst_move == 1:
			res_ls = random.choices([1, 2, 3, 4, 5, 6, 7, 0],weights=[green, yellow, blue, purple, gray, purple, blue, yellow], k=1)
			return res_ls[0]
		elif lst_move == 2:
			res_ls = random.choices([2, 3, 4, 5, 6, 7, 0, 1],weights=[green, yellow, blue, purple, gray, purple, blue, yellow], k=1)
			return res_ls[0]
		elif lst_move == 3:
			res_ls = random.choices([3, 4, 5, 6, 7, 0, 1, 2],weights=[green, yellow, blue, purple, gray, purple, blue, yellow], k=1)
			return res_ls[0]
		elif lst_move == 4:
			res_ls = random.choices([4, 5, 6, 7, 0, 1, 2, 3],weights=[green, yellow, blue, purple, gray, purple, blue, yellow], k=1)
			return res_ls[0]
		elif lst_move == 5:
			res_ls = random.choices([5, 6, 7, 0, 1, 2, 3, 4],weights=[green, yellow, blue, purple, gray, purple, blue, yellow], k=1)
			return res_ls[0]
		elif lst_move == 6:
			res_ls = random.choices([6, 7, 0, 1, 2, 3, 4, 5],weights=[green, yellow, blue, purple, gray, purple, blue, yellow], k=1)
			return res_ls[0]
		elif lst_move == 7:
			res_ls = random.choices([7, 0, 1, 2, 3, 4, 5, 6],weights=[green, yellow, blue, purple, gray, purple, blue, yellow], k=1)
			return res_ls[0]  # direction 7 for example

	def infection_prob(dst, mask1, mask2):

		if dst > Dis:
			return 0
		elif dst <= Dis:
			if mask1 == "masked" and mask2 == "masked":
				return (min(1, (ka / (dst ** 2)))) / (lamda ** 2)
			elif (mask1 == "masked" and mask2 == "notmasked") or (mask1 == "notmasked" and mask2 == "masked"):
				return (min(1, (ka / (dst ** 2)))) / lamda
			else:
				return min(1, (ka / (dst ** 2)))
	for person in universal_state:
		old_positions.append(person[0])


	for person in universal_state:  #[[(34, 21), 4, 'notmasked', 'notinfected'], [(27, 28), 2, 'notmasked', 'notinfected'], [(40, 28), 6, 'notmasked', 'infected'], [(34, 33), 2, 'masked', 'notinfected']]
		move = prob_move(person[1])
		new_position = new_pst(move,person[0])
		if new_position in old_positions:
			new_positions.append(person[0])
			moves.append(person[1])
		elif new_position in new_positions:
			new_positions.append(person[0])
			moves.append(person[1])
		elif (new_position[0] < 0 or new_position[0] > (n-1)) or (new_position[1] < 0 or new_position[1] > (m-1)):
			new_positions.append(person[0])
			moves.append(person[1])
		else:
			new_positions.append(new_position) # new_positions = [(33, 22), (26, 28), (41, 27), (35, 32)] for instance
			moves.append(move) # moves = [1, 2, 5, 5] for instance

	infection_update = people * ["a"] # to store the new infection data

	for i in range(0,people): # infection update
		for j in range(i+1,people):
			distance = ((new_positions[i][1]-new_positions[j][1])**2 + (new_positions[i][0]-new_positions[j][0])**2)**0.5
			if infection_prob(distance,universal_state[i][2],universal_state[j][2]) > 0:
				if (universal_state[i][3] == "notinfected" and universal_state[j][3] == "notinfected") or (universal_state[i][3] == "infected" and universal_state[j][3] == "infected"):
					continue
				elif universal_state[i][3] == "notinfected" and universal_state[j][3] == "infected":
					chance = infection_prob(distance,universal_state[i][2],universal_state[j][2])
					new_state = random.choices(["infected","notinfected"], weights = [chance,1-chance], k = 1)[0]
					if new_state == "notinfected":
						continue
					elif new_state == "infected":
						infection_update[i] = "infected"
						continue
				elif universal_state[i][3] == "infected" and universal_state[j][3] == "notinfected":
					chance = infection_prob(distance, universal_state[i][2], universal_state[j][2])
					new_state = random.choices(["infected", "notinfected"], weights=[chance, 1 - chance], k=1)[0]
					if new_state == "notinfected":
						continue
					elif new_state == "infected":
						infection_update[j] = "infected"
						continue

	useless = 0
	for k in infection_update: # this loop replaces the untouched "a"s in the infection_update list with the previous infection data
		if k == "a":
			infection_update[useless] = universal_state[useless][3]
		useless += 1

	for t in range(0,people):
		universal_state[t][0] = new_positions[t]
		universal_state[t][1] = moves[t]
		universal_state[t][3] = infection_update[t]

	return universal_state





