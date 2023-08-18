import csv
from sklearn import tree

x_1=[]
y_1=[]

with open('hight.csv','r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        x_1.append(line[0:3])
        y_1.append(line[3:])

x=x_1[1:]
y=y_1[1:]

# print(x)
# print(y)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
new_data = [[100,89,43],[80,70,38]]
answer = clf.predict(new_data)

# print(answer[0])
# print(answer[1])

for i in range(len(new_data)):
     print(f'Person: {i+1} ==> Gender: {answer[i]}')
