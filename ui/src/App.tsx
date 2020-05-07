import 'bootstrap/dist/css/bootstrap.min.css';

import * as Validator from "email-validator";

import React, { useState } from "react";
import logo from "./logo.svg";
import Alert from "react-bootstrap/Alert";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./App.css";
import { render } from '@testing-library/react';

function Main() {

}

function App() {
  const validator = true;
  const [show, setShow] = useState(false);
  const [showLogin, setLogin] = useState(false);
  const handleSubmit = (event: any) => {
    const form = event.currentTarget;
    if (form.checkValidity() === false) {
      event.preventDefault();
      event.stopPropagation();
      setShow(true);
    }
    else {
      setLogin(validator || undefined);
    }
  };
  if (showLogin) {
    return (
      <div>
        <p>entered</p>
      </div>
    )
  }

  if (show)
    return (
      <div className="App">
        <header className="App-header">
          <h1>Please Login here.</h1>
          <Alert dismissible variant="danger" onClose={() => setShow(false)}>
            You have entered invalid login information.
          </Alert>
        </header>
      </div>
    );
  return (
    <div className="App">
      <header className="App-header">
          <p><strong>UMScheduler</strong></p>
          <Form noValidate validated={showLogin} onSubmit={handleSubmit}>
            <Form.Group controlId="formBasicEmail">
              <Form.Label>Email address</Form.Label>
              <Form.Control type="email" placeholder="Enter email" defaultValue="" />
              <Form.Text className="text-muted">
                We'll never share your email with anyone else.
              </Form.Text>
              <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
            </Form.Group>

            <Form.Group controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" placeholder="Password" defaultValue="" />
              <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
            </Form.Group>
            <Button variant="primary" type="submit" onClick={() => {Validator.validate("ab@bo.co"); setShow(true);}}>
              Submit
            </Button>
          </Form>
      </header>
    </div>
  );
}

export default App;
