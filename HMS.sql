create database hms;
use hms;
CREATE TABLE Patient (
    patientId INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    dateOfBirth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    contactNumber VARCHAR(15) NOT NULL,
    address VARCHAR(100) NOT NULL
);
CREATE TABLE Doctor (
    doctorId INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    contactNumber VARCHAR(15) NOT NULL
)AUTO_INCREMENT = 101;

CREATE TABLE Appointment (
    appointmentId INT PRIMARY KEY AUTO_INCREMENT,
    patientId INT NOT NULL,
    doctorId INT NOT NULL,
    appointmentDate DATE NOT NULL,
    description TEXT,
    FOREIGN KEY (patientId) REFERENCES Patient(patientId),
    FOREIGN KEY (doctorId) REFERENCES Doctor(doctorId)
)AUTO_INCREMENT = 1001;

INSERT INTO Patient (firstName, lastName, dateOfBirth, gender, contactNumber, address) VALUES
('Raj', 'Patel', '1990-05-15', 'Male', '9876543210', 'No 2, Gandhi Street, Mumbai'),
('Priya', 'Sharma', '1985-08-20', 'Female', '8876543211', 'No 45, NSB Road, Trichy');
INSERT INTO Patient (firstName, lastName, dateOfBirth, gender, contactNumber, address) 
VALUES
('Amit', 'Verma', '1978-11-10', 'Male', '7765432112', 'Flat 12, Lake View Apartments, Delhi'),
('Ananya', 'Singh', '1995-03-25', 'Female', '6654321123', 'House No 32, MG Road, Kolkata'),
('Kiran', 'Kumar', '1980-09-08', 'Male', '5543211234', 'Block B, Skyline Tower, Bangalore');
    
INSERT INTO Doctor (firstName, lastName, specialization, contactNumber) VALUES
('Arun', 'Kumar', 'Cardiologist', '8776543212'),
('Sunita', 'Das', 'Dermatologist', '7876543213');
INSERT INTO Doctor (firstName, lastName, specialization, contactNumber) 
VALUES
('Rajesh', 'Patil', 'Orthopedic Surgeon', '6876543214'),
('Swati', 'Mehta', 'Ophthalmologist', '9876543215'),
('Vivek', 'Singh', 'Pediatrician', '8876543216');



INSERT INTO Appointment (patientId, doctorId, appointmentDate, description) VALUES
(1, 101, '2024-04-01', 'Routine checkup'),
(2, 102, '2024-04-02', 'Skin allergy consultation');

SELECT * FROM Patient;
SELECT * FROM Doctor;
SELECT * FROM Appointment;






