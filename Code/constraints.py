import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import re
import os
from jsonschema import validate
import schema
import initialization as ini

class constraints:

	def __init__(self):
		pass

	def define_constraint_schema(self):
		#change this to make it dynamic based on user input
		constraint_schema = {
		"type" : "object",
		"properties" : {
			"attr_id" : {"type" : "int"},
			"constraint" : {"type" : "int"},
			},
		"required": ["attr_id","constraint"]
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


	#ToDo: get constraints from user or by generating it
	#toDo: check if constraints are less than or equal to group size
	def get_constraints(self,actor):
		return input("constraints")
