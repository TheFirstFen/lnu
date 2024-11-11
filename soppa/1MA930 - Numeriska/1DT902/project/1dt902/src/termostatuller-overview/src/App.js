import './App.css';
import './cards.css'
import React from 'react';
import { Helmet } from 'react-helmet';
import LoginPage from './LoginPage'; // Import the login page component
import MainPage from './MainPage';

export default class App extends React.Component {
  state = {
    isLoggedIn: false, // Set the initial login state to false
    username: "",
    password: "",
  }

  // Method to update the login state
  updateLoginState = (isLoggedIn, username, password) => {
    this.setState({ isLoggedIn, username, password });
  }

  render() {
    return (
      <>
        <Helmet>
          <meta charSet="utf-8" />
          <title>Termostatuller</title>
        </Helmet>
        {/* Check if the user is logged in */}
        {this.state.isLoggedIn ? (
          // If the user is logged in, render the existing content
          <React.Fragment>
            <MainPage loginCreds={this.state}/>
          </React.Fragment>
        ) : (
          // If the user is not logged in, render the login page
          <LoginPage updateLoginState={this.updateLoginState} />
        )}
      </>
    );
  }
}
