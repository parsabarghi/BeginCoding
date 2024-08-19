import { useState, useEffect } from 'react'
import PlcList from './plc_list'
import './App.css'
import PlcFrom from './PlcForm';

function App() {
  const [plc, setPlc] = useState([]);

  useEffect(()=> {
    fetchPLCs();
  }, []);

  const fetchPLCs = async () => {
    const response = fetch("http://127.0.0.1:5000/Lists");
    const data = await response.json();
    setPlc(data.plc);
    console.log(data.plc);
  }

  return (
    <>
      <PlcList PLCs={plc} />
      <PlcFrom />
    </>
  );
}

export default App
