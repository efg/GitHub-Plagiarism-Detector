import axios from "axios";
import React, { Component } from "react";
import ReactTooltip from "react-tooltip";
import Heading from "../heading/heading";
import { MDBDataTable } from 'mdbreact';

class StatsView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      moss_info: {},
      loading: true,
      key: -1,
    };    
  }

  get_MOSS_info(check_id) {
    axios
      .get(`/check/similarities?check_id=${check_id}`)
      .then((res) => {
        this.setState({ moss_info: res.data.payload });
        this.setState({ loading: false });
        this.setSimilarityData();
      })
      .catch((error) => {
        console.log(error);
      });
  }

  componentDidMount() {
    this.get_MOSS_info(this.props.check_id);
  }

  /**
   *
   * @param {*} info: contains moss report info
   * @param {*} k: key
   * @returns  unordered pair of team names
   */
  getTeamName(info, k) {
    return (
      <div key={k}>
        <div className="row">
          <div className="col">{info.repo1}</div>
          <div className="col">{info.repo2}</div>
        </div>
      </div>
    );
  }
  /**
   *
   * @param {*} info : moss info
   * @returns a report id
   */
  getAKey(info) {
    for (const report_id in info) return report_id;
  }

  setSimilarityData() {
    const dataObject = {columns: [{label: 'Run ID', field: 'runid', sort: 'desc', width: 100},
    {label: 'Repo A', field: 'repo_a', sort: 'asc', width: 100},
    {label: 'Repo B', field: 'repo_b', sort: 'asc', width: 100},
    {label: 'Shared Code Repo A to B', field: 'share_a_to_b', sort: 'asc', width: 100},
    {label: 'Shared Code Repo B to A', field: 'share_b_to_a', sort: 'asc', width: 100},
    {label: 'Similarity Jump Repo A to B', field: 'jump_a_to_b', sort: 'asc', width: 100},
    {label: 'Similarity Jump Repo B to A', field: 'jump_b_to_a', sort: 'asc', width: 100}],
    rows: []};
    let allKeys = Object.keys(this.state.moss_info);
    for (const key in allKeys) {
      for (const run in this.state.moss_info[allKeys[key]]) {
        dataObject.rows.push({'runid': allKeys[key], 
        'repo_a': this.state.moss_info[allKeys[key]][run]['repo1'],
        'repo_b':this.state.moss_info[allKeys[key]][run]['repo2'], 
        'share_a_to_b': `${this.state.moss_info[allKeys[key]][run]['dupl_code1']}%`,
      'share_b_to_a': `${this.state.moss_info[allKeys[key]][run]['dupl_code2']}%`, 
      'jump_a_to_b': this.state.moss_info[allKeys[key]][run]['similarity_jump1'] != 'N/A' ? 
      `${this.state.moss_info[allKeys[key]][run]['similarity_jump1']}%` : 
      `${this.state.moss_info[allKeys[key]][run]['similarity_jump1']}`,
      'jump_b_to_a': this.state.moss_info[allKeys[key]][run]['similarity_jump2'] != 'N/A' ? 
      `${this.state.moss_info[allKeys[key]][run]['similarity_jump2']}%` : 
      `${this.state.moss_info[allKeys[key]][run]['similarity_jump2']}`,
    
    });
      }
    }

    // Sort the rows in descending order of runid.
    dataObject.rows.sort((a, b) => parseFloat(b['runid']) - parseFloat(a['runid']));
  this.setState({moss_info: dataObject});
  }

  getTeamInfo(info, teamNo) {
    return (
      <div style={{ flexDirection: "column" }} className="col">
        {info.length > 0 &&
          info.map((obj, k) => (
            <div
              style={
                //hightlight high code similarity extracted from MOSS report
                {
                  backgroundColor:
                    teamNo === 1
                      ? obj.dupl_code1 > 70
                        ? "yellow"
                        : ""
                      : obj.dupl_code2 > 70
                      ? "yellow"
                      : "",
                }
              }
              key={k}
            >
              {obj.dupl_code1}% &emsp;
              {obj.dupl_code2}%
            </div>
          ))}
      </div>
      // }
    );
  }

  render() {
    if (this.props.loading) {
      return <div>Loading...</div>;
    }
    if (!this.state.moss_info){
      return (
        <div>No MOSS info found!</div>
      )
    }
    return (
      <>
        <div id="stats-view" className="container">
          <Heading
            title={"Statistics"}
            value={"In the table below we are comparing each repo with every other repo and calculating the similarity percentage from Repo A to B and Repo B to A. We are also calculating the similarity percentage jump from the last run to current run. You will notice that the first run has similarity percentage jump as N/A since we do not have a previous run to compare with."}
            isBack={true}
            onBackPress={this.props.onBackPress}
          />

          </div>
        <MDBDataTable
      scrollX
      responsive
      striped
      bordered
      order={['runid', 'desc']}
      data={this.state.moss_info}
    />
      </>
    );
  }
}

export default StatsView;
