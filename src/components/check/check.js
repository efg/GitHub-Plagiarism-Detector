import React, { Component } from 'react';
import './check.css';
import languages from './languages.json';

class Check extends Component{
    constructor(props){
        let result = [];
        for(var i in languages)
            result.push(i);
        super(props);
        this.state = {
            name:"",
            course_id:"",
            language:"",
            languages: result,
            start_date:"",
            end_date:"",
            interval:"",
            csvFile:"",
            header:''
        };
    }
    handleChange=event=>{
        const target = event.target;
        const value = target.value;
        const name = target.name;
        this.setState({
          [name]: value
        });
        if (document.getElementById("header").checked) {
            this.state.header = 'True';
        } else {
            this.state.header = 'False';
        }
        console.log(this.state);
    }
    render(){
        return(
            <div class="container">
                <form class="new-check-form" encType="multipart/form-data">
                    <div class="row flex-center min-vh-50 py-6">
                        <div class="col-sm-10 col-md-8 col-lg-6 col-xl-5">
                            <div class="card">
                                    <div class="card-header">
                                        <div class="col-auto fancy-font" align="center">
                                            Create a new Check
                                        </div>
                                    </div>
                                <div class="card-body p-4 p-sm-5">
                                    <div class="form-group">
                                        <label for="checkName">Name</label>
                                        <input class="form-control" type="text" name="name" id="checkName" placeholder="Name for the Check" onChange={this.handleChange} />
                                    </div>
                                    <div class="form-group">
                                        <label for="courseID">Course ID</label>
                                        <input class="form-control" type="text" name="course_id" id="courseID" placeholder="Course ID" onChange={this.handleChange} />
                                    </div>
                                    <div class="form-group">
                                        <label for="language">Language</label>
                                        <select class="form-control" name="language" id="language" placeholder="Select the language" onChange={this.handleChange}>
                                            <option value="" disabled selected>Select the language</option>
                                                {
                                                this.state.languages &&
                                                this.state.languages.map((h) => 
                                                (<option value={h}>{h}</option>))
                                                }
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="startDate">Start Date</label>
                                        <input class="form-control" type="date" name="start_date" id="startDate" placeholder="Start Date of the check" onChange={this.handleChange} />
                                    </div>
                                    <div class="form-group">
                                        <label for="endDate">End Date</label>
                                        <input class="form-control" type="date" name="end_date" id="endDate" placeholder="End Date of the check" onChange={this.handleChange} />
                                    </div>
                                    <div class="form-group">
                                        <label for="interval">Interval between two consecutive checks (in hrs.)</label>
                                        <input class="form-control" type="number" min="0" name="interval" id="interval" placeholder="Interval in hours" onChange={this.handleChange} />
                                    </div>
                                    <div class="form-group">
                                        <label for="csvFile">CSV file of submissions</label>
                                        <input class="form-control" type="file" name="csvFile" id="csvFile" onChange={this.handleChange} />
                                    </div>
                                    <div class="form-group">
                                        {/* <label for="header">Is header row present?</label> */}
                                        <div display="inline">Header row present ?
                                            <input type="checkbox" name="header" style={{"float":"right","marginTop":"2px", "height": "20px", "width": "20px"}} size="4" id="header" onChange={this.handleChange} />
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <button class="btn btn-primary btn-block mt-3" type="submit">Create Check</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
            </div>  
        );
    }
}

export default Check;