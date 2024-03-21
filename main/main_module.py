import entity.appointment as a

# from util.db_connection_util import DBConnection

from dao.hospital_service_impl import HospitalServiceImpl

hospital_service = HospitalServiceImpl()


def display_appointment_by_id():
    appointment_id = int(input("Enter the appointment id: "))
    appointment = hospital_service.getAppointmentById(appointment_id)
    print("Appointment by ID:")
    print(appointment)


def display_appointment_by_patient_id():
    patient_id = int(input("Enter the patient id: "))
    appointments_for_patient = hospital_service.getAppointmentsForPatient(patient_id)
    print("Appointments for Patient:\n", appointments_for_patient)


def display_appointment_by_doctor_id():
    doctor_id = int(input("Enter the doctor id: "))
    appointments_for_doctor = hospital_service.getAppointmentsForDoctor(doctor_id)
    print("Appointments for Doctor:\n", appointments_for_doctor)


def create_new_appointment():
    appointment_id = int(input("Enter the appointment id: "))
    patient_id = int(input("Enter the patient id: "))
    doctor_id = int(input("Enter the doctor id: "))
    appointment_date = input("Enter the appointment date: ")
    appointment_description = input("Enter the appointment description: ")
    new_appointment = a.Appointment(appointment_id, patient_id, doctor_id, appointment_date,
                                    appointment_description)
    success = hospital_service.scheduleAppointment(new_appointment)
    if success:
        print("Appointment scheduled successfully")
    else:
        print("Failed to schedule appointment")


def update_appointment():
    appointment_id = int(input("Enter the appointment id: "))
    patient_id = int(input("Enter the patient id: "))
    doctor_id = int(input("Enter the doctor id: "))
    appointment_date = input("Enter the appointment date: ")
    appointment_description = input("Enter the appointment description: ")
    updated_appointment = a.Appointment(appointment_id, patient_id, doctor_id, appointment_date,
                                        appointment_description)
    success = hospital_service.updateAppointment(updated_appointment)
    if success:
        print("Appointment updated successfully")
    else:
        print("Failed to update appointment")


def cancel_appointment():
    appointment_to_cancel_id = int(input("Enter the appointment id to cancel: "))
    success = hospital_service.cancelAppointment(appointment_to_cancel_id)
    if success:
        print("Appointment canceled successfully")
    else:
        print("Failed to cancel appointment")


class MainModule:

    @staticmethod
    def main():

        try:
            while True:
                print("_________________________________________")
                print("1. Display Appointment by AppointmentId\n2. Display Appointments by PatientId\n3. Display "
                      "Appointment by DoctorId\n4. Add new Appointment\n5. Update an Appointment\n6. Cancel an "
                      "appointment\n7. Quit")
                print("_________________________________________")
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    display_appointment_by_id()

                elif ch == 2:
                    display_appointment_by_patient_id()

                elif ch == 3:
                    display_appointment_by_doctor_id()

                elif ch == 4:
                    create_new_appointment()

                elif ch == 5:
                    update_appointment()

                elif ch == 6:
                    cancel_appointment()

                elif ch == 7:
                    break

                else:
                    print("Try Again, Enter valid option!!")

        except Exception as e:
            print("Error:", e)

        finally:
            print("Thank You!!")


if __name__ == "__main__":
    MainModule.main()
