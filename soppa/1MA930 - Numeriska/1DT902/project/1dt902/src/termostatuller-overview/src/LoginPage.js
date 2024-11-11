import "./LoginPage.css"
import NB from "./NB";
import React, { useState } from 'react';

export default function LoginPage(props) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(username);
        console.log(password);

        // Send the login credentials to the server using the fetch function
        fetch(`https://termostatuller.billenius.com/sql?verify=true&username=${username}&password=${password}`, {
            method: 'GET',
        })
            .then((response) => {
                // Check if the login was successful
                if (response.ok) {
                    // Run the updateLoginState function with a value of true
                    props.updateLoginState(true, username, password);
                } else {
                    // Handle the login failure
                    console.error('Login failed');
                }
            })
            .catch((error) => {
                // Handle any errors that occurred during the request
                console.error(error);
            });
    };
    return (
        <>
            <NB signin={true}/>
            <div className="Auth-form-container">
                <form className="Auth-form" onClick={handleSubmit}>
                    <div className="Auth-form-content">
                        <h3 className="Auth-form-title">Login</h3>
                        <div className="form-group mt-3">
                            <label>Username</label>
                            <input
                                value={username}
                                onChange={(event) => setUsername(event.target.value)}
                                type="email"
                                className="form-control mt-1"
                                placeholder="Enter email"

                            />
                        </div>
                        <div className="form-group mt-3">
                            <label>Password</label>
                            <input
                                value={password}
                                onChange={(event) => setPassword(event.target.value)}
                                type="password"
                                className="form-control mt-1"
                                placeholder="Enter password"
                            />
                        </div>
                        <div className="d-grid gap-2 mt-3">
                            <button type="submit" className="btn btn-primary">
                                Login
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </>
    )
}
