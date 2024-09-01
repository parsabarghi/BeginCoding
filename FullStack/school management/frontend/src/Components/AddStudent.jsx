import  { useState } from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import './AddStudent.css';
import { toast, ToastContainer } from 'react-toastify';

export default function AddStudentForm() {
    const [studentData, setStudentData] = useState({
        full_name: '',
        age: '',
        class_type: '',
    });

    const [formErrors, setFormErrors] = useState({
        full_name: '',
        age: '',
        class_type: '',
    });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setStudentData({ ...studentData, [name]: value });
        setFormErrors({ ...formErrors, [name]: '' }); // Clear any previous errors
    };

    const validateForm = () => {
        let isValid = true;
        const newErrors = {};

        if (!studentData.full_name.trim()) {
            newErrors.full_name = 'Full Name is required';
            isValid = false;
        }

        if (!studentData.age || isNaN(studentData.age) || studentData.age <= 0) {
            newErrors.age = 'Age must be a positive number';
            isValid = false;
        }

        if (!studentData.class_type.trim()) {
            newErrors.class_type = 'Class Type is required';
            isValid = false;
        }

        setFormErrors(newErrors);
        return isValid;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!validateForm()) {
            return; // Don't submit if form is invalid
        }

        try {
            const response = await fetch('http://127.0.0.1:5000/students', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(studentData),
            });

            if (response.ok) {
                console.log('Student added successfully!');
                toast.success('Student Added successfully!')
            } else {
                console.error('Error adding student:', response.statusText);
                toast.error('Error adding student, please try again!')
            }
        } catch (error) {
            console.error('Error fetching data:', error);
            toast.error('Error fetching data!')
        }
    };

    return (
        <div className='add-student-container'>
            <h2 className='h2-add-student'>Add New Student</h2>
            <Form onSubmit={handleSubmit}>
                <Form.Group className='mb-3' controlId="full_name">
                    <Form.Label>Full Name</Form.Label>
                    <Form.Control
                        type="text"
                        name="full_name"
                        value={studentData.full_name}
                        onChange={handleInputChange}
                    />
                    <Form.Text className="text-danger">{formErrors.full_name}</Form.Text>
                </Form.Group>

                <Form.Group className='mb-3' controlId="age">
                    <Form.Label>Age</Form.Label>
                    <Form.Control
                        type="number"
                        name="age"
                        value={studentData.age}
                        onChange={handleInputChange}
                    />
                    <Form.Text className="text-danger">{formErrors.age}</Form.Text>
                </Form.Group>

                <Form.Group className='mb-3' controlId="class_type">
                    <Form.Label>Class Type</Form.Label>
                    <Form.Control
                        type="text"
                        name="class_type"
                        value={studentData.class_type}
                        onChange={handleInputChange}
                    />
                    <Form.Text className="text-danger">{formErrors.class_type}</Form.Text>
                </Form.Group>

                <Button className="add-student-submit-button" variant="primary" type="submit">
                    Add Student
                </Button>
            </Form>
            <ToastContainer position="bottom-right" autoClose={3000} />
        </div>
    );
}
