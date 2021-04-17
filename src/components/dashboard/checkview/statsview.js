import axios from "axios";
import React, { Component } from "react";


class StatsView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      moss_info: [],
      loading: true,
    };
    this.getTableRow = this.getTableRow.bind(this);
    
  }

  get_MOSS_info(check_id) {
    console.log("inside get MOSS", check_id);

    axios
      .get(`http://127.0.0.1:5000/check/similarities?check_id=${check_id}`)
      .then((res) => {
        console.log(res.data.payload);
        this.setState({ moss_info: res.data.payload });
        this.setState({ loading: false });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  componentDidMount() {
    this.get_MOSS_info(this.props.check_id);
  }

  getTableRow(info){
    return (
        <tr>
            <td>{info.report_id}</td>
            <td>{info.repo1}</td>
            <td>{info.dupl_code1}</td>
            <td>{info.repo2}</td>
            <td>{info.dupl_code2}</td> 
        </tr>
    )
  }

  render() {
    if (this.props.loading){
        return (
            <div>Loading...</div>
        )
    }
    return (
      <>
        <div className="container">
            <div>
                <strong>Stats</strong>
            </div>
            <div className="stats-view">
                {!this.state.moss_info && (
                    <div>No Stats to show!</div>
                )}
                {this.state.moss_info &&
                    this.state.moss_info.length > 0 &&
                    <table className="table">
                        <thead>
                            <tr>
                                <th>Report ID</th>
                                <th>Team 1</th>
                                <th>Similarity</th>
                                <th>Team 2</th>
                                <th>Similarity 2</th>
                            </tr>
                        </thead>
                        <tbody>
                            {this.state.moss_info.map((info, k) => (
                                this.getTableRow(info)
                            ))}
                        </tbody>
                    </table>
                    }
                    {
                        // <div>
                        //     <div className="row">
                        //         <div>{info.report_id}</div>
                        //         <div>{info.repo1}</div>
                        //         <div>{info.dupl_code1}</div>
                        //         <div>{info.repo2}</div>
                        //         <div>{info.dupl_code2}</div>   
                        //     </div>

                        // </div>
                    }
            </div>
        </div>
      </>
    );
  }
}

export default StatsView;
