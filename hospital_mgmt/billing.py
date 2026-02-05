class Billing:
    def __init__(self, bill_id, patient, amount):
        self.bill_id = bill_id
        self.patient = patient
        self.amount = amount
        self.paid = False

    def pay_bill(self):
        self.paid = True

    def __str__(self):
        status = 'Paid' if self.paid else 'Unpaid'
        return (f"Billing[ID={self.bill_id}, Patient={self.patient.name}, Amount={self.amount}, Status={status}]")
