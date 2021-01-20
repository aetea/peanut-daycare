"""Read and process data about kiddos to convert into dictionary"""

import csv 

# initialise dictionary of kids
kiddos = {}
kiddos_headers = []

with open("DaycareEnrollmentInfo.csv", "r") as kiddo_file:
    kiddo_file_read = csv.reader(kiddo_file)    # converts each line into list
    # list = [name, bday, age, ds18m, ds2y, ds3y, ds4y, parents]
    # list has 8 items

    #--- Don't read header row ---#
    # kiddos_headers = next(kiddo_file_read)
    next(kiddo_file_read)
            
    for kiddo_all in kiddo_file_read:
        # pull out index 0, 1, 2, 7
        kiddo_name = kiddo_all[0]
        kiddo_bday = kiddo_all[1]
        kiddo_age = float(kiddo_all[2])
        kiddo_parents = kiddo_all[7]
        kiddos[kiddo_name] = [kiddo_bday, kiddo_age, kiddo_parents]
        # TODO> make student instances instead 

# print(kiddos_headers)
# print(kiddos)
# # QA> how do i print just first 5 dict items? cannot slice
#     # AA> have to for loop and set index; could also use SQL (to learn soon)