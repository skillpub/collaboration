'''add a script to skills'''

data = input('drop me the script')

if type(data) is dict:
    file_name = list(data.keys())[0]
    data = data[file_name]
    
    f = open('../'+file_name, "wb")
    f.write(data)
    f.close()
    
    print('done')
else:
    print('i was waiting for a text file')
