import random
import numpy as np
import pymysql
import pandas as pd
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
import MySQLdb

    
#가져오기

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='tests', charset='utf8')
cursor = db.cursor()

sql = 'SELECT * FROM test_grade'
cursor.execute(sql)
result = cursor.fetchall()

a = []
aa=[]
aaa = []


for i in range(len(result)):
    a.append(result[i][1])

for x in range(8):
    aa = []
    if x==0:
        for i in range(8):
            aa.append(a[i])
    elif x == 1:
        for i in range(8):
            aa.append(a[i+8])
    elif x == 2:
        for i in range(8):
            aa.append(a[i+16])
    elif x == 3:
        for i in range(8):
            aa.append(a[i+24])
    elif x == 4:
        for i in range(8):
            aa.append(a[i+32])
    elif x == 5:
        for i in range(8):
            aa.append(a[i+40])
    elif x == 6:
        for i in range(8):
            aa.append(a[i+48])
    elif x == 7:
        for i in range(8):
            aa.append(a[i+56])
    aaa.append(list(aa))    # -*- coding: utf-8 -*-

    
def group_user(score):
    num_user = len(score)
    score_rank = []
    user = []
    user2 = []
    result1 = 0
    result2 = 0
    group_ar = [[None] * 3 for i in range(num_user)]
    similarity_ar = [[99] * num_user for i in range(num_user)]
    
    engine = create_engine("mysql+mysqldb://root:"+"1234"+"@localhost/tests", encoding='utf-8')
    conn = engine.connect()
    
    
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
    
    for i in range(len(group_ar)):
        for x in [0,1,2]:
            group_ar[i][x] = group_ar[i][x] + 1 
    
    for i in range(num_user):
        if i == 0:
            x = [1, 1, 1]
            data = pd.DataFrame(zip(x, group_ar[i]))
            data.to_sql(name ='blog_grouprecommend',con=engine, if_exists='replace')
        else:
            x = [i+1, i+1, i+1]
            data = pd.DataFrame(zip(x, group_ar[i]))
            data.to_sql(name ='blog_grouprecommend',con=engine, if_exists='append')


    return group_ar

