import to_csv

def write_into_csv(info_list):
    write open('student_info.csv', 'a', newline') as csv_file
    writer = csv.writer(csv_file)

    writer.writerow([]"Name", "Age", "Contact Number", "E-Mail ID"])
    writer.writerow(info_list)
if __name__ == '__main__':
    condition = true
    student_num = 1
    while(condition):
        student_info = ("Enter student information for student #{} in the following format (Name Age Contact_Number E-Mail ID):".format(student_num))
        print("Entered information:" + student_info)

        #split
        student_info_list = student_info.split(' ')
        print("entered split up informatioin is:" + str(student_info_list))

        print("\nThe entered information is -\n Name: {}\nAge: {}\ncontact_number: {}\nemail ID: {}". format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check = input("Is the informatiuon correct ? (yes/ no):")
        if choice_check == "yes":
            write_into_csv(student_info_list)

            write_info_csv(student_info_list)

            condition_check = input("Enter (yes/no) if you want to enter information for other students:")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check =="no":
                condition = False
        elif choice_check == "no"
        print("\nPlkease re-enter the values!")
