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
              {this.props.title}: {this.props.value} {this.props.isBack && !this.props.isEnable && "[PAUSED]"}
            </div>
            {this.props.isBack && (
              <div className="col">
                {!this.props.isEnable && (<button
                  type="button"
                  className="btn btn-success float-right"
                  onClick={() => {
                    this.props.onEnablePress(this.props.checkId);
                  }}
                >
                  Enable
                </button>)}
                {this.props.isEnable && (<button
                  type="button"
                  className="btn btn-danger float-right"
                  onClick={() => {
                    this.props.onDisablePress(this.props.checkId);
                  }}
                >
                  Disable
                </button>)}
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
