# Gender-prediction-program-based-on-height-weight-and-shoe-size-based-on-scikit-learn

![1200px-Scikit_learn_logo_small svg](https://github.com/Peyman2012/Gender-prediction-program-based-on-height-weight-and-shoe-size-based-on-scikit-learn/assets/88220773/3d8c0e3b-15f1-4372-829e-4c0e6a24761e)


**Gender prediction program based on height, weight and shoe size based on scikit-learn**

Import csv in variables x_1 and y_1.
Because it reads the rows of the dataset columns using the csv library and gives an error. From the index, one and the next should be poured into the x and y variables.

     x_1=[]
     y_1=[]

     with open('hight.csv','r') as csvfile:
            data = csv.reader(csvfile)
            for line in data:
                    x_1.append(line[0:3])
                    y_1.append(line[3:])

     x=x_1[1:]
     y=y_1[1:]


We cannot use classification in this project because the classifier generally separates distinct classes, and so this classifier expects a string or an integer type to distinguish different classes from each other (this is called the "target " Is known). You can read more about this in Introduction to Classifiers.
The problem we are trying to solve is to determine a continuous numerical output, Result. This is known as a regression problem, so we need to use a regression algorithm (such as DecisionTreeRegressor):



     clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x,y)
    new_data = [[100,89,43],[80,70,38]]
    answer = clf.predict(new_data)
    for i in range(len(new_data)):
        print(f'Person: {i+1} ==> Gender: {answer[i]}')


