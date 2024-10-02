import React from 'react';
import Login from './pages/Login';
import Home from './pages/Home'
import Notfound from './pages/Notfound'
import Register from './pages/Register'
import ProtectedRoute from './components/ProtectedRoute'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';


const Logout = () => {
  localStorage.clear()
  return <Navigate to='/login' />
}


const RegisterAndLogout = () => {
  localStorage.clear()
  return <Register />
}



function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={
          <ProtectedRoute>
            <Home />
          </ProtectedRoute>
        } />
        <Route path='/login' element={<Login />} />
        <Route path='/logout' element={<Logout />} />
        <Route path='/register' element={<RegisterAndLogout />} />
        <Route path='*' element={<Notfound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
