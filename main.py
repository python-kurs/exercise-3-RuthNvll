# Exercise 3
#-------------------------------------------------------------------------
#Moduls
from pathlib import Path

# import functions from utils here

#------------------------------------------------------------------------
# set directory
data_dir = ("C:/Users/Ruth/Desktop/Eigene_Dateien/01_Studium/PhyGeo_Msc/Profilmodule/Python/exercise-3-RuthNvll/data/")
output_dir = ("C:/Users/Ruth/Desktop/Eigene_Dateien/01_Studium/PhyGeo_Msc/Profilmodule/Python/exercise-3-RuthNvll/solution/")
      
#-----------------------------------------------------------------------

# 1. Construct the path to the text file in the data directory using the `pathlib` module [2P]
cars_path = Path(data_dir, "cars.txt")

# 2. Read the text file [2P]

with open(cars_path) as file:
    cars = [line.rstrip() for line in file]

# 3. Count the occurences of each item in the text file [2P]

uniqueCars = dict((i,cars.count(i)) for i in set(cars))


# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]

"solution" in output_dir

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...
with open(output_dir+"UniqueCars_Count.csv", 'w') as file:
    for key in uniqueCars.keys():
        file.write("%s,%s\n"%(key,uniqueCars[key]))

