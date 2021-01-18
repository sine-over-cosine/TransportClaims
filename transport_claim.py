class Claim():
    def __init__(self,date,time,cost):
        self.date=date
        self.time=time
        self.cost=cost
import itertools as it

def format_data(filename):
    data = set()
    file = open(filename+".txt")
    for line in file:
        line=line.strip("\n").split(" ")
        data.add(Claim(line[0],line[1],float(line[2])))
    return data

mylostclaims = format_data("out")
obtained = 788.57
total = 779.87+201.70

def compute_cost(seq_of_data):
    total = 0
    for i in seq_of_data:
        total+=i.cost
    return total

import numpy as np
def unreturned_claims(data):
    file = open("report.txt","w")
    combi = it.combinations(data,8)
    left = total-obtained
    for u in combi:
        cost_= np.round(compute_cost(u),2)
        if abs(compute_cost(u)-left)<0.01 :
            file.write("****************\n")
            file.write("COST: {}\n".format(cost_))
            file.write("Actual left unimbursed: {}\n".format(left))
            for i in u:
                file.write("Date: {} Time: {} Amount: {}\n".format(i.date,i.time,i.cost))

    return 0

unreturned_claims(mylostclaims)
