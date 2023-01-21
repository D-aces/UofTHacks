import React from 'react'
import './Navbar.css'
import MenuIcon from '@mui/icons-material/Menu';
import Stack from '@mui/material/Stack';

function Navbar() {
  return (
    <div className="navigation">
        <div className='logo'>
            <h2>FamTree</h2>
        </div>
        <a href="#">
        <div className='menu'>
            <MenuIcon style={{color:"white", display:"inline"}} />
        </div>
        </a>
    </div>
  )
}

export default Navbar