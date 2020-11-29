import React, { Component } from "react";
class ListView extends Component{
    constructor(props) {
        super(props);
        this.state = {
            count: 0,
        };
        this.getTabRows = this.getTabRows.bind(this);
    };
    getTabRows(tabRow){
        this.setState({count: this.state.count+1});
        return(
            <tr key={this.state.count}>
                <th scope="row">{this.state.count}</th>
                <td>{tabRow.date}</td>
                <td>{tabRow.status}</td>
                <td>{tabRow.report}</td>
            </tr>
        )
    }
    render(){
        return(
            <div class="container">
                <div class="card overflow-hidden mb-3">
                    <div class="card-body p-2">
                        <div class="row justify-content-between align-items-center pd">
                            <div class="col">Checks</div>
                            <div class="col">
                                <button
                                    type="button"
                                    class="btn btn-falcon-primary float-right"
                                >
                                    Back
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row mr-1">
                    <table class="table">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Date</th>
                                <th scope="col">Status</th>
                                <th scope="col">Report</th>
                            </tr>
                        </thead>
                        <tbody>
                            {this.props.tabRows.map((tabRow) => getTabRow(tabRow))}
                        </tbody>
                    </table>
                </div>
            </div>
        );
    }
}