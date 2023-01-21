import React from 'react'
import FaceIcon from '@mui/icons-material/Face';
import './PersonForm.css'

function PersonForm() {
  return (
    <div className='formContainer'>
      <div className='userImage'>
        <FaceIcon style={{fill:"black", fontSize: 150}}></FaceIcon>
      </div>
      <form className='formTemplate'>
        <fieldset>
          <label for="firstName">First Name </label>
          <input type="text" id="firstName"></input>
          <label for="lastName">Last Name </label>
          <input type="text" id="lastName"></input>

        </fieldset>
      </form>
    </div>
  )
}

export default PersonForm