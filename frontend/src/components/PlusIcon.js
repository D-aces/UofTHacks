import React from 'react'
import AddIcon from '@mui/icons-material/Add';

function PlusIcon() {
  return (
    <div className='imageContainer'>
    <div className='userImage'>
        <AddIcon style={{fill:"black", fontSize: 150}}></AddIcon>
        <h4>Add a person</h4>
    </div>
    </div>
    
  )
}

export default PlusIcon