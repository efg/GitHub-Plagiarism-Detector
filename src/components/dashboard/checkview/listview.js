import React, { Component } from "react";

import "../../dashboard/dashboard.css";
import StatsView from "./statsview";

class ListView extends Component {
  constructor(props) {
    super(props);
    this.count = 0;
    this.getTabRow = this.getTabRow.bind(this);
    
  }
  getTabRow(tabRow) {
    this.count += 1;
    const report =
      tabRow.status && tabRow.report.includes("/") ? (
        <a href={tabRow.report} target="_blank">
          View
        </a>
      ) : !tabRow.status ? (
        <div>Run Failed</div>
      ) : (
        <div></div>
      );

    return (
      <tr key={this.count}>
        <th scope="row">{this.count}</th>
        <td>{tabRow.date}</td>
        <td>{tabRow.status ? "Complete" : "In Complete"}</td>
        <td>{report}</td>
      </tr>
    );
  }
  

  
  render() {

	
    return (
      <>
        <div className="container">
          <div className="card overflow-hidden mb-3">
            <div className="card-body p-2">
              <div className="row justify-content-between align-items-center pd">
                <div className="col">Checks</div>
                <div className="col">
                  <button
                    type="button"
                    className="btn btn-falcon-primary float-right"
                    onClick={this.props.onBackPress}
                  >
                    Back
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div className="row mr-1">
            <table className="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Date</th>
                  <th scope="col">Status</th>
                  <th scope="col">Report</th>
                </tr>
              </thead>
              <tbody>
                {this.props.tabRows ? (
                  this.props.tabRows.map((tabRow) => this.getTabRow(tabRow))
                ) : (
                  <p>No Reports Found</p>
                )}
              </tbody>
            </table>
          </div>
        </div>
        <StatsView check_id={this.props.check_id}/>
      </>
    );
  }
}
export default ListView;
