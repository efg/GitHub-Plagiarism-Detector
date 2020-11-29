import React, { Component } from 'react';

export default class CourseModal extends Component {
    render() {   
      return (
        <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">New Course</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body p-4 p-sm-5">
                        <div class="form-group">
                            <input class="form-control" type="text" name="name" id="inputName" placeholder="Course Name" onChange={this.props.handleChange} />
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" onClick={this.props.onSubmit}>Submit</button>
                    </div>
                </div>
            </div>
        </div>
    );
    }
}