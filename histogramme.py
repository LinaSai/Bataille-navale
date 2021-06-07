
from grille import *
from bateau import *
from fonctions1_2 import *
from bataille import *
import random
import itertools

def distribution_partie_alea():
	ls=[]
	for i in range(1000):
		b=Bataille()
		f=b.joue_alea()
		ls.append(f)
	return ls

def distribution_partie_heuristique():
	ls=[]
	for i in range(1000):
		b=Bataille()

		f=b.joue_heuristique()
		ls.append(f)

	return ls


def distribution_partie_proba_simplifiee():

	ls=[]
	for i in range(1000):
		b=Bataille()
		f=b.joue_probabiliste_simplifiee()
		ls.append(f)
	return ls

def histogramme_partie_alea():
	lp=[]
	lp=distribution_partie_alea()
	plt.hist(lp,bins="auto")
	plt.show()


def histogramme_partie_proba_simplifiee():
	lp=[]
	lp=distribution_partie_proba_simplifiee()
	plt.hist(lp,bins="auto")
	plt.show()


def histogramme_partie_heuristique():
	lp=[]
	lp=distribution_partie_heuristique()
	plt.hist(lp,bins="auto")
	plt.show()


histogramme_partie_alea()
#histogramme_partie_proba_simplifiee()
#histogramme_partie_heuristique()
