import React, { Component } from 'react';

import Login from './login/login';
import Dashboard from './dashboard/dashboard';

class App extends Component{
  loggedIn(){
    if (localStorage.getItem('user_id') != null){
      return <Dashboard />;
    }
    return <Login />;
  }

  render(){
    return(
      this.loggedIn()
    );
  }
}

export default App;
