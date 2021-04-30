import React, { Component } from "react";

class CheckModal extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div
        className="modal fade"
        id="exampleModal"
        tabIndex="-1"
        role="dialog"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div className="modal-dialog" role="document">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="exampleModalLabel">
                New Assignment
              </h5>
              <button
                type="button"
                className="close"
                data-dismiss="modal"
                aria-label="Close"
              >
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div className="modal-body p-4 p-sm-5">
              <div className="form-group">
                <label htmlFor="checkName">Name</label>
                <input
                  className="form-control"
                  type="text"
                  name="name"
                  id="checkName"
                  placeholder="Name for the Assignment"
                  onChange={this.props.handleChange}
                />
              </div>
              <div className="form-group">
                <label htmlFor="language">Language</label>
                <select
                  className="form-control"
                  name="language"
                  id="language"
                  placeholder="Select the language"
                  onChange={this.props.handleChange}
                >
                  <option value="" disabled selected>
                    Select the language
                  </option>
                  {this.props.languages &&
                    this.props.languages.map((h) => (
                      <option value={h}>{h}</option>
                    ))}
                </select>
              </div>
              <div className="form-group">
                <label htmlFor="startDate">Start Date</label>
                <input
                  className="form-control"
                  type="date"
                  name="start_date"
                  id="startDate"
                  placeholder="Start Date of the check"
                  onChange={this.props.handleChange}
                />
              </div>
              <div className="form-group">
                <label htmlFor="endDate">End Date</label>
                <input
                  className="form-control"
                  type="date"
                  name="end_date"
                  id="endDate"
                  placeholder="End Date of the check"
                  onChange={this.props.handleChange}
                />
              </div>
              <div className="form-group">
                <label htmlFor="interval">
                  Interval between two consecutive checks (in hrs.)
                </label>
                <input
                  className="form-control"
                  type="number"
                  min="0"
                  name="interval"
                  id="interval"
                  placeholder="Interval in hours"
                  onChange={this.props.handleChange}
                />
              </div>
              <div className="form-group">
                <label htmlFor="csvFile">CSV file of repository</label>
                <input
                  className="form-control"
                  type="file"
                  name="csvFile"
                  id="csvFile"
                  onChange={this.props.uploadFile}
                />
              </div>
              <div className="form-group">
                <label htmlFor="pathscsv">CSV file of file paths</label>
                <input
                  className="form-control"
                  type="file"
                  name="pathscsv"
                  id="pathscsv"
                  onChange={this.props.uploadPathsFile}
                />
              </div>
              <div className="form-group">
                {/* <label htmlFor="header">Is header row present?</label> */}
                <div display="inline">
                  Header row present ?
                  <input
                    type="checkbox"
                    name="header"
                    style={{
                      float: "right",
                      marginTop: "2px",
                      height: "20px",
                      width: "20px",
                    }}
                    size="4"
                    id="header"
                    onChange={this.props.handleChange}
                  />
                </div>
              </div>
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-secondary"
                data-dismiss="modal"
              >
                Close
              </button>
              <button
                type="button"
                className="btn btn-primary"
                data-dismiss="modal"
                onClick={this.props.handleSubmit}
              >
                Submit
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default CheckModal;
