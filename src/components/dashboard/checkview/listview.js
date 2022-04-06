import React, { Component } from "react";

import "../../dashboard/dashboard.css";
import StatsView from "./statsview";
import Heading from "../heading/heading";
import { MDBDataTable } from 'mdbreact';

class ListView extends Component {
  constructor(props) {
    super(props);
    this.setTableData();
  }

  setTableData() {
    this.dataObject = {columns: [{label: 'Run ID', field: 'runid', width: 150},
    {label: 'Date', field: 'date', sort: 'asc', width: 150},
    {label: 'Status', field: 'status', sort: 'asc', width: 150},
    {label: 'Report', field: 'report', sort: 'asc', width: 150}],
    rows: []};
    for (const row in this.props.tabRows) {
      this.dataObject.rows.push({'runid': this.props.tabRows[row].reportId, 
      'date': this.props.tabRows[row].date, 
      'status': this.props.tabRows[row].status ? "Complete" : "Incomplete", 
      'report': 
      this.props.tabRows [row].status && this.props.tabRows [row].report.includes("/") ? (
              <a href={this.props.tabRows[row].report} target="_blank" style={{color:"red"}}> View
          </a>
            ) : !this.props.tabRows[row].status ? (
              <div>Run Failed</div>
            ) : (
              <div></div>
            )
     
    });
    }
  }

  render() {
    return (
      <>
        <div className="container">
          <Heading
            title={"List of checks for assignment"}
            value={this.props.check_name}
            isBack={true}
            onBackPress={this.props.onBackPress}
          />

          <MDBDataTable
      scrollX
      striped
      responsive
      bordered
      data={this.dataObject}
    />
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
