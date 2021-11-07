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

# #import ipywidgets as widgets
# from ipywidgets import interact
# from ipywidgets import widgets
# from ipywidgets import Layout

if input("Do you want to use system-generated data (Y/N):")=="N":
    start_election=init.initialization()
    

    #read data from the user-uploaded files\
    voter_profile=start_election.get_voter_profiles()
    m=start_election.get_candidates_from_file()
    n=start_election.get_voters_from_file()
    k=start_election.get_committee_size(m)
    scoring_rule=start_election.get_scoring_rule()

    #print(str(m)+" "+str(n)+" "+str(k))

    a=elect.committee_election(m,n,k,scoring_rule,voter_profile)
    a.get_committee()
    