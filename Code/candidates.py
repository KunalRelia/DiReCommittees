import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import re
import os
from jsonschema import validate
import schema

class candidates:

	def __init__(self):
		pass

	def define_candidate_schema(self):
		#change this to make it dynamic based on user input
		candidate_schema = {
		"type" : "object",
		"properties" : {
			"id" : {"type" : "string"},
			"attr" : {"type" : "string"},
			},
		"required": ["id"]
		}

	def check_structure(struct, conf):
		if isinstance(struct, dict) and isinstance(conf, dict):
		# struct is a dict of types or other dicts
			return all(k in conf and check_structure(struct[k], conf[k]) for k in struct)
		if isinstance(struct, list) and isinstance(conf, list):
			# struct is list in the form [type or dict]
			return all(check_structure(struct[0], c) for c in conf)
		elif isinstance(conf, type):
			# struct is the type of conf
			return isinstance(conf, struct)
		else:
			# struct is neither a dict, nor list, not type
			return False

	def get_num_candidate_attributes(self):
		try:
			num=int(input("Enter the number of candidate attributes:"))
			if num>5:
				raise Exception
			return num
		except Exception as e:
			print("Invalid input. Please enter a valid number of candidate attributes (<6).")
			return self.get_num_candidate_attributes()

	def get_num_attribute_groups(self,i,m,k):
		try:
			num=int(input("Enter the number of groups for attribute "+str(i+1)+" :"))
			if (num>k) | (num<1):
				raise Exception
			return num
		except Exception as e:
			print("Invalid input. Please enter a valid number of groups for attribute "+str(i+1)+" (>0 and <="+str(k)+").")
			return self.get_num_attribute_groups(i,m,k)

	def get_diversity_constraints(self,attr_num,group_num,k):
		try:
			num=int(input("Enter the lower bound for Attribute "+str(attr_num+1)+", Group " + str(group_num+1) +" :"))
			if num>k:
				raise Exception
			if num<0:
				raise Exception
			return num
		except Exception as e:
			print("Invalid input. Please enter a valid lower bound (>=0 and <="+str(k)+").")
			return self.get_diversity_constraints(attr_num,group_num,k)


