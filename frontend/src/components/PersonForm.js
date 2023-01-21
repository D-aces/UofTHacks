import React from 'react'
import FaceIcon from '@mui/icons-material/Face';
import './PersonForm.css'

function PersonForm() {
  return (
    <div className='formContainer'>
      <div className='userImage'>
        <FaceIcon style={{fill:"black", fontSize: 150}}></FaceIcon>
        <h4>This is you!</h4>
      </div>
      <form className='formTemplate'>
        <fieldset>
          <div className='inputField'>
          <label for="firstName">First Name </label>
          <input type="text" id="firstName"></input>
          </div>
          <div className='inputField'>
          <label for="lastName">Last Name </label>
          <input type="text" id="lastName"></input>
          </div>
          <div className='inputField'>
          <label for="dateofbirth">Date of birth </label>
          <input type="date" id="dateofbirth"></input>
          </div>
          <div className='inputField'>
          <label for="relationship">Type of relationship</label>
          <input type="date" id="relationship"></input>
          </div>
        </fieldset>
      </form>
    </div>
  )
}

export default PersonForm