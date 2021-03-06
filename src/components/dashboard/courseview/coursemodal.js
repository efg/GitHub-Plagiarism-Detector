import React, { Component } from 'react';

export default class CourseModal extends Component {
    render() {
        return (
            <div className="modal fade" id="exampleModal" tabIndex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div className="modal-dialog" role="document">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h5 className="modal-title" id="exampleModalLabel">New Course</h5>
                            <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div className="modal-body p-4 p-sm-5">
                            <div className="form-group">
                                <input className="form-control" type="text" name="name" id="inputName" placeholder="Course Name" onChange={this.props.handleChange} />
                            </div>
                        </div>
                        <div className="modal-footer">
                            <button type="button" className="btn btn-secondary" data-dismiss="modal">Close</button>
                            <button type="button" className="btn btn-primary" onClick={this.props.onSubmit}>Submit</button>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}