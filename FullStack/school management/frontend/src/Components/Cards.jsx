import { useState, useEffect } from 'react';
import { Card, Button, Form, Container, Row, Col } from 'react-bootstrap';
import Image from './img_avatar.png';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import './Cards.css';
import StudentDetail from './StudentDetail';
import { Link } from 'react-router-dom';

export default function Cards({ searchTerm }) {
    const [students, setStudents] = useState([]);
    const [selectedStudentId, setSelectedStudentId] = useState(null);

    useEffect(() => {
        fetch("http://127.0.0.1:5000/students")
            .then(response => response.json())
            .then(data => setStudents(data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    const handleDelete = (id) => {
        fetch(`http://127.0.0.1:5000/student/${id}`, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
        })
            .then(response => {
                if (response.status === 200) {
                    setStudents(prevStudents => prevStudents.filter(student => student.id !== id));
                    toast.success('Student deleted successfully!');
                } else {
                    toast.error('Error deleting student. Please try again later.');
                }
            })
            .catch(error => {
                console.error('Error deleting student:', error);
                toast.error('An unexpected error occurred. Please try again later.');
            });
    };

    const handleShowInfo = (id) => {
        setSelectedStudentId(id);
    };

    const filteredStudents = students.filter(student =>
        student.full_name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <Container className="cards-container">
            <Row className="justify-content-center">
                {filteredStudents.map((student) => (
                    <Col md={4} key={student.id}>
                        <Card className='Card'>
                            <Card.Img variant="top" src={Image} />
                            <Card.Body>
                                <Card.Title>{student.full_name}</Card.Title>
                                <Card.Text>
                                    Age: {student.age}<br />
                                    Class Type: {student.class_type}<br />
                                    Card Number: {student.card ? student.card.card_number : 'No card assigned'}
                                </Card.Text>
                                <Link to={`/student/${student.id}`}>
                                    <Button
                                        className='card-information-button'
                                        variant="primary"
                                        onClick={() => handleShowInfo(student.id)}
                                    >
                                        Information
                                    </Button>
                                </Link>
                                <Button
                                    className='card-delete-button'
                                    variant="outline-danger"
                                    onClick={() => handleDelete(student.id)}
                                >
                                    Delete
                                </Button>
                            </Card.Body>
                        </Card>
                    </Col>
                ))}
            </Row>
            {selectedStudentId && (
                <StudentDetail studentId={selectedStudentId} />
            )}
            <ToastContainer position="bottom-right" autoClose={3000} />
        </Container>
    );
}
