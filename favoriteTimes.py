import sys

if len(sys.argv) != 2:
    raise ValueError('Please provide an argument(either a integer D or a filename.')

# Supporting both command line input and file input
# Read from command line
if sys.argv[1].isdigit():
    D = int(sys.argv[1])
else:
    # Read input integer from file
    file = open(sys.argv[1])
    D = int(file.readline())
    # print(D) # debug, print the input duration integer
if D < 0 or D > 1000000000:
    raise ValueError('Please provide a valid duration integer D where 0 <= D <= 1000000000.')
    
# We first find all the possible arithmetic sequences in 12 hours    
# count used records the number of arithmetic sequence
count = 0
# result used to store all arithmetic sequence stamp
result = []
for hour in range(1,13):
    # get the tens digit of hour
    hour_tens = hour // 10
    # get the units digit of hour
    hour_units= hour % 10

    for minute_tens in range(0, 6):
        for minute_units in range(0, 10):
            # get the differences between digits
            d_1 = hour_units - hour_tens
            d_2 = minute_tens - hour_units
            d_3 = minute_units - minute_tens
            if (d_2 == d_3):
                if (hour_tens == 0):
                    count = count + 1
                    result.append((hour, minute_tens*10+minute_units))
                elif (d_1 == d_2):
                    count = count + 1
                    result.append((hour, minute_tens*10+minute_units))
                
# We consider 12:34 as a special case and remove 12:34 from the 
# end of result list
result = result[:-1]

# print(count) # debug, printing the total number of arithmetic sequences in 12 hours
# print(result) # debug, printing the result list for all arithmetic sequences

# calculate the actual output
# num_of_cycle stores the number of 12-hour cycle in the duration
num_of_cycle = D // (12 * 60)
# left_out_duration is the minutes left
left_out_duration = D % (12 * 60)
# number of arithmetic sequences met for time in the cycles
output = num_of_cycle * count

if (left_out_duration >= 34):
    output = output + 1

if (left_out_duration >= 60):
    # get the hour and minute for the end_time
    hour = left_out_duration // 60
    minute = left_out_duration % 60

    # calculate the number of arithmetic sequences in the left duration
    for i in range(len(result)):
        cur_hour = result[i][0]
        cur_minute = result[i][1]
        if (cur_hour < hour):
            output = output + 1
        elif (cur_hour <= hour) and (cur_minute <= minute):
            output = output + 1
        else:
            break

print(output)
