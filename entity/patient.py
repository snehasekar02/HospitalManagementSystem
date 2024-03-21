class Patient:
    def __init__(self, patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address):
        self.__patientId = patientId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__contactNumber = contactNumber
        self.__address = address

    def set_patient_id(self, patientId):
        self.__patientId = patientId

    def set_first_name(self, firstName):
        self.__firstName = firstName

    def set_last_name(self, lastName):
        self.__lastName = lastName

    def set_date_of_birth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

    def set_gender(self, gender):
        self.__gender = gender

    def set_contact_number(self, contactNumber):
        self.__contactNumber = contactNumber

    def set_address(self, address):
        self.__address = address

    def get_patient_id(self):
        return self.__patientId

    def get_first_name(self):
        return self.__firstName

    def get_last_name(self):
        return self.__lastName

    def get_date_of_birth(self):
        return self.__dateOfBirth

    def get_gender(self):
        return self.__gender

    def get_contact_number(self):
        return self.__contactNumber

    def get_address(self):
        return self.__address

    def __str__(self) -> str:
        return (f"Patient ID: {self.__patientId}\nName: {self.__firstName} {self.__lastName}\nDOB: {self.__dateOfBirth}"
                f"\nGender: {self.__gender}\nContact: {self.__contactNumber}\nAddress: {self.__address}")


'''
patient = Patient(1, "John", "Doe", "2000-01-01", "Male", "1234567890", "123 Street, City")
print(patient)
'''
