from Doctor import Doctor                       # Access to Doctor class
from Patient import Patient                     # acess to Patient class
import pickle                                   # Save data to and load from file
import matplotlib.pyplot as plt                 # print the management report on diagram

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    #Store patients' data into a file
    def save_patients_data(self, patients, filename):
        with open(filename, 'wb') as file:
            pickle.dump(patients, file)
        print('Data saved successfully in file.')

    #Load patients' data from a file
    def load_patients_data(self, filename):
        try:
            with open(filename, 'rb') as file:
                patients = pickle.load(file)
            print('Patients stored data loaded successfully.')
            return patients
        except FileNotFoundError:
            print(f'File {filename} not found. No data loaded.')
            return []
        
    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin
        print("Welcome to the Hospital Management System")

        while True:
            try:
                username = input('Please enter the username: ')
                password = input('Please enter the password: ')

            # check if the username and password match the registered ones
                if self.__username == username and self.__password == password:
                    return self.__username
                else:
                    raise ValueError('Incorrect username or password. Please try again.')
            except ValueError as e:
                print(e)


    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input('Plese enter the first name: ') 
        surname = input('Plese enter the surname: ') 
        speciality = input('Plese enter the speciality: ')

        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("\n-----Doctor Management-----")

        # menu
        print('Plese choose an operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input('Input: ')


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Plese enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    break
            new_doctor = Doctor(first_name, surname, speciality)
            doctors.append(new_doctor)
                                                         # ... to the list of doctors
            print('Doctor has been registered.')

        # View
        elif op == '2':
            print("\n-----List of Doctors-----")
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("\n-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Plese enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Plese choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase

            if op == 1:
                new_first_name = input('Plese enter the new first name:')
                doctors[index].set_first_name(new_first_name)
            elif op == 2:
                new_surname = input('Plese enter the new surname: ')
                doctors[index].set_surname(new_surname)
            elif op == 3:
                new_speciality = input('Plese enter the new speciality: ')
                doctors[index].set_speciality(new_speciality)

        # Delete
        elif op == '4':
            print("\n-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Plese enter the ID of the doctor to be deleted: ')
            try:
                doctor_index = int(doctor_index)-1
                if 0 <= doctor_index < len(doctors):
                    del doctors[doctor_index]
                    print('Doctor has been deleted successfully.')
                else:
                    print('Oops! Invalid docotor ID.')
            except ValueError:
                print('Invalid input. Please enter a valid number.')
               
            
            print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("\n-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("\n-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("\n-----Doctors Select-----")
        print('Plese select the doctor that fits these symptoms:')
        patients[patient_index].get_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors) #Display the doctor's full name in the list
        for index, doctor in enumerate(doctors):
            print(f'{index + 1:3}|{doctor.full_name():<30}|{doctor.get_speciality()}')

        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11Completed
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                self.view(patients)
                self.view(doctors)
                
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("\n-----Discharge Patient-----")
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            patient_index = int(patient_index)
            if 0 <= patient_index < len(patients):
                discharge_patient = patients.pop(patient_index)
                discharge_patients.append(discharge_patient)
                print(f'{discharge_patient.full_name()} has been discharged successfully.')
            else:
                print('Invalid patient ID.')
        except ValueError:
            print('Invalid input. Pease enter a valid patient ID number.')

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("\n-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        while True:
            print('Plese choose the field to be updated:')
            print(' 1 Username')
            print(' 2 Password')
            print(' 3 Address')
            op = int(input('Input: '))

            if op == 1:
                new_username = input('Plese enter the new username:')
                self.__username = new_username
                break

            elif op == 2:
                password = input('Plese enter the new password: ')
                # validate the password
                if password == input('Plese enter the new password again: '):
                    self.__password = password
                    break

            elif op == 3:
                new_address = input('Plese enter the new address: ')
                self.__address = new_address
                break

            else:
                print('Invalid operation chosen. Check your spelling!')
    
    # Grouping the same family together by Admin
    def assign_family_id(self, patients, family_id):
        """
        Assign a family ID to a group of patients
        Args:
            patients (list<Patient>): List of patients
            family_id (int): Family ID to be assigned
        """
        print("\n-----Assign Family ID-----")
        print('  ID|        Full Name           | Age |    Mobile     | Postcode ')
        self.view(patients)

        while True:
            patient_ids = input('Please enter the ID of patients (comma-separated) to assign the family ID: ')
            try:
                patient_ids = [int(id) - 1 for id in patient_ids.split(',')]
                # Check if the entered IDs are valid
                if all(0 <= id < len(patients) for id in patient_ids):
                    break
                else:
                    print('Invalid patient ID(s). Please enter valid IDs.')

            except ValueError:
                print('Invalid input. Please enter comma-separated numbers.')

        for patient_id in patient_ids:
            patients[patient_id].set_family_id(family_id)

        print(f'Family ID {family_id} assigned to selected patients.')

    # View same family grouped together 
    def view_same_family_patients(self):
        """
        View patients grouped by family ID
        """
        print("\n-----View Same Family Grouped Patients-----")
        for family_id, family_patients in Patient.family_patients.items():
            print(f'Family ID: {family_id}')
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            self.view(family_patients)
            print('\n')

    # Relocating patients from one doctor to another
    def relocate_patient(self, patients, doctors):
        """
        Relocate a patient from one doctor to another
        Args:
            patients (list<Patient>): List of patients
            doctors (list<Doctor>): List of doctors
        """
        print("\n-----Relocate Patient-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient index is the patient ID minus one (-1)
            patient_index = int(patient_index) - 1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return  # stop the procedures

        except ValueError:  # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return  # stop the procedures

        print("\n-----Doctors Select-----")
        print('Please select the new doctor for the patient:')
        # Display the doctor's full name in the list
        for index, doctor in enumerate(doctors):
            print(f'{index + 1:3}|{doctor.full_name():<30}|{doctor.get_speciality()}')

        new_doctor_index = input('Please enter the new doctor ID: ')

        try:
            # new_doctor_index is the doctor ID minus one (-1)
            new_doctor_index = int(new_doctor_index) - 1

            # check if the id is in the list of doctors
            if self.find_index(new_doctor_index, doctors) != False:

                # unlink the patient from the old doctor
                old_doctor_name = patients[patient_index].get_doctor()
                old_doctor = next((doc for doc in doctors if doc.full_name() == old_doctor_name), None)
                if old_doctor:
                    old_doctor.get_patients().remove(patients[patient_index])

                # link the patient to the new doctor
                patients[patient_index].link(doctors[new_doctor_index].full_name())
                doctors[new_doctor_index].add_patient(patients[patient_index])

                print('The patient has been relocated to the new doctor.')
                self.view(patients)
                self.view(doctors)

            # if the id is not in the list of doctors
            else:
                print('The new doctor id entered was not found.')

        except ValueError:  # the entered id could not be changed into an int
            print('The new doctor id entered is incorrect.')

    # Generate a management report for the hospital system
    def generate_management_report(self, doctors):
        """
        Generate a management report with various statistics
        Args:
            doctors (list<Doctor>): List of doctors
        """
        print("\n-----Management Report-----")
        print(f'Total number of doctors in the system: {len(doctors)}')

         # Bar chart data
        doctor_names = [doctor.full_name() for doctor in doctors]
        patients_count = [len(doctor.get_patients()) for doctor in doctors] 

        # Display bar chart
        plt.bar(doctor_names, patients_count)
        plt.xlabel('Doctor')
        plt.ylabel('Total Number of Patients')
        plt.title('Total Number of Patients per Doctor')
        plt.show()

        for doctor in doctors:
            patients_count = len(doctor.get_patients())  # Total number of patients per doctor
            appointments_count = sum(len(appointments) for appointments in doctor.get_appointments().values())

            print(f"\nDoctor: {doctor.full_name()}")
            print(f'Total number of patients: {patients_count}')
            print(f'Total number of appointments per month: {appointments_count}')

        illness_type_count = {}
        # Loop through each doctor and patient to count illness types
        for doctor in doctors:
            for patient in doctor.get_patients():
                for symptom in patient.get_symptoms():
                    if symptom not in illness_type_count:
                        illness_type_count[symptom] = 1
                    else:
                        illness_type_count[symptom] += 1

        # Total number of patients based on the illness type
        print("\nTotal number of patients based on illness type:")
        for symptom, count in illness_type_count.items():
            print(f"{symptom}: {count}")






    # The End of the Admin Class