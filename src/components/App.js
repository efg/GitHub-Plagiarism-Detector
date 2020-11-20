import React, { Component } from 'react';

import Login from './login/login';
import Dashboard from './dashboard/dashboard';
import Check from './check/check';

class App extends Component{
  loggedIn(){
    if (localStorage.getItem('user_id') != null){
      return <Dashboard />;
    }
    return <Login />;
  }

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
      // this.loggedIn()
    );
  }
}

export default App;
