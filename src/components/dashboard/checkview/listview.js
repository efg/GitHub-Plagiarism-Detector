import React, { Component } from "react";
class ListView extends Component{
    constructor(props) {
        super(props);
        this.count = 0;
        this.getTabRow = this.getTabRow.bind(this);
    };
    getTabRow(tabRow){
        this.count += 1;
        const report = (tabRow.status)? <a href={tabRow.report} target="_blank">View</a> : <div></div>;
        if(tabRow.status){

        }
        return(
            <tr key={this.count}>
                <th scope="row">{this.count}</th>
                <td>{tabRow.date}</td>
                <td>{(tabRow.status)? "Complete": "InComplete"}</td>
                <td>{report}</td>
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
                                    onClick={this.props.onBackPress}
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
                            {this.props.tabRows? (this.props.tabRows.map((tabRow) => this.getTabRow(tabRow))) : <p>No Reports Found</p>}
                        </tbody>
                    </table>
                </div>
            </div>
        );
    }
}
export default ListView;