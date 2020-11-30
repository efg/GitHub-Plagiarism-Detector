import React, { Component } from 'react';

class CheckModal extends Component {
    constructor(props){
        super(props);
        console.log(props);
    }
    render() {   
      return (
        <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">New Check</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body p-4 p-sm-5">
                        <div class="form-group">
                            <label for="checkName">Name</label>
                            <input class="form-control" type="text" name="name" id="checkName" placeholder="Name for the Check" onChange={this.props.handleChange} />
                        </div>
                        <div class="form-group">
                            <label for="language">Language</label>
                            <select class="form-control" name="language" id="language" placeholder="Select the language" onChange={this.props.handleChange}>
                                <option value="" disabled selected>Select the language</option>
                                    {
                                    this.props.languages &&
                                    this.props.languages.map((h) => 
                                    (<option value={h}>{h}</option>))
                                    }
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="startDate">Start Date</label>
                            <input class="form-control" type="date" name="start_date" id="startDate" placeholder="Start Date of the check" onChange={this.props.handleChange} />
                        </div>
                        <div class="form-group">
                            <label for="endDate">End Date</label>
                            <input class="form-control" type="date" name="end_date" id="endDate" placeholder="End Date of the check" onChange={this.props.handleChange} />
                        </div>
                        <div class="form-group">
                            <label for="interval">Interval between two consecutive checks (in hrs.)</label>
                            <input class="form-control" type="number" min="0" name="interval" id="interval" placeholder="Interval in hours" onChange={this.props.handleChange} />
                        </div>
                        <div class="form-group">
                            <label for="csvFile">CSV file of submissions</label>
                            <input class="form-control" type="file" name="csvFile" id="csvFile" onChange={this.props.uploadFile} />
                        </div>
                        <div class="form-group">
                            <label for="pathscsv">CSV file of paths</label>
                            <input class="form-control" type="file" name="pathscsv" id="pathscsv" onChange={this.props.uploadPathsFile} />
                        </div>
                        <div class="form-group">
                            {/* <label for="header">Is header row present?</label> */}
                            <div display="inline">Header row present ?
                                <input type="checkbox" name="header" style={{"float":"right","marginTop":"2px", "height": "20px", "width": "20px"}} size="4" id="header" onChange={this.props.handleChange} />
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" data-dismiss="modal" onClick={this.props.handleSubmit}>Submit</button>
                    </div>
                </div>
            </div>
        </div>
    );
    }
}
export default CheckModal;