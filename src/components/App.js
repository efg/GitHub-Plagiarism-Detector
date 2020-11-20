import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import Login from './login/login';
import Dashboard from './dashboard/dashboard';

class App extends Component{
  render(){
    return(
      <BrowserRouter>
        <div>
            <Switch>
              <Route path="/index">
                <Login />
              </Route>
              <Route path="/dashboard">
                <Dashboard />
              </Route>
           </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
