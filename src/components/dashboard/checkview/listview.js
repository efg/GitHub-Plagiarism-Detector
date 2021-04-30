import React, { Component } from "react";

import "../../dashboard/dashboard.css";
import StatsView from "./statsview";
import Heading from "../heading/heading";

class ListView extends Component {
  constructor(props) {
    super(props);
    this.getTabRow = this.getTabRow.bind(this);
  }
  getTabRow(tabRow) {
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
      <tr key={tabRow.reportId}>
        <th scope="row">{tabRow.reportId}</th>
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
          <Heading
            title={"Asssignment"}
            value={this.props.check_name}
            isBack={true}
            onBackPress={this.props.onBackPress}
          />

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
        <StatsView
          check_id={this.props.check_id}
          onBackPress={this.props.onBackPress}
        />
      </>
    );
  }
}
export default ListView;
