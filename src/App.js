import './App.css';
// import React, { useState } from "react";
// import { Button, Paper, TextField } from '@mui/material';

import React, { useState } from "react";
import { Button, TextField, Grid, FormControl, FormControlLabel, FormLabel, Radio, RadioGroup, Select, MenuItem, Slider} from '@mui/material';
import Form from './Form';


function App() {
  return (
    <div style={{padding: "50px"}}>
      <Form id="Form_Container"></Form>
    </div>
  );
}

export default App;
