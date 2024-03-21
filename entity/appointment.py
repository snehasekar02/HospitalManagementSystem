class Appointment:
    def __init__(self, appointmentId, patientId, doctorId, appointmentDate, description):
        self.__appointmentId = appointmentId
        self.__patientId = patientId
        self.__doctorId = doctorId
        self.__appointmentDate = appointmentDate
        self.__description = description

    def set_appointment_id(self, appointmentId):
        self.__appointmentId = appointmentId

    def set_patient_id(self, patientId):
        self.__patientId = patientId

    def set_doctor_id(self, doctorId):
        self.__doctorId = doctorId

    def set_appointment_date(self, appointmentDate):
        self.__appointmentDate = appointmentDate

    def set_description(self, description):
        self.__description = description

    def get_appointment_id(self):
        return self.__appointmentId

    def get_patient_id(self):
        return self.__patientId

    def get_doctor_id(self):
        return self.__doctorId

    def get_appointment_date(self):
        return self.__appointmentDate

    def get_description(self):
        return self.__description

    def __str__(self) -> str:
        return (f"Appointment ID: {self.__appointmentId}\nPatient ID: {self.__patientId}\nDoctor ID: {self.__doctorId}"
                f"\nDate: {self.__appointmentDate}\nDescription: {self.__description}")


'''
appointment = Appointment(1001, 1, 101, "2024-03-20", "Regular Checkup")
print(appointment)
'''
