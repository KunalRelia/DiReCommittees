import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import re
import os
from jsonschema import validate
import schema
import initialization as ini

class actors:

	def __init__(self):
		pass

	def define_actor_schema(self):
		#change this to make it dynamic based on user input
		actor_schema = {
		"type" : "object",
		"properties" : {
			"id" : {"type" : "int"},
			"attr" : {
				{"attr_id" : "string"},
				#ToDo: check if the function supports "categorical"
				{"type" : "string"},
				},
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

	def get_num_of_attributes(self,actor):
		try:
			num=int(input("Enter the number of "+actor+" attributes:"))
			if num<0:
				raise Exception
			return num
		except Exception as e:
			print("Invalid input. Please enter a valid number of "+actor+" attributes (>0).")
			return self.get_num_candidate_attributes(actor)

	def get_num_attribute_groups(self,i,actor, count):
		try:
			num=int(input("Enter the number of groups for attribute "+str(i+1)+" :"))
			if (num>count) | (num<1):
				raise Exception
			return num
		except Exception as e:
			print("Invalid input. Please enter a valid number of groups for attribute "+str(i+1)+" (>0 and <="+str(count)+").")
			return self.get_num_attribute_groups(i,actor, count)


