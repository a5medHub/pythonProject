import sys
import time


def menu():  # sleep is added to let the user see the info before listing again the menu , you can remove it if you want
    choice = 0
    print('\n******************\nLOADING List'), time.sleep(2),
    while choice != -1:  # o(n)
        print('******************',
              '\nTo select Enter the number of the choice: ',
              '\n1  Display Statistics: ',
              '\n2  Display All Students: ',
              '\n3  Add New Student: ',
              '\n4  Remove Student: ',
              '\n5  Enroll Existing Student in a Course: ',
              '\n6  Edit Student: ',
              '\n7  Display Student: ',
              '\n8  Exit')

        choice = input()
        if choice == '1':
            display_statistics()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            add_new_student()
        elif choice == '4':
            remove_student()
        elif choice == '5':
            eesic()  # Enroll_Existing_Student_in_a_Course
        elif choice == '6':
            Edit_Student()
        elif choice == '7':
            Display_Student()
        elif choice == '8':
            to_exit()
        else:
            print('******************\n', choice, 'Is an invalid input\n', 'try a number from 1 to 8',
                  '\n******************')
            time.sleep(2)
        # print("******************\n******************")


def display_statistics():
    c_fcs = 0
    c_fsw = 0
    c_fsw22 = 0
    for student in tmp_dict.keys():
        if 'FCS' == tmp_dict[student][2][0:3]:  # 2 is the value of course_name
            c_fcs += 1
        if 'FSW' == tmp_dict[student][2][0:3]:
            c_fsw += 1
        if 'FSW22' == tmp_dict[student][2][0:5]:
            c_fsw22 += 1
    print('Total Number of FCS Students is: ', c_fcs
          , '\nTotal Number of FSW Students is: ', c_fsw
          , '\nTotal Number of FSW22 Students is: ', c_fsw22)
    menu()


def display_all_students():
    for i in tmp_dict.values():
        print(i[1], i[0], i[2][0:3])


def add_new_student():
    ID = input('Enter the ID of the student: ')
    if ID in tmp_dict:  # check existing student
        print(ID, 'already exists !')
    elif ID not in tmp_dict:  # id not found // add new student
        fName = input('Student First name: ')
        lName = input('Student Last name: ')
        tmp_dict[ID] = fName, lName, 'N/A'
    menu()


def remove_student():
    ID = input('To remove student enter his/her id: ')
    if ID in tmp_dict:  # check if id exist
        del tmp_dict[ID]
    elif ID not in tmp_dict:
        print('ID:', ID, 'not found')
    menu()


def eesic():
    ID = input('To enrol course enter his/her id: ')
    if ID in tmp_dict:
        course = input('Enter the course you want to register: ')
        tmp_dict[ID][2] = course
    elif ID not in tmp_dict:
        print('ID:', ID, 'not found')
    menu()


def Edit_Student():
    ID = input('To edit student enter his/her id: ')
    if ID in tmp_dict:
        fName = input("First name: ")
        tmp_dict[ID][0] = fName

        lName = input('Last name: ')
        tmp_dict[ID][1] = lName

        course = input('Enter the course name: ')
        tmp_dict[ID][2] = course

    elif ID not in tmp_dict:
        print('ID:', ID, 'not found')

    menu()


def Display_Student():
    Display_Student_dict = {}
    choice = input('Choose 1 to enter the first name or 2 to enter the ID: ')

    if choice == '1':
        fName = input('enter the first name: ')
        for y, values in tmp_dict.items():  # O[n]
            if fName == tmp_dict[y][0]:
                Display_Student_dict[y] = tmp_dict[y]

        for k, v in Display_Student_dict.items():  # O[n]
            print(k, Display_Student_dict[k][1], Display_Student_dict[k][0], Display_Student_dict[k][2])

    if choice == '2':
        ID = input('enter the first name: ')
        if ID in tmp_dict:
            print(id, tmp_dict[id][1], tmp_dict[id][0], tmp_dict[id][2])
        else:
            print('ID: ', ID, ' does not exist')
    else:
        print('please enter a valid number ether [1 or 2]')
    menu()


def to_exit():
    choice = input('Enter (1) to Save before Exit or (2) to terminate without saving: ')
    if choice == '1':
        with open("Student.txt", "w") as tmp_save:
            for i in tmp_dict.keys():
                tmp_save.write(
                    i + ":" + tmp_dict[i][0] + "," + tmp_dict[i][1] + "," + tmp_dict[i][2] + "\n")
        print('goodbye')
        sys.exit()
    elif choice == '2':
        print('goodbye')
        sys.exit()
    else:
        print('please Enter (1) to Save before Exit or (2) to terminate without saving: ')


# not finished yet
def lName_sorted():
    for i in tmp_dict.keys():
        for j in tmp_dict.values():
            if len(i[1]) < len(j[1]):
                print(len(i))
                print('true', i, j)

            print('false', i, j)


print('******************\n', '\tWelcome', '\n******************')
for i in range(0, 5):  # five attempt only
    if i > 5:  # O(N)
        sys.exit()
    else:
        userName = input('Please enter the UserName: ')
        userPass = input('hello ' + userName.upper() + ' Please enter the Password: ')
        if userName == 'admin' and userPass == 'admin123123':  # O(N)*2
            print('******************\n', 'Welcome ', userName.upper(), '\n******************')

            tmp_dict = dict()
            tmp_student = open('Student.txt', 'r')  # open file as read mode
            for student in tmp_student:
                ID, *Values = student.rstrip().split(
                    ':')  # reading line by line from tmp_student + splitting keys & values
                for x in Values:  # nested loop for split values from each other of the same line
                    x = Values[0].split(',')
                tmp_dict[ID] = x  # save in dict
            menu()

        else:  # elif userName != 'admin' or userPass != 'admin123123'
            i += 1
            if i < 5:
                print('Incorrect UserName and/or Password', '\nattempt ', i, ' you still have ', 5 - i, ' attempt')
            else:
                print('you have no more attempt!!'.upper())
