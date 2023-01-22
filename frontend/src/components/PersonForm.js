import React, { useEffect } from 'react'
import FaceIcon from '@mui/icons-material/Face';
import './PersonForm.css'
import { useState } from 'react';

function PersonForm(props) {
  const id = props.id;
  const setPeople = props.setPeople;

  const [person, setPerson] = useState({})

  useEffect (() => {
    let newPeople = {};
    newPeople[id] = person;
    setPeople(p => ({...p, ...newPeople}));
  }, [person, id, setPeople]);


  return (
    <div className='formContainer'>
      <div className='userImage'>
        <FaceIcon style={{ fill: "black", fontSize: 150 }}></FaceIcon>
        <h4> {person.firstName ? 'This is ' + person.firstName : '???'}</h4>
      </div>
      <form className='htmlFormTemplate'>
        <fieldset>
          <div className='inputField'>
            <label htmlFor="firstName">First Name </label>
            <input type="text" id="firstName" value={person.firstName} onChange={e => setPerson(p => ({...p, firstName: e.target.value}))}/>
          </div>
          <div className='inputField'>
            <label htmlFor="lastName">Last Name </label>
            <input type="text" id="lastName" value={person.lastName} onChange={e => setPerson(p => ({...p, lastName: e.target.value}))}/>
          </div>
          <div className='inputField'>
            <label htmlFor="dateofbirth">Date of birth </label>
            <input type="date" id="dateofbirth" value={person.dob} onChange={e => setPerson(p => ({...p,dob: e.target.value}))}/>
          </div>
          <div className='inputField'>
            <label htmlFor="relationship">Type of relationship</label>
            <select id="relationship" name="relationship"value={person.relationship} onChange={e => setPerson(p => ({...p,relationship: e.target.value}))}>
              <option defaultValue>  </option>
              <option value="father">Father</option>
              <option value="mother">Mother</option>
              <option value="sibling">Sibling</option>
              <option value="spouse">Spouse</option>
            </select>
          </div>
        </fieldset>
      </form>
    </div>
  )
}

export default PersonForm