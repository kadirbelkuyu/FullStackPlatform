import React, { useState, useEffect,useParams } from 'react';
import axios from 'axios';


function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    axios.get('http://localhost:5000/hello')
      .then(response => {
        setMessage(response?.data?.message);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>{message}</p>
      </header>
    </div>
  );
}

export default App;
