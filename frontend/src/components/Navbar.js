import React from 'react'
import './Navbar.css'
import MenuIcon from '@mui/icons-material/Menu';
import SpaIcon from '@mui/icons-material/Spa';
import Stack from '@mui/material/Stack';

function Navbar() {
  return (
    <div className="navigation">
        <div className='logo'>
            <Stack spacing={1} direction={"row"}>
                <h2>FamTree</h2>
                <SpaIcon style={{fill:"white", alignSelf:"center"}}></SpaIcon>
            </Stack>
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