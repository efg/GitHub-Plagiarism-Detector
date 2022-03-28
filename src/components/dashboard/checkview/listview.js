import React, { Component } from "react";

import "../../dashboard/dashboard.css";
import StatsView from "./statsview";
import Heading from "../heading/heading";
import { MDBDataTable } from 'mdbreact';
import { MDBBtn } from "mdbreact";

class ListView extends Component {
  constructor(props) {
    super(props);
    this.dataObject = {columns: [{label: 'Run ID', field: 'runid', sort: 'desc', width: 150},
    {label: 'Date', field: 'date', sort: 'asc', width: 150},
    {label: 'Status', field: 'status', sort: 'asc', width: 150},
    {label: 'Report', field: 'report', sort: 'asc', width: 150}],
    rows: []};
    this.state = {
      tabRows: this.props.tabRows
    };  
    this.setTableData();
    // this.setTableData = this.setTableData.bind(this);
  }
  // getTabRow(tabRow) {
  //   const report =
  //     tabRow.status && tabRow.report.includes("/") ? (
  //       <a href={tabRow.report} target="_blank">
  //         View
  //       </a>
  //     ) : !tabRow.status ? (
  //       <div>Run Failed</div>
  //     ) : (
  //       <div></div>
  //     );

  //   return (
  //     <tr key={tabRow.reportId}>
  //       <th scope="row">{tabRow.reportId}</th>
  //       <td>{tabRow.date}</td>
  //       <td>{tabRow.status ? "Complete" : "In Complete"}</td>
  //       <td>{report}</td>
  //     </tr>
  //   );
  // }

  setTableData() {
    for (const row in this.state.tabRows) {
      this.dataObject.rows.push({'runid': this.state.tabRows[row].reportId, 'date': this.state.tabRows[row].date, 
      'status': this.state.tabRows[row].status ? "Complete" : "In Complete", 
      'report': 
      this.state.tabRows[row].status && this.state.tabRows[row].report.includes("/") ? (
              <a href={this.state.tabRows[row].report} target="_blank" style={{color:"red"}}> View
          </a>
            ) : !this.state.tabRows[row].status ? (
              <div>Run Failed</div>
            ) : (
              <div></div>
            )
     
    });
    }
    this.setState({tabRows: this.dataObject});
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

          {/* <div className="row mr-1">
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
          </div> */}
          <MDBDataTable
      scrollX
      striped
      bordered
      order={['runid', 'desc']}
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
