def initialization():
  def do_global():
    global m
    global n
    global k
    global voter_profiles
    
  def initialization(file):
    if file is not None:
        #Todo: Make this user defined. Need to take input from user.
        path="/Users/kunalrelia/Desktop/DiReCommittee/Code/DivRepCom/Data/Input/"
        filename="25_1000_9_10"
        voter_profiles=pd.read_csv(path+filename+".csv")
    
    m=25
    n=10000
    k = input("Committee Size:")
    do_global()
    
    