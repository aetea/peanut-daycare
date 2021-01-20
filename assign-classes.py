### Go through all students and assign them to groups according to age ###

from kiddos import kiddos   # dictionary of kids 


class Daycare:
    
    def __init__(self):
        groups = []   

    def balance_groups(self):
        """Balance group sizes by moving oldest students to next group"""
        
        for i, group in enumerate(self.groups[:-1]):
            # TODO> sort students by age
            # check if group has too many students
            num_transfers = len(group.students) - group.class_max
            if num_transfers > 0:
                # if yes, bump oldest students to next age group                
                kids_to_move = group.students[-num_transfers:]
                del group.students[-num_transfers:]

                next_group = self.groups[i+1]
                next_group.students[:0] = kids_to_move

        # repeat for next oldest group    


class Group(Daycare):

    school = None       # TODO: QUESTION> is there a better way to do this?
    
    def __init__(self, min_age, max_age, class_max, name):
        self.min_age = min_age
        self.max_age = max_age
        self.class_max = class_max
        self.name = name
        self.students = []

        # TODO> add group instance to daycare's groups list?? 


    def add_student(self, student):
        """Add a student to the group."""
        # add student to this age group 
        self.students.append(student)


class Student(Daycare):
    
    def __init__(self, name, bday, age, parents):
        """Create a Student instance"""
        self.name = name
        self.bday = bday
        self.age = age
        self.parents = parents 


# TODO> create student instances from the kiddo dict
# loop over kiddo dict
# create a student instance for each kid


# ---- Sample kiddos dictionary for testing ------
some_kiddos = {}
i = 0

for kid_name, kid_info in kiddos.items():
    if i < 10:
        some_kiddos[kid_name] = kid_info
        i += 1
    else:
        break

print(some_kiddos)
# -----------------------------------------------


############################
### SETUP PEANUT DAYCARE ###
############################

# set up age groups
baby_group = Group(0, 1.5, 10, "babies")
ones_group = Group(1.5, 2, 8, "ones")
twos_group = Group(2, 3, 8, "twos") ## too many kids
threes_group = Group(3, 4, 8, "threes")  ## too many kids
fours_group = Group (4, 5, 10, "fours")

peanut_daycare = Daycare()
peanut_daycare.groups = [baby_group, ones_group, twos_group, threes_group, fours_group]


# =============================================
#   Match students to best age group 
# ---------------------------------------------
# NOTE: kiddos is a dict {name: [list of info]}

for kid_name in kiddos:

    kid_info = kiddos[kid_name]
    kid_age = kid_info[1]

    print(f"now checking {kid_name} who is {kid_age} {type(kid_age)}")

    for group in peanut_daycare.groups:
        # ...print(f"...checking {kid_name} against {group.name}...") 
        # compare kiddo.age to the various groups age requirements
        if kid_age >= group.min_age and kid_age <= group.max_age:
            # add them to the best group (Group method)
            group.add_student(kid_name) 
            # ...print(f"{kid_name} was added to the {group.name} group, which now has: ")
            # ...print(group.students)
            break 


# ===========================================
#    Balance groups in daycare
# -------------------------------------------
peanut_daycare.balance_groups()


# ===========================================
#    Display groups and students
# -------------------------------------------