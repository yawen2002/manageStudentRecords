#The program menu
print("Welcome to the Simple Class Calculator. Here's the list of available options:")
print("")
print("1- Enter a student record(Name, ID, and 4 grades separated by commas and no spaces).")
print("2- Display the full class data sorted in alphabetical order based on name.")
print("3- Display the class descriptive statistics.")
print("4- Display a chosen student record.")
print("5- Exit")
print("")
choice=int(input("Select an option by entering its number or 5 to exit:"))
list_of_ID=[]
list_of_students=[]
#Hold the data for all students. Each list element holds the data for one student.
def Letter_Grade(total):
    '''Calculate the Letter Grade for a student.'''
    if total>=87:
        return 'A'
    elif 86>=total>=75:
        return 'B'
    elif 74>=total>=65:
        return 'C'
    elif total<65:
        return 'F'
#Option 1
while choice != 5:
    if choice==1:
        enter=input("Enter a student record(Name, ID, and 4 grades separated by commas and no spaces:")
        sub_enter=enter.split(",")
        for i in range(2,len(sub_enter)):
            sub_enter[i]=float(sub_enter[i])
        if len(sub_enter[1])!=7:
            print("ID must have 7 digits. Record rejected.")
            continue #brings back to the menu
        elif len(sub_enter)!=6:
            print("Record Incomplete, Record rejected.")
        elif sub_enter[2]>25 or sub_enter[3]>25 or sub_enter[4]>25 or sub_enter[5]>25:
            print("Grades for tests and assignments are out of 25 each.")
            continue
        elif sub_enter[1] in list_of_ID:
            print("Duplicate ID number. Record rejected.")
            continue
        else: #it's a good record.
            print("Record Accepted")
            sub_enter[1]=int(sub_enter[1])#make ID integer.
            list_of_ID.append(sub_enter[1])
            total=float(sub_enter[2])+float(sub_enter[3])+float(sub_enter[4])+float(sub_enter[5])
            sub_enter.append(total)
            y=Letter_Grade(total)
            sub_enter.append(y)#sub_enter holds data for one student.
            print(sub_enter)
            list_of_students.append(sub_enter)
            print(list_of_students)
        #The program menu
        print("Welcome to the Simple Class Calculator. Here's the list of available options:")
        print("")
        print("1- Enter a student record(Name, ID, and 4 grades separated by commas and no spaces).")
        print("2- Display the full class data sorted in alphabetical order based on name.")
        print("3- Display the class descriptive statistics.")
        print("4- Display a chosen student record.")
        print("5- Exit")
        print("")
        choice=int(input("Select an option by entering its number or 5 to exit:"))
#Option 2
    if choice==2:
        list_of_students.sort()
        print(list_of_students)
        #The program menu
        print("Welcome to the Simple Class Calculator. Here's the list of available options:")
        print("")
        print("1- Enter a student record(Name, ID, and 4 grades separated by commas and no spaces).")
        print("2- Display the full class data sorted in alphabetical order based on name.")
        print("3- Display the class descriptive statistics.")
        print("4- Display a chosen student record.")
        print("5- Exit")
        print("")
        choice=int(input("Select an option by entering its number or 5 to exit:"))
#Option 3
    if choice==3:
        number=len(list_of_students) #number of students entered
        print("Number of students entered is", number)
        big_total=0
        total_test_1=0
        total_test_2=0
        total_assign_1=0
        total_assign_2=0
        for student in list_of_students:
            big_total=big_total+student[6]
            total_test_1=total_test_1+student[2]
            total_test_2=total_test_2+student[3]
            total_assign_1=total_assign_1+student[4]
            total_assign_2=total_assign_2+student[5]
        average=big_total/number #class average
        print("Class average is", average)
        test_1=total_test_1/number #average grade for test 1
        test_2=total_test_2/number #average grade for test 2
        assign_1=total_assign_1/number #average grade for assignment 1
        assign_2=total_assign_2/number #average grade for assignment 2
        print("Average grade for Test 1 is", test_1, ". Average grade for Test 2 is", test_2, ". Average grade for Assignment 1 is", assign_1, ". Average grade for Assignment 2 is", assign_2, ".")
        times_A=0
        times_B=0
        times_C=0
        times_F=0
        for student in list_of_students:
            if student[7]=='A':
                times_A=times_A+1
            elif student[7]=='B':
                times_B=times_B+1
            elif student[7]=='C':
                times_C=times_C+1
            elif student[7]=='F':
                times_F=times_F+1
        print(times_A, "students got A.", times_B, "students got B.", times_C, "students got C.", times_F, "students got F.")
        h=0
        for student in list_of_students:
            if student[6]>=average:
                h=h+1
                a=number-h
        print("Number of students above or on the average is", h)
        print("Number of students below the average is", a)
        #The program menu
        print("Welcome to the Simple Class Calculator. Here's the list of available options:")
        print("")
        print("1- Enter a student record(Name, ID, and 4 grades separated by commas and no spaces).")
        print("2- Display the full class data sorted in alphabetical order based on name.")
        print("3- Display the class descriptive statistics.")
        print("4- Display a chosen student record.")
        print("5- Exit")
        print("")
        choice=int(input("Select an option by entering its number or 5 to exit:"))
#Option 4
    if choice==4:
        l=int(input("Enter the ID of a student:"))
        for student in list_of_students:
            if student[1]==l:
                print("Name:", student[0])
                print("ID:", l)
                print("Test Grades:",student[2],",",student[3])
                print("Assignment Grades:",student[4],",",student[5])
                print("Total Grade:",student[6])
                print("Letter Grade:",student[7])
        #The program menu
        print("Welcome to the Simple Class Calculator. Here's the list of available options:")
        print("")
        print("1- Enter a student record(Name, ID, and 4 grades separated by commas and no spaces).")
        print("2- Display the full class data sorted in alphabetical order based on name.")
        print("3- Display the class descriptive statistics.")
        print("4- Display a chosen student record.")
        print("5- Exit")
        print("")
        choice=int(input("Select an option by entering its number or 5 to exit:"))
#Option 5
exit
print("You exit the program.")
