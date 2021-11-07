import pandas as pd

path="/Users/kunalrelia/Desktop/DiReCommittee/Code/DivRepCom/API/data/user_given/User1/"
filename="25_1000_9_10"
voter_profiles=pd.read_csv(path+filename+".csv")

voter_profiles_new=pd.DataFrame()

for i in range(len(voter_profiles)):
	for j in range(len(voter_profiles.columns)):
		ctr=25-1-j
		for k in range(ctr):
			voter_profiles_new.iloc[[k]]={i,voter_profiles.loc[0].iloc[[0]][0].split(',')[0][1:]}

print(voter_profiles.loc[0].iloc[[0]][0].split(',')[0][1:])
print(voter_profiles.loc[0].iloc[[0]][0].split(',')[1][1:-1])