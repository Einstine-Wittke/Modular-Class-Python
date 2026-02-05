
from patient import Patient
from doctor import Doctor
from appointment import Appointment
from billing import Billing
from hospital import Hospital


def main():
    hospital = Hospital()

    # Add patients
    p1 = Patient(1, "Alice Smith", 30, "F")
    p2 = Patient(2, "Bob Brown", 45, "M")
    hospital.add_patient(p1)
    hospital.add_patient(p2)

    # Add doctors
    d1 = Doctor(1, "Dr. John Doe", "Cardiology")
    d2 = Doctor(2, "Dr. Jane Lee", "Neurology")
    hospital.add_doctor(d1)
    hospital.add_doctor(d2)

    # Add appointments
    a1 = Appointment(1, p1, d1, "2026-02-10", "10:00 AM")
    a2 = Appointment(2, p2, d2, "2026-02-11", "11:00 AM")
    hospital.add_appointment(a1)
    hospital.add_appointment(a2)

    # Add billings
    b1 = Billing(1, p1, 500)
    b2 = Billing(2, p2, 300)
    hospital.add_billing(b1)
    hospital.add_billing(b2)

    print("\nAll Patients:")
    for patient in hospital.list_patients():
        print(patient)

    print("\nAll Doctors:")
    for doctor in hospital.list_doctors():
        print(doctor)

    print("\nAll Appointments:")
    for appt in hospital.list_appointments():
        print(appt)

    print("\nAll Billings:")
    for bill in hospital.list_billings():
        print(bill)

    # Demonstrate search
    print("\nFind Patient with ID 1:")
    print(hospital.find_patient(1))

    print("\nRemove Patient with ID 2 and list again:")
    hospital.remove_patient(2)
    for patient in hospital.list_patients():
        print(patient)

    # Demonstrate paying a bill
    print("\nPaying Bill ID 1...")
    bill = hospital.find_billing(1)
    if bill:
        bill.pay_bill()
    print(bill)

if __name__ == "__main__":
    main()
