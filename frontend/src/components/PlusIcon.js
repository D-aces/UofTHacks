import React from 'react'
import AddIcon from '@mui/icons-material/Add';
import { color } from '@mui/system';

function PlusIcon(props) {
  return (
    <button className='imageContainer' onClick={props.onClick}>
    <div className='userImage'>
        <AddIcon style={{fill:"black", fontSize: 150}}></AddIcon>
        <h4>Add a person</h4>
    </div>
    </button>
  )
}

export default PlusIcon