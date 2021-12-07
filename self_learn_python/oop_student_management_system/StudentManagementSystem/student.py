class Student(object):
    def __init__(self, name: str, gender: str, telephone_number):
        self.name = name
        self.gender = gender
        self.telephone_number = telephone_number

    def __str__(self):
        return f'Info of this student: Name: {self.name}, Gender: {self.gender}, Telephone Number: {self.telephone_number}'


if __name__ == '__main__':
    jim = Student('Jim', 'M', 12345678)
    print(jim)
