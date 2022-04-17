Firstly presenting user some coded letters for specific outputs.
F     | For full detail of 19-session.
SEC   | To see the names of the students in all sections.
SD    | For detail of the single student.
SGPA  | To calculate gpa of a Student. You can also change SUBJECTS and then finds Gpa.
SORT  | To get details on the basis of GPA (higher to lower).
RANGE | To see the students Registration with gpa in the specific range.
GRS   | To Generate Registrations of students of any department You Want.
NSD   | To enter new session Details and save them in a txt file.

if user == F:
    calling full detail function and storing data in txt file.
elif(user == SEC ):
    geting detail from sections list and storing data in txt file.
elif(user == SORT ):
    Loading data from full detail file and then sorting it on the basis of CGPA and 
    storing it in a txt file.
elif(user == SD):
    calling single student detail function and then return a dictionary.
elif(user == SGPA):
    calling GPA Calculation funtion, then finds GPA by using grades and creditHours list and 
    then returning and saving data in a txt file.
elif(user == RANGE):
    User enter the specific range of GPA. Then loading data from full detail.txt file
    and then storing specific range data in text file.
elif(user == GRS):
    Getting data from user like, number of students, department name and year,
    and then using data as input argument of AllstudentReg function and then 
    returning roll numbers that user can copy in a file.
elif(user == NSD):
    It will take required data from user such as session number, number of students user wants to add,
    and registration, email and then using all this data it will use a function AdStudentDetails and then ,
    returning data in a txt file.