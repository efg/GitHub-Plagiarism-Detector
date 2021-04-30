import React, { Component } from "react";

class Heading extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="card overflow-hidden mb-3">
        <div className="card-body p-2">
          <div className="row justify-content-between align-items-center pd">
            <div className="col">
              {this.props.title}: {this.props.value}
            </div>
            {this.props.isBack && (
              <div className="col">
                <button
                  type="button"
                  className="btn btn-falcon-primary float-right"
                  onClick={this.props.onBackPress}
                >
                  Back
                </button>
              </div>
            )}
          </div>
        </div>
      </div>
    );
  }
}

export default Heading;
