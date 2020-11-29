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
            selectedCourse: -1,
            courses: [],
            checks: [],
        };
        this.getChecks = this.getChecks.bind(this);
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
        await axios.get('http://127.0.0.1:5000/check/list?course_id=' + course_id)
        .then(res => {
            this.setState({selectedCourse: course_id, displayChecks: true, checks: res.data['payload']});
            console.log(res.data['payload']);
        })
      .catch((error) => {
            console.log(error['message']);
        });
    };

    getDisplayComponent(){
        if(this.state.displayChecks)
            return <CheckView courseId={this.state.selectedCourse} getChecks={this.getChecks} checks={this.state.checks} />;
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