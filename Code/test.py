#import the usual libraries (e.g., pandas, numpy, etc.)
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import re
import os

#import DiRe-related libraries
import initialization as init
import candidates as cand
import committee_election as elect

#import ipywidgets as widgets
from ipywidgets import interact
from ipywidgets import widgets
from ipywidgets import Layout

start_election=init.initialization()

m=start_election.get_candidates()
n=start_election.get_voters()
k=start_election.get_committee_size(m)
scoring_rule=start_election.get_scoring_rule()
voter_profile=start_election.get_voter_profiles()

candidate_info=cand.candidates()

num_of_cand_attributes=candidate_info.get_num_candidate_attributes()

cand_attr_groups=[0]*num_of_cand_attributes
for i in range(0,num_of_cand_attributes):
    cand_attr_groups[i]=candidate_info.get_num_attribute_groups(i,m)

for a in range(0,num_of_cand_attributes):
    print("Lower Bounds for Candidate Attribute "+str(a+1)+"")
    
    for i in range(0,cand_attr_groups[a]):
        @interact(lower_bound=widgets.IntSlider(
        value=0,
        min=0,
        max=m,
        step=1,
        description='Group '+str(i+1)+':',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        layout=Layout(width='50%', height='15px')
        ))

        def visualization_1(lower_bound=0):
            next

a=elect.committee_election(m,n,k,scoring_rule,voter_profile)
a.get_committee()