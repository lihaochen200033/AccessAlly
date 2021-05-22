import sys

# Support both file input and command line input
if len(sys.argv) == 2:
    # Read input integers from file
    file = open(sys.argv[1])
    cur_line = file.readline()
    # units_of_blood stores the 8 integers for blood units
    units_of_blood = []
    # go over all 8 integers in the current line
    for i in range (0,7):
        separate = cur_line.find(" ")
        units_of_blood.append(eval(cur_line[0:separate]))
        cur_line = cur_line[separate + 1:]
    units_of_blood.append(eval(cur_line))

    # read the second line from file
    cur_line = file.readline()
    # number_of_patients stores the 8 integers for number of patients
    number_of_patients = []
    # go over all 8 integers in the current line
    for i in range (0,7):
        separate = cur_line.find(" ")
        number_of_patients.append(eval(cur_line[0:separate]))
        cur_line = cur_line[separate + 1:]
    number_of_patients.append(eval(cur_line))
elif len(sys.argv) == 17:
    units_of_blood = []
    number_of_patients = []
    for i in range (1,9):
        units_of_blood.append(eval(sys.argv[i]))
    for i in range (9, 17):
        number_of_patients.append(eval(sys.argv[i]))
else:
    raise ValueError('Please provide a filename.')

# store original values
blood = units_of_blood
patients = number_of_patients

# min_unit(a, b): Return the min number between units_of_blood[a] and
#                 number_of_patients[b]
# Effects: Mutates the two lists by reducing the minimum number from
#          units_of_blood[a] and number_of_patients[b]
# min_unit: (Int, Int) -> Int
def min_unit(a, b):
    low = min(units_of_blood[a], number_of_patients[b])
    units_of_blood[a] = units_of_blood[a] - low
    patients[b] = number_of_patients[b] - low
    return low

# Greedy Algorithm
# Order 1
total = 0
# O- (taking all O- you can)
total = total + min_unit(0,0)
# O+ (taking all O+ you can, then taking from 0-)
total = total + min_unit(1,1) + min_unit(0,1)
# A- (taking all A- you can, then taking from 0-)
total = total + min_unit(2,2) + min_unit(0,2)
# B- (taking all B- you can, then taking from 0-)
total = total + min_unit(4,4) + min_unit(0,4)
# A+ (taking all A+ you can, then taking from O+)
total = total + min_unit(3,3) + min_unit(1,3) 
# B+ (taking all B+ you can, then taking from O+)
total = total + min_unit(5,5) + min_unit(1,5)
# A+ (taking all A- you can, then taking from O-)
total = total + min_unit(2,3) + min_unit(0,3) 
# B+ (taking all B- you can, then taking from O-)
total = total + min_unit(4,5) + min_unit(0,5)
# AB- (taking all AB- you can, then taking from B-, A- or O-)
total = total + min_unit(6,6) + min_unit(4,6) + min_unit(2,6) + min_unit(0,6)
# AB+ (taking all AB+ you can, then taking from AB-, B+, B-, A+, A-, O+ or O-)
total = total + min_unit(7,7) + min_unit(6,7) + min_unit(5,7) + min_unit(4,7) +\
        min_unit(3,7) + min_unit(2,7) + min_unit(1,7) + min_unit(0,7)

# Return to the original values
units_of_blood = blood
number_of_patients = patients

# Order 2
total2 = 0
# O- (taking all O- you can)
total2 = total2 + min_unit(0,0)
# O+ (taking all O+ you can, then taking from 0-)
total2 = total2 + min_unit(1,1) + min_unit(0,1)
# A- (taking all A- you can, then taking from 0-)
total2 = total2 + min_unit(2,2) + min_unit(0,2)
# B- (taking all B- you can, then taking from 0-)
total2 = total2 + min_unit(4,4) + min_unit(0,4)

# A+ (taking all A+ you can, then taking from A-)
total2 = total2 + min_unit(3,3) + min_unit(2,3)
# B+ (taking all B+ you can, then taking from B-)
total2 = total2 + min_unit(5,5) + min_unit(4,5)
# A+ (taking all O+ you can, then taking from O-)
total2 = total2 + min_unit(1,3) + min_unit(0,3) 
# B+ (taking all O+ you can, then taking from O-)
total2 = total2 + min_unit(1,5) + min_unit(0,5)

# AB- (taking all AB- you can, then taking from B-, A- or O-)
total2 = total2 + min_unit(6,6) + min_unit(4,6) + min_unit(2,6) + min_unit(0,6)
# AB+ (taking all AB+ you can, then taking from AB-, B+, B-, A+, A-, O+ or O-)
total2 = total2 + min_unit(7,7) + min_unit(6,7) + min_unit(5,7) + min_unit(4,7) +\
         min_unit(3,7) + min_unit(2,7) + min_unit(1,7) + min_unit(0,7)

# Print the output
print(max(total, total2))