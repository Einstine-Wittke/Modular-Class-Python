from patient import Patient
from doctor import Doctor
from appointment import Appointment
from billing import Billing

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.billings = []

    # Patient management
    def add_patient(self, patient):
        self.patients.append(patient)
    def list_patients(self):
        return self.patients
    def find_patient(self, patient_id):
        for p in self.patients:
            if p.patient_id == patient_id:
                return p
        return None
    def remove_patient(self, patient_id):
        self.patients = [p for p in self.patients if p.patient_id != patient_id]

    # Doctor management
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
    def list_doctors(self):
        return self.doctors
    def find_doctor(self, doctor_id):
        for d in self.doctors:
            if d.doctor_id == doctor_id:
                return d
        return None
    def remove_doctor(self, doctor_id):
        self.doctors = [d for d in self.doctors if d.doctor_id != doctor_id]

    # Appointment management
    def add_appointment(self, appointment):
        self.appointments.append(appointment)
    def list_appointments(self):
        return self.appointments
    def find_appointment(self, appointment_id):
        for a in self.appointments:
            if a.appointment_id == appointment_id:
                return a
        return None
    def remove_appointment(self, appointment_id):
        self.appointments = [a for a in self.appointments if a.appointment_id != appointment_id]

    # Billing management
    def add_billing(self, billing):
        self.billings.append(billing)
    def list_billings(self):
        return self.billings
    def find_billing(self, bill_id):
        for b in self.billings:
            if b.bill_id == bill_id:
                return b
        return None
    def remove_billing(self, bill_id):
        self.billings = [b for b in self.billings if b.bill_id != bill_id]
