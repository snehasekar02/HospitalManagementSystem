from abc import ABC, abstractmethod
from typing import List
from entity.appointment import Appointment


class IHospitalService(ABC):
    @abstractmethod
    def getAppointmentById(self, appointmentId: int) -> Appointment | None:
        pass

    @abstractmethod
    def getAppointmentsForPatient(self, patientId: int) -> List[str]:
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self, doctorId: int) -> List[str]:
        pass

    @abstractmethod
    def scheduleAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def updateAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def cancelAppointment(self, appointmentId: int) -> bool:
        pass
