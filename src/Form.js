import React, { useState } from "react";
import { Button, TextField, Paper } from '@mui/material';

const defaultValues = {
    name: ""
};

const Form = () => {
    const [textValue, setTextValue] = useState("");
    const onTextChange = (e) => setTextValue(e.target.value);
    const callApi = () => {
        return fetch("https://c4spuy5dwf.execute-api.us-east-1.amazonaws.com/dev", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                sms: textValue
            })
        })
            .then(response => response.json())
            .then(data => alert(data.body.result));
    };
    const handleSubmit = () => {
        // make a post request to the following api https://c4spuy5dwf.execute-api.us-east-1.amazonaws.com/dev with the following body: {"sms": "test"}
        callApi();
        setTextValue("");
    };

    return (
        <Paper>
            <h1>Spam or Ham?</h1>
            <p>Enter a sample sms message to detect if it is spam or ham!</p>
            <TextField
                onChange={onTextChange}
                value={textValue}
                label={"Enter SMS Message"}
                multiline
                rows={20}
                style={{ width: "100%" }}
            />
            <Button variant="contained" onClick={handleSubmit} style={{ width: "100%" }}>Submit</Button>
        </Paper>
    );
};
export default Form;