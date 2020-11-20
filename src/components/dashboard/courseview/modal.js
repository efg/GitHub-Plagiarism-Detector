import React, { Component } from 'react';

export default class Modal extends React.Component {
    constructor(props){
        super(props);
        console.log(this.props);
    }
    
    getModalContent(){
        if (this.props.showModal){
            return(
                
                <div class="container">
                    <div class="row flex-center min-vh-50 py-6">
                        <div class="col-sm-10 col-md-8 col-lg-6 col-xl-5">
                            <div class="card">
                                <div class="card-header">
                                    <div class="col-auto fancy-font">
                                        Create a new Course
                                    </div>
                                </div>
                                <div class="card-body p-4 p-sm-5">
                                    <div class="form-group">
                                        <input class="form-control" type="text" name="name" id="inputName" placeholder="Course Name" onChange={this.props.handleChange} />
                                    </div>
                                    <div class="form-group">
                                        <button class="btn btn-primary btn-block mt-3" onClick={this.props.onSubmit}> Create </button>
                                    </div>
                                    <div class="form-group mb-0">
                                        <div class="row no-gutters">
                                            <button class="btn btn-danger btn-block mt-3" onClick={this.props.hideModalHandler}> Close </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
            </div>
            )
        }
        else{
            return null;
        }
    }
    render() {
        
      return (
        <div>
            {this.getModalContent()}
        </div>
        );
    }
  }