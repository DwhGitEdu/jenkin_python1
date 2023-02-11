#####################
## proyecto pytho ##
#####################

import os

List1 = [8, 9, 3, 6, 1, 10]
List1.reverse()
print("The reversed list is", List1)

List2 = [81, 92, 33, 64, 11, 101]
List2.sort()
print("The sorted list is", List2)

List3 = []
List3 = List1.copy()
print("The copy list", List3)

Indexvalue = List2[2:6]
print("The index value ", Indexvalue)

import pandas
df = pandas.DataFrame(data={"col1": List1, "col2": List2})

df.to_csv("C:/Users/EDUARDO/Desktop/05_REPOS/99_EXPORT_FILES/file.csv", sep=',',index=False)

