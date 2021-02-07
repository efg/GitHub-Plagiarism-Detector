import React, { Component } from 'react';

import Login from './login/login';
import Dashboard from './dashboard/dashboard';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      'userId': localStorage.getItem('user_id')
    }
    this.onLogIn = this.onLogIn.bind(this);
    this.onLogOut = this.onLogOut.bind(this);
  }
  onLogIn(userId) {
    this.setState({ userId: userId });
  }
  onLogOut() {
    localStorage.removeItem('user_id');
    localStorage.removeItem('admin');
    this.setState({ userId: null });
  }
  render() {
    if (this.state.userId == null)
      return <Login onLogIn={this.onLogIn} />;
    else
      return <Dashboard onLogOut={this.onLogOut} />;
  }
}

export default App;
