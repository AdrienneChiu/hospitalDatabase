import json
import os

# Set up #

class HospitalDatabase:
    def __init__(self):
        self.patients = self.load_patients_from_file()

    def load_patients_from_file(self):
        if os.path.exists("patients.json"):
            with open("patients.json", "r") as file:
                return json.load(file) 
        return [] 

    def save_patients_to_file(self):
        with open("patients.json", "w") as file:
            json.dump(self.patients, file, indent=4)

    def check_in_patient(self, name, age, new_patient):
        patient_info = {
            "Name": name,
            "Age": age,
            "New Patient": new_patient
        }

        self.patients.append(patient_info)
        self.save_patients_to_file()
        print(f"Patient {name} checked in successfully.")

    def show_all_patients(self):
        if not self.patients:
            print("No patients have been checked in.")
        else:
            print("Patient List:")
            for idx, patient in enumerate(self.patients, start=1):
                print(f"{idx}. Name: {patient['Name']}, Age: {patient['Age']}, New Patient: {patient['New Patient']}")

# Main Program #
hospital_db = HospitalDatabase()

while True:
    print("\nHospital Database Menu: ")
    print("1. Check in New Patient")
    print("2. Show all Patients")
    print("3. Exit")

    choice = input("Enter option (1-3): ")

    if choice == '1':
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")
        new_patient_input = input("Is this a new patient? (yes/no): ").strip().lower()
        new_patient = True if new_patient_input == 'yes' else False
        hospital_db.check_in_patient(name, age, new_patient)

    elif choice == '2':
        hospital_db.show_all_patients()

    elif choice == '3':
        print("Exiting Program.")
        break

    else:
        print("Invalid choice, please choose again (1-3): ")
