import os, csv
from pathlib import Path

# change this to create the posts for different years
year = '2021'

# folder where the data and the posts are respectively
DATA_DIR = os.getcwd() + os.sep + '..' + os.sep + '_data'
POSTS_DIR = os.getcwd() + os.sep + '..' + os.sep + '_posts'
# base name for our google file
file = "Machine Learning Club Schedule - "

# make the year folder if it doesn't exist already
Path(POSTS_DIR + os.sep + year).mkdir(parents=True,exist_ok=True)

# go through the csv file and create a markdown
with open(DATA_DIR + os.sep + file + year + '.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # title of the file
        titleSimple = ( ( row['title'].strip() ).replace(" ","-")
                                ).translate({ord(c): None for c in '!@#$:'})
        # no spaces in filename
        filename = row['date'].strip() + '-' + titleSimple + '.md'

        # writing the markdown file
        with open(POSTS_DIR + os.sep + year + os.sep + filename,"w+") as f:
            f.write("---\n")
            for key in row:
                value = (row[key].replace("--","")).strip() # get rid of empty --
                value = value.replace('"',"'") # stick to one quotation
                if key=='date':
                    f.write(f"{key}: {value}\n")
                elif value=='':
                    f.write(f"{key}: \n") # empty for variable that don't exist
                else:
                    f.write(f'{key}: "{value}"\n') # value as a string
            f.write("---\n")
            f.close()

print("Thank you for updating the schedule, Comrade!")
