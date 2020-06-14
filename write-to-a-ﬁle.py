from datetime import datetime as dt  
today = dt.now()
file_name = "my_first_file.txt"
with open(file_name, "w") as file_object:   
    file_object.write("Hello file!\n")   
    file_object.write(str(today))
    file_object.write("\n You're my favorite file!")