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
