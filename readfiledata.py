import csv

data_list = []

def read(filename, sep):
    ''' Parameters: filename, sep(column separator)
        Description:  Reads data from file and return a list of dictionaries
                    which contain key as column name and value as row data'''
    try:
        with open(filename,'r') as f:
            reader = csv.reader(f, delimiter=sep)
            for col in reader:
                if col[1] == 'D':
                    data = {
                    'Customer_Name':col[2],
                    'Customer_ID': col[3],
                    'Open_Date': col[4],
                    'Last_Consulted_Date':col[5],
                    'Vaccination_Id':col[6],
                    'Dr_Name':col[7],
                    'State':col[8],
                    'Country':col[9],
                    'DOB':col[10],
                    'Is_Active':col[11]   
                    }

                    data_list.append(data)
        
        return data_list

    except FileNotFoundError:
        return "File {} does not exist.".format(filename)

    except Exception as e:
        return e



# Execution demo
fdata = read('sample.txt','|')
for row in fdata:
    print(row)