#!/usr/bin/python
import matplotlib.pyplot  as  plt  
x=["ashu","python","prateek","blu"]
y=[100,30,20,150]

#x1=[3,66,33,9]
#y1=[13,6,3,19]

plt.xlabel("name of people")
plt.ylabel("number of occurance")
plt.scatter(x,y,label="general word count with dots ",marker="*",s=200)
plt.plot(x,y,label="general word count with line")
plt.bar(x,y,label="bar plot")
#plt.plot(x1,y1,label="fake data")
plt.legend()
plt.grid()
plt.show()

