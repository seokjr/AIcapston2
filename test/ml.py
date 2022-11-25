import random
import numpy as np
import pandas as pd



score = []
num_people = 5

for i in range(num_people):
    score.append(random.choices(range(0, 6), k=8))

def group_user(score):
    num_user = len(score)
    score_rank = []
    user = []
    user2 = []
    result1 = 0
    result2 = 0
    group_ar = [[None] * 3 for i in range(num_user)]
    similarity_ar = [[99] * num_user for i in range(num_user)]
    
    for i in range(num_user):
        df = pd.Series(score[i])
        rnk = df.rank(method='min', ascending=False)
        rnk = [round(n) for n in list(rnk)]
        score_rank.append(rnk)

    for i in range(num_user):
        user.append(score[i])
        user.append(score_rank[i])

    for i in range(0, len(user), len(user)//num_user):
        user2.append([user[i], user[i+1]])

    for x in range(num_user):
        for y in range(num_user):
            if x==y:
                continue
            for z in range(2):
                for k in range(8):
                    if (z == 0):
                        result1 = 0.5*(user2[x][z][k] - user2[y][z][k])**2
                    else:
                        result2 = 0.5*(user2[x][z][k] - user2[y][z][k])**2         
                    similarity_ar[x][y] = result1 + result2
                
    for i in range(num_user):
        df1 = similarity_ar[i]
        df1 = [round(n) for n in list(df1)]   
        df1 = np.array(df1)
        temp = df1.argsort()
        ranks = np.empty_like(temp)
        ranks[temp] = np.arange(len(df1))
        for j in range(num_user):
            if ranks[j] == 0:
                group_ar[i][0] = j 
            elif ranks[j] == 1:
                group_ar[i][1] = j
            elif ranks[j] == 2 :
                group_ar[i][2] = j

    return group_ar

group_user(score)
