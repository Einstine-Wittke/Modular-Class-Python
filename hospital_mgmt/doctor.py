class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"Doctor[ID={self.doctor_id}, Name={self.name}, Specialty={self.specialty}]"
