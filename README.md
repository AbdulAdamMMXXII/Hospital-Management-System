# Hospital Management System (Python)

## Overview
This project is a console-based Hospital Management System developed in Python during my first year of undergraduate Computer Science studies (November 2023 – January 2024). It simulates core administrative and clinical workflows commonly found in real-world healthcare systems, with a strong emphasis on object-oriented design, data modelling, and system robustness.

The system enables an administrator to manage doctors and patients, assign and relocate patients, group family members, generate management reports, and persist data using file storage.

---

## Features
- Secure administrator login
- Doctor registration, viewing, updating, and deletion
- Patient viewing, assignment, relocation, and discharge
- Doctor–patient linking and workload tracking
- Family ID grouping for related patients
- Persistent data storage using file serialisation
- Management reporting with basic statistical visualisation
- Robust input validation and exception handling

---

## System Design
The application is structured using object-oriented programming principles:
- **Encapsulation** for secure data handling
- **Class-based modelling** for Doctors, Patients, and Admin roles
- **Separation of concerns** to improve readability and maintainability

Custom data structures are used to manage relationships between doctors, patients, appointments, and family groups.

---

## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- File Handling and Serialisation (`pickle`)
- Data Validation and Exception Handling
- Basic Data Visualisation (`matplotlib`)

---

## How to Run
1. Ensure Python 3 is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hospital-management-system.git
Navigate to the project directory:
cd hospital-management-system
Run the main application file:
python main.py

**Project Structure**  
├── Admin.py  
├── Doctor.py
<br>├── Patient.py
├── main.py
├── data/
│   └── patients_data.pkl\
└── README.md

---

**Learning Outcomes**
Applied object-oriented programming to a real-world domain
Designed and managed interrelated data models
Implemented defensive programming techniques
Gained experience with system-level problem decomposition
Developed foundational skills relevant to large-scale software systems

---

**Future Improvements**
Graphical User Interface (GUI)
Database-backed persistence (e.g., SQLite)
Role-based access control
Automated unit and integration testing
REST-based architecture for web deployment
