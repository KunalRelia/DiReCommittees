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
			"v_id" : {"type" : "string"},
			"preferences" : {"type" : "string"},
			},
		"required": ["id","preferences"]
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

	def is_vote_valid(self, vote,n):
		regex=r"(\(\d,\d\),|\(\d,\d\)$)"
		matches = re.finditer(regex, vote, re.MULTILINE)
		for matchNum, match in enumerate(matches, start=1):
			next
		if matchNum!=int(n):
			return False
		return True


	def get_voter_preferences(self,n):
		try:
			votes=ini.get_votes()
			voter_ctr=1
			for vote in votes:
				voter_ctr=voter_ctr+1
				if !is_vote_valid(vote):
					raise Exception
			return votes
		except Exception as e:
			print("Invalid voter profile for voter "+str(voter_ctr)+" .")
			return self.get_voter_preferences(actor)

