import React, { Component } from 'react';
import Card from '../card/card'; 
import Modal from './modal';
import axios from 'axios';

class CourseView extends Component{
    constructor(props){
        super(props);
        // console.log(props.courses);
        this.getCard = this.getCard.bind(this);
        this.onFormSubmit = this.onFormSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.state = {
            showModal : false,
            name: "",
            user_id: localStorage.getItem('user_id')
        };
    }

    

    showModalHandler = (event) =>{
        this.setState({showModal:true});
    }

    hideModalHandler = (event) =>{
        this.setState({showModal:false});
    }
      
    getCard(course){
        return  (
            <Card id={course.id}
                  name={course.name} 
                  infoAttr="Course Status"
                  infoVal={(course.active === true)? "Active": "Not Active"}
                  onViewPress={this.props.getChecks}
            />);
    }
    onFormSubmit= async ()=>{
        // console.log(this.state);
        this.hideModalHandler();
        const name = this.state.name;
        const user_id = this.state.user_id;

       await axios.post('http://127.0.0.1:5000/course/new', { name, user_id })
      .then(res => {
        window.location.reload();
        
      })
      .catch((error) => {
        console.log(error.message);
        // useHistory().push("/dashboard");
      });
    }

    handleChange=event=>{
        const target = event.target;
        const value = target.value;
        const name = target.name;
        this.setState({
          [name]: value
        });
    }
    render(){
        return(
            <div>
            <div class="container">
                <div class="card overflow-hidden mb-3">
                    <div class="card-body p-2">
                        <div class="row justify-content-between align-items-center pd">
                            <div class="col">
                                Courses
                            </div>
                            <div class="col">
                                <button class="btn btn-falcon-primary float-right" onClick={this.showModalHandler}>New Course</button>
                                
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row mr-1">
                    {this.props.courses.map((course) => this.getCard(course))}
                </div>
                
            </div>
            <div>
            <Modal showModal={this.state.showModal} hideModalHandler={this.hideModalHandler} onSubmit={this.onFormSubmit} handleChange={this.handleChange}></Modal>
            </div>
            </div>
        );
    }
}
export default CourseView;