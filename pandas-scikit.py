import pandas as pd
from sklearn import tree

h_w_sh=pd.read_csv('hight.csv')
df=pd.DataFrame(h_w_sh)
# print(df)

x=[]
y=[]

hight = df['Hight']
weight = df['Weight']
shoes = df['Shoe size']
gender = df['Gender']


for i in range(len(df)):
     x.append([hight[i],weight[i],shoes[i]])
     y.append([gender[i]])


# print(x)
# print(y)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
new_data = [[100,89,43],[180,70,38],[165,80,42],[165,70,38]]
answer = clf.predict(new_data)
# print(answer[0])
# print(answer[1])

for i in range(len(new_data)):
     print(f'Person: {i+1} ==> Gender: {answer[i]}')
