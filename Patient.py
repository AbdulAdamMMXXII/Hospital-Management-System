class Patient:
    """Patient class"""
    
    # Initiates same family patients as an instance attrurbutes 
    family_patients = {}
    def __init__(self, first_name, surname, age, mobile, postcode, family_id=None):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
            family_id (int, optional): Family ID. Defaults set to none.
        """
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = []
        self.__family_id = family_id   # Family ID attribute
       

        # Initialise an empty dictionary for each instance
        self.__family_patients = {}

        if family_id is not None:
            self.set_family_id(family_id)
    
            
    def full_name(self) :
        """full name is first_name and surname"""
        return self.__first_name+" "+self.__surname
    
    # Get patients' family name
    def get_family_id(self):
        return self.__family_id
    
    def get_doctor(self) :
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def get_symptoms(self):
        return self.__symptoms if self.__symptoms is not None else []
    
    def print_symptoms(self):
        """prints all the symptoms"""
        if len(self.__symptoms) == 0:
            print("No symptoms entered for this patient! ")
        else:
            print("Symptoms:")
            for symptom in self.__symptoms:
                print(f"- {symptom}")

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
    
    # Add the patient to the family patients group
    def set_family_id(self, family_id):
        # Remove the existing family entry for the patient
        if self.__family_id in self.__family_patients:
            self.__family_patients[self.__family_id].remove(self)
    
        # Update the family ID and add the patient to the new family
        self.__family_id = family_id
        if family_id is not None:
            if family_id not in Patient.family_patients:
                Patient.family_patients[family_id] = []
            Patient.family_patients[family_id].append(self)

    # The assign_family_id method is used to group same family patients
    def assign_family_id(self, family_id):
        self.__family_id = family_id
        if family_id not in Patient.family_patients:
            Patient.family_patients[family_id] = []
        Patient.family_patients[family_id].append(self)

# View same family patients method is used to display the grouped patients
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
