import Navbar from './components/Navbar';
import './App.css';
import PersonForm from './components/PersonForm';
import PlusIcon from './components/PlusIcon';
import { useState } from 'react';

function App() {

  const [personForm, setPersonForm] = useState([<PersonForm key={0} />])

  let renderNewForm = (e) => {
    e.preventDefault()
    setPersonForm([...personForm, <PersonForm key={personForm.length} />])
  }


  return (
    <div className="App">
      <Navbar />
      <button className='submit-btn'>
        <p>Generate Family Tree</p>
      </button>
      <h1>Add your family!</h1>
      <div className='mainPage'>
      {personForm}
      <PlusIcon onClick={renderNewForm} />
    </div>
    </div>
  );
}

export default App;
