import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import Login from './login/login';
import Dashboard from './dashboard/dashboard';
import Check from './check/check';

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
              <Route path="/check">
                <Check />
              </Route>
           </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
