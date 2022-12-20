from bs4 import BeautifulSoup
import os

# a helper function to remore all text in file
def clear_file(to_delete):
    open(to_delete, 'w').close()

# a helper function that return all filenames in given path
def get_filenames(input_address):
    file_list = []
    for filename in os.listdir(input_address):
        file_list.append(input_address + "/" + filename)
    return file_list


# the main function that extract all math tokens in a file
def extract(input_file, output_file):
    infile = open(input_file, "r", encoding='utf-8')
    soup = BeautifulSoup(infile, 'lxml')
    all_vars = soup.find_all(encoding="MathML-Content")
    for variables in all_vars:
        # open the file that we need to write to in append byte mode
        with open(output_file, "ab") as f:
            var_str = variables.string
            if var_str:
                f.write(var_str.encode('utf-8'))
                f.write("\n".encode('utf-8'))
    infile.close()



# open the folder that contains all the input files
input_address = "testFiles"
inputs = get_filenames(input_address)
output_address = "variables"
outputs = get_filenames(output_address)

count = 0
while count < min(len(inputs), len(outputs)):
    # call the extract function for all files
    extract(inputs[count], outputs[count])
    # save this line for clear outputs
    # clear_file(outputs[count])
    count += 1














