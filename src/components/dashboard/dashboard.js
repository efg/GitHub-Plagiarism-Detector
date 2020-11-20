import React, { Component } from 'react';
import axios from 'axios';
import CourseView from './courseview/courseview';
import CheckView from './checkview/checkview';
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
            this.setState({courses: res.data['payload']})
      })
      .catch((error) => {
        console.log(error.response.data);
      });
    }

    async getChecks(course_id){
        console.log(course_id);
        await axios.get('http://127.0.0.1:5000/check/list?course_id=' + course_id)
        .then(res => {
            this.setState({displayChecks: true, checks: res.data['payload']})
            console.log(res.data['payload'])
        })
      .catch((error) => {
            console.log(error['message']);
        });
    }

    getDisplayComponent(){
        if(this.state.displayChecks)
            return <CheckView checks={this.state.checks} />;
        return <CourseView courses={this.state.courses} getChecks={this.getChecks}/>
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