
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './Components/Header';
import Cards from './Components/Cards';
import './App.css'
import AddStudentForm from './Components/AddStudent';
import StudentDetail from './Components/StudentDetail';
import { Container, Row, Col, Image, Card } from 'react-bootstrap';
import { useState } from 'react';


function App() {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = (term) => {
    setSearchTerm(term);
  };

  return (
    <Router>
      <Header onSearch={handleSearch} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/students" element={<Cards searchTerm={searchTerm} />} />
        <Route path="/students/add-student" element={<AddStudentForm />} />
        <Route path="/student/:studentId" element={<StudentDetail />} />
      </Routes>
    </Router>
  );
}


function Home() {
  return (
    <Container className="home-container">
      <Row className="justify-content-center">
        <Col md={8}>
          <Card className="home-card">
            <Card.Body>
              <h2 className="home-text">Welcome to the School Management System</h2>
              <Image src="https://via.placeholder.com/800x400" fluid className="home-image" />
              <Card.Text className="home-description">
                This project is designed to help manage student information efficiently. You can add, view, edit, and delete student details with ease. Follow the guidelines below to get started:
              </Card.Text>
              <ul className="home-guidelines">
                <li>Navigate to the -Students- page to view all students.</li>
                <li>Use the -Add Student- form to add new students.</li>
                <li>Click on a student s -Information- button to view and edit their details.</li>
                <li>Use the -Delete- button to remove a student from the system.</li>
              </ul>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default App;
