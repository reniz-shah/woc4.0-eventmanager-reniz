import matplotlib.pyplot as plt

file = open('Book1.csv','r')
tick_label = []
height = []
for row in file:
    tick_label.append((row.split(','))[0].replace('\n',''))
    try:
        height.append(int((row.split(','))[1].replace('\n','')))
    except:
        y_label = (row.split(','))[1].replace('\n','')
x_label = tick_label.pop(0)
maxx = 5 
title = 'Bar Chart'
left = []
v = 0
for i in range(0,len(height)):
    v = v+maxx
    left.append(v)
plt.bar(left,height,tick_label = tick_label,color = ['black','grey'])
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)
name = str(title) + '.png'
plt.savefig(name)
plt.show()