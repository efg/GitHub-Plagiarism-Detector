import React, { Component } from "react";
import axios from "axios";
import Card from "../card/card";
import CheckModal from "./checkmodal";
import languages from "../../../resources/languages.json";
import ListView from "./listview";

class CheckView extends Component {
  constructor(props) {
    super(props);
    // let result = [];
    this.state = {
      name: "",
      course_id: this.props.courseId,
      language: "",
      languages: [],
      start_date: "",
      end_date: "",
      interval: "",
      csvFile: null,
      pathscsv: null,
      header: "",
      tabView: false,
      tabData: []
    };
    this.getCard = this.getCard.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.uploadFile = this.uploadFile.bind(this);
    this.uploadPathsFile = this.uploadPathsFile.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.getReports = this.getReports.bind(this);
    this.hideTabView = this.hideTabView.bind(this);
    for (var i in languages) this.state.languages.push(i);
  }

  getCard(check) {
    return (
      <Card
        key={check.id}
        id={check.id} 
        name={check.name}
        infoAttr="Start Date"
        infoVal={check.start_date}
        attr="Language:"
        attrVal={check.language}
        onViewPress={this.getReports}
      />
    );
  }

  async getReports(check_id){
    console.log(check_id);
    await axios.get('http://127.0.0.1:5000/report/list?check_id=' + check_id)
        .then(res => {
            console.log(res.data['payload']);
            this.setState({tabView: true, tabData: res.data['payload']});
            // Report data (payload) is in format: date: "Sun, 01 Nov 2020 19:10:25 GMT" report: "www.mosslink.com" status: true
            // console.log(res.data['payload']);
        })
      .catch((error) => {
            console.log(error['message']);
        });

  }

  hideTabView(){
    this.setState({tabView: false, tabData: []});
  }

  handleChange = (event) => {
    const target = event.target;
    const value = target.value;
    const name = target.name;
    this.setState({
      [name]: value,
    });
    if (document.getElementById("header").checked) {
      this.setState({header: "True"});
    } else {
      this.setState({header: "False"});  
    }
    // this.state.csvFile = event.target.files[0];
    console.log(this.state);
  };

  uploadFile = (event) => {
    this.setState({
      csvFile: event.target.files[0],
      loaded: 0,
    });
  };

  uploadPathsFile = (event) => {
    this.setState({
      pathscsv: event.target.files[0],
      loaded: 0,
    });
  };

  handleSubmit = async () => {
    const data = new FormData();
    data.append("name", this.state.name);
    data.append("course_id", this.state.course_id);
    data.append("language", this.state.language);
    data.append("start_date", this.state.start_date);
    data.append("end_date", this.state.end_date);
    data.append("interval", this.state.interval);
    data.append("header", this.state.header);
    data.append("csvFile", this.state.csvFile);
    data.append("pathscsv", this.state.pathscsv);
    // console.log(data);

    await axios
      .post("http://127.0.0.1:5000/check/new", data)
      .then((res) => {
        this.props.getChecks(this.state.course_id);
      })
      .catch((error) => {
        console.log(error.response.data);
      });
  };

  render() {
    if(this.state.tabView){
      return(
        <ListView tabRows={this.state.tabData} onBackPress={this.hideTabView} />
      )
    }
    return (
      <div>
        <div class="container">
          <div class="card overflow-hidden mb-3">
            <div class="card-body p-2">
              <div class="row justify-content-between align-items-center pd">
                <div class="col">Checks</div>
                <div class="col">
                  <button
                    type="button"
                    class="btn btn-falcon-primary float-right"
                    data-toggle="modal"
                    data-target="#exampleModal"
                  >
                    New Check
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div class="row mr-1">
            {this.props.checks? (this.props.checks.map((check) => this.getCard(check))) : <p class="fancy-font">No Checks Found</p>}
          </div>
        </div>
        <CheckModal
          handleChange={this.handleChange}
          uploadFile={this.uploadFile}
          uploadPathsFile={this.uploadPathsFile}
          handleSubmit={this.handleSubmit}
          languages={this.state.languages}
        />
      </div>
    );
  }
}
export default CheckView;
