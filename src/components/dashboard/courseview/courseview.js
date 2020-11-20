import React, { Component } from 'react';
import Card from '../card/card'; 

class CourseView extends Component{
    constructor(props){
        super(props);
        // console.log(props.courses);
        this.getCard = this.getCard.bind(this);
    }
    getCard(course){
        return  (
            <Card key={course.id}
                  name={course.name} 
                  infoAttr="Course Status"
                  info={(course.active === true)? "Active": "Not Active"}
                  onViewPress={this.props.getChecks}
            />);
    }
    render(){
        return(
            <div class="container">
                <div class="card overflow-hidden mb-3">
                    <div class="card-body p-2">
                        <div class="row justify-content-between align-items-center pd">
                            <div class="col">
                                Courses
                            </div>
                            <div class="col">
                                <button class="btn btn-falcon-primary float-right" onClick={this.handleSubmit}>New Course</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row mr-1">
                    {this.props.courses.map((course) => this.getCard(course))}
                </div>
            </div>
        );
    }
}
export default CourseView;