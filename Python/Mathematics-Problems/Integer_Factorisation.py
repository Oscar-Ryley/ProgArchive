#13/10/2023

def take_input():
    while True:
        num_input = input()
        if num_input.isdigit() == True:
            num_input = int(num_input)
            break
    return num_input

def find_prime_factors():
    number = take_input()
    prime_factor_list = []
    num = 2
    while True:
        if number % num == 0:
            number = number // num
            prime_factor_list.append(num)
            num = 2
        else:
            num += 1
        if number == 1:
            break
    return prime_factor_list

def make_exponentials(plist):
    twodim_array = []
    for i in plist:
        done = False
        for j in twodim_array:
            if j[0] == i:
                j[1] += 1
                done = True
        if done == False:
            twodim_array.append([i, 1])
    output_string = ""
    x = 0
    for i in twodim_array:
        output_string += (str(i[0]) + "^" + str(i[1]))
        if x != len(twodim_array)-1:
            output_string += (" + ")
        x += 1
    return output_string

def main():
    return make_exponentials(find_prime_factors())

print(main())