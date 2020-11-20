import React, { Component } from 'react';
import './check.css';
import axios from 'axios';
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
            csvFile:null,
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
        // this.state.csvFile = event.target.files[0];
        console.log(this.state);
    }

    uploadFile=event=>{
        this.setState({
            csvFile: event.target.files[0],
            loaded: 0,
          })
    }


    handleSubmit = async ()=>{

        const data = new FormData()
        data.append('name', this.state.name)
        data.append('course_id', this.state.course_id)
        data.append('language', this.state.language)
        data.append('start_date', this.state.start_date)
        data.append('end_date', this.state.end_date)
        data.append('interval', this.state.interval)
        data.append('header', this.state.header)
        data.append('file', this.state.csvFile)


    await axios.post('http://127.0.0.1:5000/check/new', data)   
    .then(res => {
        // Redirect to next page here
        console.log("Success");
        // useHistory().push("/dashboard");
      })
      .catch((error) => {
        console.log(error.response.data);
        // useHistory().push("/dashboard");
      });

    }
    render(){
        return(
            <div class="container">
                {/* <form class="new-check-form"> */}
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
                                        <input class="form-control" type="file" name="csvFile" id="csvFile" onChange={this.uploadFile} />
                                    </div>
                                    <div class="form-group">
                                        {/* <label for="header">Is header row present?</label> */}
                                        <div display="inline">Header row present ?
                                            <input type="checkbox" name="header" style={{"float":"right","marginTop":"2px", "height": "20px", "width": "20px"}} size="4" id="header" onChange={this.handleChange} />
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <button class="btn btn-primary btn-block mt-3" onClick={this.handleSubmit}>Create Check</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                {/* </form> */}
            </div>  
        );
    }
}

export default Check;