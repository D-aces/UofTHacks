import Navbar from './components/Navbar';
import './App.css';
import PersonForm from './components/PersonForm';
import PlusIcon from './components/PlusIcon';
import { useState } from 'react';


function App() {
  return (
    <div className="App">
      <Navbar />
      <div className='mainPage'>
      <PersonForm />
      <PlusIcon />
    </div>
    </div>
  );
}

export default App;
