import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import re
import os
import random

class committee_election:

	def __init__(self,m,n,k,scoring_rule,voter_profile,num_of_cand_attributes,cand_attr_groups,
                           diversity_constraints,num_of_voter_attributes,voter_attr_groups,representation_constraints):
		self.m=m
		self.n=n
		self.k=k
		self.scoring_rule=scoring_rule
		self.voter_profile=voter_profile
		self.num_of_cand_attributes=num_of_cand_attributes
		self.cand_attr_groups=cand_attr_groups
		self.diversity_constraints=diversity_constraints
		self.num_of_voter_attributes=num_of_voter_attributes
		self.voter_attr_groups=voter_attr_groups
		self.representation_constraints=representation_constraints

	def print_committee(self,candidate_scores):
		winning_candidates=[index for index, value in sorted(enumerate(candidate_scores), reverse=True, key=lambda x: x[1])][:int(self.k)]
		for pos in range(0,len(winning_candidates)):
			print("Candidate "+str(winning_candidates[pos])+" scores "+str(candidate_scores[int(winning_candidates[pos])]))


	def k_plurality(self):
		candidate_scores = [0] * self.m
		for i in range(0,len(self.voter_profile)):
			vote=self.voter_profile[i]
			#vote=self.voter_profile.iloc[i]
			candidate_scores[int(re.sub("[()' ]", '', str(vote[0])).split(',')[0])]+=1
			#for j in range(0,len(vote)):
			#	candidate_scores[int(re.sub("[()' ]", '', str(vote[j])).split(',')[0])]+=1
			#for pos in range(0,int(self.k)):
			#	candidate_scores[int(re.sub("[()' ]", '', vote[pos]).split(',')[0])]+=1
		return candidate_scores

	def k_Borda(self):
		candidate_scores = [0] * self.m
		for i in range(0,len(self.voter_profile)):
			vote=self.voter_profile[i]
			#vote=self.voter_profile.iloc[i]
			for pos in range(0,len(vote)):
				candidate_scores[int(re.sub("[()' ]", '', str(vote[pos])).split(',')[0])]+=(int(self.m)-pos-1)
			#candidate_scores[int(re.sub("[()' ]", '', str(vote[pos-1])).split(',')[1])]+=(int(self.m)-pos-1)
		return candidate_scores

	def diversity_feasibility_check(self):
		for a in range(0,self.num_of_cand_attributes):
			sum=0
			for i in range(0,self.cand_attr_groups[a]):
				sum=sum+self.diversity_constraints[a][i]
			if sum>self.k:
				print("There is no feasible committee!")
				return False
		return True

	def create_groups(self):
		candidate_groups = []
		for i in range(0,self.num_of_cand_attributes):
			candidate_groups.append([str('')] * self.cand_attr_groups[i])
		#print(candidate_groups)
		
		for a in range(0,self.num_of_cand_attributes):
			for cand in range(0,self.m):
				group_num=random.randint(0,self.cand_attr_groups[a]-1)
				#print(group_num)
				#print(candidate_groups[a][group_num])
				candidate_groups[a][group_num]=candidate_groups[a][group_num]+','+(str(cand))
		#print(candidate_groups)
		return candidate_groups


	def create_populations(self):
		voter_population = []
		for i in range(0,self.num_of_voter_attributes):
			voter_population.append([str('')] * self.voter_attr_groups[i])
		#print(candidate_groups)
		
		for a in range(0,self.num_of_voter_attributes):
			for voter in range(0,self.n):
				group_num=random.randint(0,self.voter_attr_groups[a]-1)
				#print(group_num)
				#print(candidate_groups[a][group_num])
				voter_population[a][group_num]=voter_population[a][group_num]+','+(str(voter))
		#print(candidate_groups)
		return voter_population
			


	def get_committee(self):
		if self.diversity_feasibility_check()==False:
			return

		candidate_groups=self.create_groups()
		voter_population=self.create_populations()

		#feasible_committees=self.find_dire_committees()
		
		#lambda x: print_committee() if x == '1' else lambda x: print_committee() if x == '2' else print_committee()
		if self.scoring_rule=='1':
			self.print_committee(self.k_plurality())
		elif self.scoring_rule=='2':
			self.print_committee(self.k_Borda())
		# else:
		# 	CC(m,n,k,voter_profiles,scoring_rule)

