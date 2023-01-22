import React from 'react'
import { useState } from 'react'

const useForm = () =>  {
  const [state, setState] = state({})

  const handleChange = e => {
    setState(state => ({...state, [e.target.name]: e.target.value}))
  }

  return [state, handleChange]

}

export default useForm