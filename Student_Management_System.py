import random,string,datetime,time,os
os.system('cls')
StudentReg=[(f'2019-MC-{i+1:0>2}') for i in range(77)] #Generating registration
Studentemail=[(f'2019mc{i+1:0>2}@student.uet.edu.pk') for i in range(77)] #Generating Eamils.
#Below I write name of students. 
SecA=['Ali Haider', 'Hafiz Muhammad Talha', 'Abdul Rehman', 'Hafiz Muhammad Irfan', 
    'Abdul Hadi', 'Muhammad Abdullah', 'Usman Irshad Bhatti', 'Waleed Raza', 'Sami Ullah Saleem',
    'Dawood Muhammad Tahir', 'Abdullah Khan ', 'Sauf Ullah Afzal', 'Asad Raza ', 'Muhammad Ahmad',
    'Huzaifa Sarwar', 'Ahmed Imran', 'Muhammad Hassan', 'Momin Sarmad', 'Syed Ali Raza', 
    'Muhammad Umar Mubashir', 'Hisham Khan Awaz', 'Muhammad Umer Farooq', 'Muhamad Ahmad', 
    'Muhammad Ali Hamza', 'Haseeb Ahmad Fiai', 'Muhammad Qasim', 'Dawood Imtiaz', 'Muhammad Nafees',
    'Mujtaba Shabbir', 'Syed Faraz Ali Rizvi', 'Usman Tariq', 'Muhammad Ibrahim', 'Zain Zakir', 
    'Shaheer Ahmad Khan', 'Maesha Ijaz', 'Umme Habiba', 'Yusra Kashif', 'Shawar Zahra', 'Irsa Idrees', 
    'Nukhba Iqbal']
SecB=['Zorain Bin Khalid', 'Muhammad Shaheer', 'Ali Irfan', 'Abdul Rehman Sajid', 
    'Talha Tayyab', 'Wali Sheikh', 'Muhammad Talha Arshad', 'Amaan Majid', 'Arslaan Rafique', 'Wasif Ali', 
    'Safi Ullah', 'Muhammad Haris', 'Haffiz Asad Ullah','Faraz Shah', 'Hamza Ubaid', 'Asad Ali', 'Muhammad Zohaib Khalid', 
    'Zain-ul-Hassan', 'Rana Ahmad Latif', 'Shahzaib Ali Afaq', 'Muhammad Shess', 'Muhammad Usman', 'Danish Ali', 
    'Usman Tariq', 'Abdur Rehman Sarwar', 'Mohsin Sohail','Nadeem Ansari','Muhammad Haroon', 'Raja Haseeb Ahmad', 'Junaid Ali ', 'Heera Baig', 
    'Noor-Ul-Huda', 'Laveeza Yasin', 'Asmaa Tabasum Bhatti', 'Maleeha Syed', 'Makarma Rashid', 'Areeba Azhar']
Session_19=[SecA,SecB]
CreditHours={  # This dictionary contain subjects name as keys with credit hours as values.
    'CP-I' : 1.00,
    'CP-I_Lab': 3.00,  
    'EM' : 2.00, 
    'EM_Lab' : 1.00, 
    'ED' : 3.00, 
    'ED_Lab' : 1.00, 
    'DLD' : 3.00, 
    'DLD_Lab' :1.00, 
    'VCA' : 3.00
    }
cgpa=[f'{random.uniform(1,4):.3f}' for i in range(77)] ## For this project I'm randomly generating cgpa.But for finding it, there is also a user-defined function.
def AllStudentsReg(n,y,d): 
    '''Here I use list comprehension to generate registrations of n students of y year. '''
    StudentReg=[print(f'{y}-{d}-{i+1:0>2}') for i in range(n)] 
    '''If I use print statement inside list comprehension then it will also return None.
    To solve that simply remove print inside the list comprehension.  '''
    return StudentReg
def StudentDetail(reg):
    ''' Input Argument is regitration number. 
        Ouput is required student details.'''
    if( (  len(SecA)+len(SecB)  ) < reg or reg<0 ): #Checking a valid registration.
        return(print("Total Students are from 01 to 77 in 19-session."))
    elif(reg<=len(SecA)): #Students detail from section-A
        StudentDetail={
            "Name" : f'{SecA[reg-1]}',
            "Reg"  : f'{StudentReg[reg-1]}',
            "Cgpa" : f'{cgpa[0]}',
            "Email": f'{Studentemail[reg-1]}',
        }
    else:  #Students detail from section-A
        StudentDetail={
            "Name" : f'{SecB[reg-41]}',
            "Reg"  : f'{StudentReg[reg-1]}',
            "Cgpa" : f'{cgpa[reg-1]}',
            "Email": f'{Studentemail[reg-1]}',     
        }
    return(print(StudentDetail))
def calculateGPA():
    ''' Just enter grade of subjects and the output is gpa. 
    If you want to change subjects then this funtion also helps you.'''
    CreditHours={  # I use dictionary here as well because outside dictionary is not accessible.
    'CP-I' : 1.00,
    'CP-I_Lab': 3.00,  
    'EM' : 2.00, 
    'EM_Lab' : 1.00, 
    'ED' : 3.00, 
    'ED_Lab' : 1.00, 
    'DLD' : 3.00, 
    'DLD_Lab' :1.00, 
    'VCA' : 3.00
    }
    print('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F')
    print(f'The Subjects with credit hours are: {CreditHours}')
    change = input('Do You want to change the subjects with there Credit_Hours [Y/N]: ')
    if (change == 'Y' or change == 'y'): #checking If user wants to change subjects.
        sub= int(input('How Many Subjects you want to enter: '))
        d=[input(f'Enter {i+1}-subject name:  ')  for i in range(sub)]
        f= [int(input(f'Enter {d[i]} credit hour :  '))   for i in range(sub)]
        a=dict(zip(d,f))
        CreditHours=a  #changing dictionary. 
        print('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F')  
    z=[input(f"Enter Letter Grade of {i}:  ")   for i in CreditHours ] # It contains grade like A, B+ .
    dic={
        'A+':4,'A':4,'A-':3.7,
    'B+':3.3,'B':3.0,'B-':2.7,
    'C+':2.3,'C':2.0,'C-':1.7,
    'D+':1.3,'D':1.0,
    'F':0.0
    }
    x=gradepoint=[dic[i.upper()] for i in z] 
    y=CreditHoursPoints=[CreditHours.get(i) for i in CreditHours] #getting credit hours of subjects.
    gpa=[x[i]*y[i] for i in range(len(y))] #Simply use gpa formula.
    return (sum(gpa)/sum(y))
def GradeForSubjects():
    ''' Randomly generating grades for different subjects of different students. '''
    g=['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
    s= [i for i in CreditHours]
    # This function can become advance by using following
    # change = input('Do You want to change the subjects with there Credit_Hours [Y/N]: ')
    # if (change == 'Y' or change == 'y'): #checking If user wants to change subjects.
    #     sub= int(input('How Many Subjects you want to enter: '))
    #     d=[input(f'Enter {i+1}-subject name:  ')  for i in range(sub)]
    #     f= [int(input(f'Enter {d[i]} credit hour :  '))   for i in range(sub)]
    #     a=dict(zip(d,f))
    #     CreditHours=a
    #     s= [i for i in CreditHours]

    output =  { s[i]:random.choice(g)  for i in range(len(s)) }
    return list(output.items())
def cgpCalByRandomGrades():
    '''This function stored random gardes list and stored them in variable o. 
    and on basis of that its return GPA.'''
    o=GradeForSubjects()
    o=dict(o)
    z=[ o.get(i)  for i in o ] # Its have grades. A+, C.
    dic={
        'A+':4,'A':4,'A-':3.7,
    'B+':3.3,'B':3.0,'B-':2.7,
    'C+':2.3,'C':2.0,'C-':1.7,
    'D+':1.3,'D':1.0,
    'F':0.0
    }

    x=gradepoint=[dic[i.upper()] for i in z] #It contain grade Points.
    y=CreditHoursPoints=[CreditHours.get(i) for i in o] #It contains credit hours points.
    gpa=[x[i]*y[i] for i in range(len(y))]
    return (sum(gpa)/sum(y)) 
def fullDetail():
    '''Returns all the details of session. '''
    #Using SecA,B and StudentReg and Student Emails and subjects grades and GPA.
    a=[]
    for i in range(len(SecA)+len(SecB)):
        if(i<len(SecA)):
            a.append(f'{(SecA[i]):>20}\t{StudentReg[i]:>10}\t{Studentemail[i]}\t{cgpCalByRandomGrades():.3f}\t{GradeForSubjects()}')
        else:
            a.append(f'{SecB[i-len(SecA)]:>20}\t{(StudentReg[i]):>10}\t{Studentemail[i]}\t{cgpCalByRandomGrades():.3f}\t{GradeForSubjects()}')
    return a #returns session detail.
def AddStudentDetails(n,ns,y,d):
    ''' If you want to add another session detail then this function will helps you.
    n,ns,y,d are session number,number of total students,year and department coded name.
    This Function Return data in txt file. '''
    j=0 # j used to upgrade student number.
    for i in range(ns):
        name=input(f'Enter {j+1:0>3}-student name: ')
        reg=input(f'Enter Student registration > {y}-{d}- ')
        email=input('Enter Student email: ')
        cgpa=input('Enter Student CGPA: ')
        j+=1
        s='\t\t'.join([name,reg,email,cgpa])
        with open(f'{n}-session Details.txt','a') as f: #Only storing all data in txt file using append mode.
            f.write('\n')
            f.write(s)
localtime = time.asctime(time.localtime(time.time()))
dt = datetime.datetime.now()
print('#####################################################################################################################################################')
print(f'''                                      Enter the specific Letters to see your desired Output.                       Date: {localtime}
----------------------------------------------------------------------------------------------------------------------------------------------------

Code             Detail

F     | For full detail of 19-session.
SEC   | To see the names of the students in all sections.
SD    | For detail of the single student.
SGPA  | To calculate gpa of a Student. You can also change SUBJECTS and then finds Gpa.
SORT  | To get details on the basis of GPA (higher to lower).
RANGE | To see the students Registration with gpa in the specific range.
GRS   | To Generate Registrations of students of any department You Want.
NSD   | To enter new session Details and save them in a txt file.
######################################################################################################################################################''')
t=input('Enter letters:  '.upper().strip())
if (t.lower()=='F'.lower()):
    #Accessing data from full detal function and writing it into the txt file.
    with open('19-Full Details.txt','a') as f:
        f.write((f'''The Semester Subjects With there Credit Hours and the complete students details Shown Below

        {CreditHours}                    Date: {localtime}'''))
        f.write(f''' 
        
        ''')
        f.write('\n')
        f.write('      Name           Registration             Email           CGPA             Grades Of All Subjects')
        f.write('\n')

        for i in fullDetail():
            f.write('\n')
            f.write(i)
    print('See the file "19-Full Details.txt"')
elif(t.lower() == 'SEC'.lower() ):
    #Access data from Session_19 contains sections details and storing it in txt file.
    with open ('Section Names.txt','w') as f:
        A='A'
        for i in Session_19:

            f.write(f'---------- SECTION-{A} ----------')
            f.write('\n')
            for j in i:
                f.write(j)
                f.write('\n')
            A='B'
    print("See the file 'Section Names.txt'.")       
elif(t.lower()=='SORT'.lower() ):
    with open('Sorted_Details.txt','w') as f:
        for i in fullDetail():
            f.write(i)
            f.write('\n')
    with open('Sorted_Details.txt','r') as f:
        c=[] # It contain [['Ali Haider', '2019-MC-01', '2019mc01@student.uet.edu.pk', '3.545',
        b=[] # It contains gpa not in sorted way.
        for i in f:
            i=i.strip()
            L=i.split('\t')
            b.append(L[3])  
            c.append(L)

        a=sorted(b,reverse=True)  ## contains all the sorted gpas H to L
        d=[] # This contains names 
        e=[] # This contains registration 
        for i in a: 
            for gp in c:
                if i in gp:
                    if gp[0] not in d:
                        d.append(gp[0])
                        e.append(gp[1])
    with open('Sorted_Details.txt','w') as f:
        c=0
        for i in d:
            f.write(i+'\t\t'+a[c] + '\t\t' + e[c] ) 
            c+=1
            f.write('\n')  
    print("See the file 'Sorted_Details.txt'. ")
            ### It return  sorted name and cgpa in file  Sorted_Details.txt      
elif( t.lower()== 'SD'.lower()):
    r=int(input('Enter the Roll number of student, 2019-MC-'))
    #Using StudentDetail function and access its data and printing it on terminal window.
    StudentDetail(r)
elif(t.lower() =='SGPA'.lower() ):
    #Simply calling calculate GPA function and storing it in a file.
    r=int(input('Enter the Roll number of student, 2019-MC-'))
    with open('Gpa Calclation.txt','a') as f:
        f.write(f'2019-MC-{r}\t\t{calculateGPA():.3f}\n')
        print(f'CGPA of 2019-MC-{r} Successfully stored in Gpa Calculation.txt')
elif(t.lower()=='NSD'.lower() ):
    #Using AddStudentDetails function, and taking input arguments from user for the function.
        n=input('Enter the session number: ')
        ns=int(input('Enter Number of Students: '))
        y=int(input('Enter the session year[0000]: '))
        d=input('Enter department short name [Like ME for Mechanical]: ')
        AddStudentDetails(n,ns,y,d)
elif(t.lower() == 'RANGE'.lower() ):
    #Firstly I make 19_Full details.txt and then taking data from it I write specific range data into specific range file.
    with open('19-Full Details.txt','a') as f:
        f.write((f'''The Semester Subjects With there Credit Hours and the complete students details Shown Below

        {CreditHours}  '''))
        f.write(f''' 
        
        ''')
        f.write('\n')
        f.write('      Name           Registration             Email           CGPA             Grades Of All Subjects')
        f.write('\n')

        for i in fullDetail():
            f.write('\n')
            f.write(i)
    h=eval(input('Enter the Range highest value[4 to 1]: '))
    l=eval(input('Enter the Range lowest value[less then highest]: '))
    with open('19-Full Details.txt','r') as f:
        c=[]
        b=[]
        for i in f:
            i=i.strip()
            L=i.split('\t')
            if(len(L)<5):
                continue
            c.append(L)
            b.append([L[3],L[1]])
        #Out side the Loop list b  contains tuple (gpa,reg),
        #Now I only need range on basis of gpa with reg also
        r=[]
        for i in b:
            i[0]=float(i[0])  # (gpa, reg) ## Converting str to floar to check if its greater or smaller
            if ( l < i[0]  <  h ):
                i[0]=str(i[0]) ## converting back to string because I also need it as str while writing in file.
                r.append(i)
        r.sort(reverse=True)
        # # list r contains the range of gpa from higher to lower also with reg
        with open('Specific Range.txt','w' ) as f:
            for i in r:
                f.write(i[1] + '\t\t' + str(i[0]))
                f.write('\n') 
    print("See the file 'Specific Range.txt'. ")
elif(t.lower() == 'GRS'.lower()):
    #Using AllStudentsReg Function and taking input arguments from user for the function.
    n=int(input('How many number of registrations you want? : '))
    y=input('Enter the session Year[0000]: ')
    d=input('Enter department short name [Like ME for Mechanical]: ')
    O=AllStudentsReg(n,y,d)
    print(O)
else:
    print('''Kindly Follow the Instructions to get your Desired Details.\nThanks!''')















