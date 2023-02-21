import os

def intro_variable(input_file, output_file):
    sum = get_variable_size(input_file)

    with open(input_file, "rb") as in_file, open(output_file, "wb") as out_file:
        print("Now you are in file " + input_file)
        print("This file contains " + str(sum) + " variables in total")

        count = 1
        for line in in_file:
            print( "The " + str(count) + " variable to be define is " +  line.decode('utf8'))
            count += 1
            inp = input("This variable should be catorized as : ")
            low_inp = inp.lower()
            if low_inp == "variable" :
                dimension = input("Is it a Scalar, Vector, or Matrix? \n")
                low_dim = dimension.lower()
                if (low_dim != "scalar" or low_dim != "vector" or low_dim != "matrix"):
                    print("Not a valid answer")




# a helper function to get the total number of variables in the file
def get_variable_size(input_file):
    with open(input_file, "rb") as in_file:
        count = 0
        for line in in_file:
            count += 1
    return count

def get_variable_list(input_file):
    with open(input_file, "rb") as in_file:
        output = []
        for variables in in_file:
            output.append(variables.decode()) 
    return output


def remove_n(binary_variable):
    binary_in = binary_variable.encode('utf8')
    out = binary_in[0:-2]
    return out.decode('utf8')

# a helper function that return all filenames in given path
def get_filenames(input_address):
    file_list = []
    for filename in os.listdir(input_address):
        file_list.append(input_address + "/" + filename)
    return file_list

variable_address = "variables"
var_list = get_filenames(variable_address)
variable_add = get_variable_list(var_list[0])
a= remove_n(variable_add[0])

database = 'test_database'
# while count < len(var_list):
 #   intro_variable(var_list[count], database)

  #  count += 1