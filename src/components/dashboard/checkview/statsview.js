import axios from "axios";
import React, { Component } from "react";
import ReactTooltip from "react-tooltip";
import Heading from "../heading/heading";

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
        // console.log(res.data.payload);
        this.setState({ moss_info: res.data.payload });
        this.setState({ loading: false, key: this.getAKey(res.data.payload) });
      })
      .catch((error) => {
        // console.log(error);
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
              {teamNo === 1 ? obj.dupl_code1 : obj.dupl_code2}
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
            value={""}
            isBack={true}
            onBackPress={this.props.onBackPress}
          />
          {/* <div
            style={{margin: "1rem"}}>
            <h4><strong>Statistics</strong></h4>
          </div> */}

          <div className="row justify-content-md-center">
            <div className="col-2">
              <label>
                <strong>Team Names</strong>
              </label>
              <div style={{ flexDirection: "column" }} className="row">
                <div className="row">
                  <div style={{ color: "#5f6368" }} className="col">
                    <b>Team</b>
                  </div>
                  <div style={{ color: "#5f6368" }} className="col">
                    <b>Report#</b>
                  </div>
                </div>

                {this.state.moss_info &&
                  this.state.moss_info[this.state.key] &&
                  this.state.moss_info[this.state.key].map((info, k) =>
                    this.getTeamName(info, k)
                  )}
              </div>
            </div>
            <div className="col-5">
              <label>
                <strong>
                  Shared Code
                  <a data-tip="% of first team’s code that is shared with second team">
                    ❓
                  </a>
                  <ReactTooltip place="top" type="info" effect="solid" />
                </strong>
              </label>
              <div style={{ flexDirection: "row" }} className="row">
                {this.state.moss_info &&
                  Object.keys(this.state.moss_info).map((key, i) => (
                    <div>
                      <div style={{ color: "#5f6368" }} className="col">
                        <b>{key}</b>
                      </div>
                      {this.getTeamInfo(this.state.moss_info[key], 1)}
                    </div>
                  ))}
              </div>
            </div>

            <div className="col-5">
              <label>
                <strong>
                  Shared Code
                  <a data-tip="% of second team’s code that is shared with first team">
                    ❓
                  </a>
                  <ReactTooltip place="top" type="info" effect="solid" />
                </strong>
              </label>
              <div style={{ flexDirection: "row" }} className="row">
                {this.state.moss_info &&
                  Object.keys(this.state.moss_info).map((key, i) => (
                    <div>
                      <div style={{ color: "#5f6368" }} className="col">
                        <b>{key}</b>
                      </div>
                      {this.getTeamInfo(this.state.moss_info[key], 2)}
                    </div>
                  ))}
              </div>
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default StatsView;
