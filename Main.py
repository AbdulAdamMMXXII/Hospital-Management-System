# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def get_valid_option():
    " Get a valid option for the menu option from the user "
    while True:
        try:
            op = int(input('Option: '))
            if 1 <= op <= 6:
                return str(op)
            else:
                print('Invalid option. Please enter a number between 1 and 6. ')
        except ValueError:
            print('That was invalid inputs. Please enter a number.')
    
def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []
    
    # keep trying to login till the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            print('Login was successful.')
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('\nPlese choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6- View same family grouped patients')
        print(' 7- Relocate patients')
        print(' 8- Request a mangement report')
        print(' 9- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            admin.doctor_management(doctors)
            # Save patients' data after doctor management
            admin.save_patients_data(patients, 'patients_data.pkl') 

        elif op == '2':
            admin.discharge(patients,discharged_patients)
             # Save patients' data after discharge
            admin.save_patients_data(patients, 'patients_data.pkl')

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    admin.discharge(patients, discharged_patients)
                    # Save patients' data after additional discharge
                    admin.save_patients_data(patients, 'patients_data.pkl')
                    break

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            admin.view_discharge(discharged_patients)
            # Load patients' data from the file
            patients = admin.load_patients_data('patients_data.pkl')

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)
            # Save patients' data after assigning a doctor
            admin.save_patients_data(patients, 'patients_data.pkl')

        elif op == '5':
            # 5- Update admin details
            admin.update_details()
        
        elif op == '6':
            print('\n--------Manage same family patients--------')
            print('1- Group same family patients ')
            print('2- View same family patients ')
            op = input('Please enter your choice: ')

            if op == '1':
                # Group family with the same surname in the family list
                family_id = input('Please enter the family ID: ')
                admin.assign_family_id(patients, family_id)

            # view same family grouped together
            elif op == '2':
                admin.view_same_family_patients()
                
            else:
                print("That was invalid choice. Please try again. ")

        elif op == '7':
            # 7- Relocate patients
            admin.relocate_patient(patients, doctors)
            # Save patients' data after relocating a patient
            admin.save_patients_data(patients, 'patients_data.pkl')

        elif op == '8':
            # 8- Request a management report
            admin.generate_management_report(doctors)

            # 9 - Quit program
        elif op == '9':
            # Save patients' data before quitting
            admin.save_patients_data(patients, 'patients_data.pkl')
            print('The program has been terminated.')
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()