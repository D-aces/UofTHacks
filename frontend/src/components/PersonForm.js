import React, { useEffect } from 'react'
import FaceIcon from '@mui/icons-material/Face';
import './PersonForm.css'
import { useState, useRef } from 'react';

function PersonForm() {
  const [personRelation, setRelation] = useState('you')
  const renderCount = useRef(0)

  useEffect (() => {
  renderCount.current = renderCount.current+1
})

  return (
    <div className='formContainer'>
      <div className='userImage'>
        <FaceIcon style={{ fill: "black", fontSize: 150 }}></FaceIcon>
        <h4>This is {personRelation}!</h4>
      </div>
      <form className='htmlFormTemplate'>
        <fieldset>
          <div className='inputField'>
            <label htmlFor="firstName">First Name </label>
            <input type="text" id="firstName"></input>
          </div>
          <div className='inputField'>
            <label htmlFor="lastName">Last Name </label>
            <input type="text" id="lastName"></input>
          </div>
          <div className='inputField'>
            <label htmlFor="dateofbirth">Date of birth </label>
            <input type="date" id="dateofbirth"></input>
          </div>
          <div className='inputField'>
            <label htmlFor="relationship">Type of relationship</label>
            <select id="relationship" name="relationship">
              <option disabled defaultValue> -- select an option -- </option>
              <option value="father">Myself</option>
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