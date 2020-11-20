import React, { Component } from 'react';
import axios from 'axios';
import Course from './course/course';
// import './dashboard.css';
class Dashboard extends Component{
    constructor(props){
        super(props);
        this.state = {
            displayChecks: false,
            courses: [],
            checks: [],
        };
    }
    async componentDidMount() {
        const user_id = localStorage.getItem('user_id');
        const admin = localStorage.getItem('admin');
        await axios.get('http://127.0.0.1:5000/course/list?user_id=' + user_id + '&admin=' + admin)
        .then(res => {
            console.log(localStorage.getItem('admin'))
            console.log(res.data['payload'])
            this.setState({courses: res.data['payload']})
      })
      .catch((error) => {
        console.log(error.response.data);
      });
    }
    getDisplayComponent(){
        if(this.state.displayChecks)
            return <h1>Checks</h1>;
        return <Course courses={this.state.courses} />
    }
    render(){
        let secondComponent = this.getDisplayComponent(); 
        return(
            <div class="container">
                {secondComponent}
            </div>
        );
    }
}
export default Dashboard;   