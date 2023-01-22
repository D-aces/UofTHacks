import Navbar from './components/Navbar';
import './App.css';
import PersonForm from './components/PersonForm';
import PlusIcon from './components/PlusIcon';
import { useEffect, useState } from 'react';
import axios, { Axios } from 'axios';

function App() {

  const[people, setPeople] = useState({})

  const [personForm, setPersonForm] = useState([<PersonForm key={0} id={0} setPeople={setPeople}/>])

  useEffect(() => {console.log(people)}, [people]);

  let renderNewForm = (e) => {
    e.preventDefault()
    setPersonForm([...personForm, <PersonForm key={personForm.length} id={personForm.length} setPeople={setPeople} />])
  }

  const postFamily = () => {
    console.log("Pressed")
    axios.post('localhost:3000/success', 
      people
    )
  }

  return (
    <div className="App">
      <Navbar />
      <button className='submit-btn' onClick={postFamily}>
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
