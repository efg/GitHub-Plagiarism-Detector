import axios from "axios";
import React, { Component } from "react";

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
    console.log("inside get MOSS", check_id);

    axios
      .get(`http://127.0.0.1:5000/check/similarities?check_id=${check_id}`)
      .then((res) => {
        console.log(res.data.payload);
        this.setState({ moss_info: res.data.payload });
        this.setState({ loading: false, key: this.getAKey(res.data.payload) });
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

  getTeamInfo(info, teamNo) {
    // for (const [key, val] of Object.entries(info)) {
    {
      console.log(info);
    }
    return (
      <div style={{ flexDirection: "column" }} className="col">
        {info.length > 0 &&
          info.map((obj, k) => (
            <div key={k}>{teamNo === 1 ? obj.dupl_code1 : obj.dupl_code2}</div>
          ))}
      </div>
      // }
    );
  }

  render() {
    if (this.props.loading) {
      return <div>Loading...</div>;
    }
    return (
      <>
        <div className="container">
          <div>
            <strong>Statistics</strong>
          </div>

          <div className="row justify-content-md-center">
            <div className="col-2">
              <label>Team Names</label>
              <div style={{ flexDirection: "column" }} className="row">
                <div className="row">
                  <div className="col">Team</div>
                  <div className="col">Report</div>
                </div>

                {this.state.moss_info &&
                  this.state.moss_info[this.state.key] &&
                  this.state.moss_info[this.state.key].map((info, k) =>
                    this.getTeamName(info, k)
                  )}
              </div>
            </div>
            <div className="col-5">
              <label> First Team </label>
              <div style={{ flexDirection: "row" }} className="row">
                {this.state.moss_info &&
                  Object.keys(this.state.moss_info).map((key, i) => (
                    <div>
                      <div className="col">{key}</div>
                      {this.getTeamInfo(this.state.moss_info[key], 1)}
                    </div>
                  ))}
              </div>
            </div>

            <div className="col-5">
              <label>Second Team</label>
              <div style={{ flexDirection: "row" }} className="row">
                {this.state.moss_info &&
                  Object.keys(this.state.moss_info).map((key, i) => (
                    <div>
                      <div className="col">{key}</div>
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
