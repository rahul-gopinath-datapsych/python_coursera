
def valley_input(data_input):
    first_step = 0
    total_valley = 0
    for i in data_input:
        for j in i:
            if j == 'U':
                first_step = first_step + 1
                if first_step == 0:
                    total_valley = total_valley + 1
            elif j == 'D':
                first_step = first_step - 1
    return total_valley

#data_input = ['UDDDUDUU']

data_input = ['DDUUDDUDUUUD']   


total_valley = valley_input(data_input)

print("Total Number of Valleys encountered during trail: " + str(total_valley))
            

