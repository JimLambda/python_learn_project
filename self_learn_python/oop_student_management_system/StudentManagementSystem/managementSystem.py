from student import Student


class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        self.load_students()
        while True:
            self.show_menu()

            menu_num = int(input('Please input an option: '))
            if menu_num == 1:
                # Add a student.
                self.add_student()
            elif menu_num == 2:
                # Delete a student.
                self.delete_student()
            elif menu_num == 3:
                # Modify a student.
                self.modify_student()
            elif menu_num == 4:
                # Query a student.
                self.search_student()
            elif menu_num == 5:
                # Show all students.
                self.show_students()
            elif menu_num == 6:
                # Save the student info.
                self.save_student()
            elif menu_num == 7:
                # Exit.
                break

    # Show function menu.
    @staticmethod
    def show_menu():
        """
        Show menu. Static method.

        :return: None.
        """
        print('Please choose an function:')
        print('1. Add a student.')
        print('2. Delete a student.')
        print('3. Modify a student.')
        print('4. Query info of a student.')
        print('5. Show info of all students.')
        print('6. Save the student\'s info.')
        print('7. Exit the system.')

    def add_student(self):
        print('Add a student.')
        name = input('Please input your name: ')
        gender = input('Please input your gender: ')
        telephone_number = input('Please input your telephone number: ')

        student = Student(name, gender, telephone_number)

        self.student_list.append(student)
        print(self.student_list)
        print(student)

    def delete_student(self):
        print('Delete a student.')
        delete_name = input('Please input the name of who you want to delete: ')
        for student_object in self.student_list:
            if student_object.name == delete_name:
                self.student_list.remove(student_object)
                break
        else:
            print('There is no such student!')

    def modify_student(self):
        print('Modify a student.')
        modifing_student_name = input('Please input the name of the student which you want to modify: ')
        for student_object in self.student_list:
            if student_object.name == modifing_student_name:
                student_object.name = input('Please input the new name: ')
                student_object.gender = input('Please input the new gender: ')
                student_object.telephone_number = input('Please input the new telephone number: ')
                print('Modify successfully! ', end='')
                print(student_object)
                break
        else:
            print('There is no such student!')

    def search_student(self):
        print('Search/Query a student.')
        searching_student_name = input('Please input the name of the student: ')
        for student_object in self.student_list:
            if student_object.name == searching_student_name:
                print(student_object)
                break
        else:
            print('There is no such student!')

    def show_students(self):
        print('Show all students\'s info.')
        for student_object in self.student_list:
            print(
                f'Name: {student_object.name}, Gender: {student_object.gender}, Telephone number: {student_object.telephone_number}.')

    def save_student(self):
        print('Save the student\'s info.')
        with open('student.data', 'w', encoding='utf-8') as file:
            student_info_dict_list = [student_object.__dict__ for student_object in self.student_list]
            file.write(str(student_info_dict_list))

    def load_students(self):
        print('Loading students\'s info...')
        try:
            with open('student.data', 'r', encoding='utf-8') as file:
                content = file.read()
                if content != '':
                    student_info_dict_list = eval(content)
                    self.student_list = [Student(i['name'], i['gender'], i['telephone_number']) for i in
                                         student_info_dict_list]
                else:
                    return
        except:
            pass
