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
    all_vars = soup.find_all("ci")
    for variables in all_vars:
        # open the file that we need to write to in append byte mode
        with open(output_file, "ab") as f:
            var_str = variables.string
            if var_str:
                f.write(var_str.encode('utf-8'))
                f.write("\n".encode('utf-8'))
    infile.close()

# the function that output prettified file for visual
def prettify_files(input_file, output_file):
    infile = open(input_file, "r", encoding='utf-8')
    soup = BeautifulSoup(infile, 'lxml')
    with open(output_file, "wb") as f:
        f.write(soup.prettify().encode())
    infile.close()

# the function to remove all duplicated tokens in file
def clear_duplicate(input_file):
    clear_file(input_file)

def remove_duplicate(input_file):
    variable_list = []
    with open(input_file, "rb") as in_file:
        for line in in_file:
            if line in variable_list:
                continue
            else:
                variable_list.append(line)
    
    with open(input_file, "wb") as rewrite_file:
        rewrite_file.writelines(variable_list)


# open the folder that contains all the input files
input_address = "testFiles"
inputs = get_filenames(input_address)
output_address = "variables"
outputs = get_filenames(output_address)
pretty_address = "prettify"
pretty = get_filenames(pretty_address)

count = 0
while count < min(len(inputs), len(outputs)):
    
    # call the extract function for all files
    extract(inputs[count], outputs[count])
    remove_duplicate(outputs[count])

    # save this line for clear outputs
    # clear_duplicate(outputs[count])
    # prettify_files(inputs[count], pretty_address[count])
    count += 1

