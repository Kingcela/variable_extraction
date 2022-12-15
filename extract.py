from bs4 import BeautifulSoup

# since we are reading and writing html files, we have to read in and write in bytes
infile = open("testFiles/1001.0008.html", "rb")
outfile = open("prettified_files/prettified_08.html", "wb")

# create the soup object for searching
soup = BeautifulSoup(infile, 'lxml')
# write the prettified version of origional file to prettified
pretty = soup.prettify()
outfile.write(pretty.encode())
# first try finding all parts with mathML encoding
all_vars = soup.find_all(encoding="MathML-Content")

for variables in all_vars:
    with open("variables/variables_08.text", "w") as f:
        if (variables.string == "None"):
            continue
        else:
            #print(variables.string)
            f.writelines(variables.string.encode('utf8'))


infile.close()
outfile.close()















