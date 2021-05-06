

import random
random.seed(111)




def get_data():
	"""Get the initial state of the individuals & the environment"""
	       #[M, N,   D,   K, LAMBDA, MU,    universal_state]
	return [50, 100, 5,  80,  30,   0.55,  [[(34, 21), 4, 'notmasked', 'notinfected'] , [(27, 28), 2, 'notmasked', 'notinfected'] , [(40, 28), 6, 'notmasked', 'infected'] , [(34, 33), 2, 'masked', 'notinfected']]]
