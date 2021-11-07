import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import re
import os
from jsonschema import validate

class initialization:

	def __init__(self):
		pass

	def get_candidates(self):
		try:
			return int(input("Number of candidates:"))
		except Exception as e:
			print("Invalid input. Please enter a valid number of candidates.")
			return self.get_candidates()

	def get_voters(self):
		try:
			return int(input("Number of voters:"))
		except Exception as e:
			print("Invalid input. Please enter a valid number of voters.")
			return self.get_voters()

	def get_candidates_from_file(self):
		return int("25_1000_9_10"[:-10])

	def get_voters_from_file(self):
		return int("25_1000_9_10"[3:-5])

	def get_committee_size(self,m):
		try:
			k=int(input("Committee Size (k):"))
			if k>m:
				raise Exception
			return k
		except Exception as e:
			print("Invalid input. Please enter a valid committee size.")
			return self.get_committee_size(m)


	def get_voter_profiles(self):
		path="/Users/kunalrelia/Desktop/DiReCommittee/Code/DivRepCom/API/data/user_given/User1/"
		filename="voter_profile"
		voter_profiles=pd.read_csv(path+filename+".csv")
		#print(voter_profiles)
		return voter_profiles

	def  get_voter_profiles_from_RSM(self,m,n,poset):
		voter_profiles=list()
		try:
			phi=float(input("Enter phi (cohesiveness of voter profile (between 0.1 and 1.0)):"))
			#print(phi)
			if phi<0.1:
				raise Exception
			if phi>1.0:
				raise Exception
			center = list(range(0,m))
			model_1 = poset.Mallows_RSM(center,phi)
			#print("here")
			for i in range(n):
				ranking = model_1.sample_a_ranking()
				pref_pairs=list()
				left=ranking[0]
				for candidate in ranking:
					right=candidate
					if left==right:
						next
					else:
						pref_pairs.append((left,right))
						left=right
				#print(pref_pairs)
				voter_profiles.append(pref_pairs)
			return voter_profiles

		except Exception as e:
			print("Invalid input. Please enter a valid value for phi.")
			return self.get_voter_profiles_from_RSM(m,n,poset)


	def get_scoring_rule(self):
		return input("\n\nScoring Rules\n1. k-Plurality\n2. k-Borda\n3. Chamberlain-Courant\nYour choice:")

