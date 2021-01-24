import sys
import os
path = 'data'
list1 = []       # citation papers
list2 = []       # research papers
list3 = []       # folder where both of cp & rp are stored
for root, dirs , files in os.walk(path,topdown=False):
    print(f" directory : {root}")
    dirs = root.split('/')
    print(f" dirName 1 : {dirs[0]}")
    if(len(names)==2):
        files = dirs[1].split('_')
        cp = 'data/' + files[0] + '/' + files[0] + '.annv3_parsed_data.csv'
        rp = 'data/' + files[0] + '/' + files[0] + '_parsed_data.csv'
        f_name = 'data/' + files[0]
        list1.append(cp)
        list2.append(rp)
        list3.append(f_name)

for i in range(len(list1)):
    cit = list1[i]
    ref = list2[i]
    folder_name = list3[i]
    # function to be declared
    print(f"folder no. {i+1} evaluated")






