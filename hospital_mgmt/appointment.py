class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def __str__(self):
        return (f"Appointment[ID={self.appointment_id}, Patient={self.patient.name}, "
                f"Doctor={self.doctor.name}, Date={self.date}, Time={self.time}]")
