import sys
import csv
import pandas as pd
# typesetting the database
# with open ("merge_database", 'ab') as wb:
#     for new in new_set:
#         wb.write(new.encode('utf8'))
file_path = []
symbol_order = []
the_symbol = []
main_attribute = []
sub_attribute = []
contents = []
def txt2csv():
    with open ("merge_database", 'rb') as base:
        for line in base:
            parts = line.decode('UTF-8')[:60].split()
            file_path.append(parts[0])
            symbol_order.append(parts[1])
            the_symbol.append(parts[2])
            main_attribute.append(parts[3])
            # since DS are 2 words, it need extra if statement
            if parts[4] == "Discipline":
                sub_attribute.append("Discipline specified")
            else:
                sub_attribute.append(parts[4])
            
            # the \n in original file affect a lot so we eliminate them by using -2
            length = len(file_path[-1]) + len(symbol_order[-1]) + len(the_symbol[-1]) + len(main_attribute[-1]) + len(sub_attribute[-1])
            contents.append(line.decode('UTF-8')[length + 5: -2]) 

    data = pd.DataFrame({'file path': file_path, 
                        'symbol order': symbol_order,
                        'symbol': the_symbol,
                        'main attribute': main_attribute,
                        'sub attribute' : sub_attribute,
                        'content' : contents,
                        })

    data.to_csv('data.csv', index = False) 


txt2csv()



