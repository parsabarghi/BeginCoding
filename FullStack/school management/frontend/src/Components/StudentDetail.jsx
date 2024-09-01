import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Form, Button, Spinner, Container, Row, Col, Card } from 'react-bootstrap';
import './StudentDetail.css'; // Import the CSS file

export default function StudentDetail() {
  const { studentId } = useParams();
  const [studentData, setStudentData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({
    full_name: '',
    age: '',
    class_type: ''
  });

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      try {
        const response = await fetch(`http://127.0.0.1:5000/student/${studentId}`);
        if (response.status === 200) {
          const data = await response.json();
          setStudentData(data[0]);
          setFormData({
            full_name: data[0].full_name,
            age: data[0].age,
            class_type: data[0].class_type
          });
        }
      } catch (error) {
        console.error('Error fetching student data:', error);
      } finally {
        setIsLoading(false);
      }
    };

    if (studentId) {
      fetchData();
    }
  }, [studentId]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleEditClick = () => {
    setIsEditing(true);
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`http://127.0.0.1:5000/student/${studentId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });
      if (response.status === 200) {
        const updatedData = await response.json();
        setStudentData(updatedData[0]);
        setIsEditing(false);
      } else {
        console.error('Error updating student data');
      }
    } catch (error) {
      console.error('Error updating student data:', error);
    }
  };

  return (
    <Container className="student-detail-container">
      {isLoading ? (
        <Spinner animation="border" role="status">
          <span className="sr-only">Loading...</span>
        </Spinner>
      ) : (
        studentData && (
          <Row className="justify-content-center">
            <Col md={6}>
              <Card className="student-detail-card">
                <Card.Body>
                  <h2>Student Information</h2>
                  {isEditing ? (
                    <Form onSubmit={handleFormSubmit}>
                      <Form.Group controlId="formFullName">
                        <Form.Label>Name</Form.Label>
                        <Form.Control
                          type="text"
                          name="full_name"
                          value={formData.full_name}
                          onChange={handleInputChange}
                        />
                      </Form.Group>
                      <Form.Group controlId="formAge">
                        <Form.Label>Age</Form.Label>
                        <Form.Control
                          type="number"
                          name="age"
                          value={formData.age}
                          onChange={handleInputChange}
                        />
                      </Form.Group>
                      <Form.Group controlId="formClassType">
                        <Form.Label>Class Type</Form.Label>
                        <Form.Control
                          type="text"
                          name="class_type"
                          value={formData.class_type}
                          onChange={handleInputChange}
                        />
                      </Form.Group>
                      <Button variant="primary" type="submit">
                        Save
                      </Button>
                    </Form>
                  ) : (
                    <div>
                      <p>Name: {studentData.full_name}</p>
                      <p>Age: {studentData.age}</p>
                      <p>Class Type: {studentData.class_type}</p>
                      <Button variant="primary" onClick={handleEditClick}>
                        Edit
                      </Button>
                    </div>
                  )}
                </Card.Body>
              </Card>
            </Col>
          </Row>
        )
      )}
    </Container>
  );
}
