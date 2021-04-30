import React, { Component } from "react";
import "./card.css";
const moment = require("moment");
class Card extends Component {
  render() {
    return (
      <div className="col-sm-3 pr-0">
        <div className="card mb-3 shadow-sm">
          <div className="card-body">
            <h6 className="pb-0">{this.props.name}</h6>
            <p className="card-text pb-1">
              <small className="text-muted">
                {this.props.infoAttr}:{" "}
                {moment(this.props.infoVal).format("MM/DD/YYYY")}
              </small>
            </p>
          </div>
          <div className="card-body fs--1 pt-0">
            <div className="list-group-flush">
              <div className="list-group-item bg-transparent d-flex justify-content-between px-0 py-1">
                <p className="card-text p-0 card-text-muted">
                  {this.props.attr} {this.props.attrVal}
                </p>
              </div>
            </div>
          </div>
          <div className="card-footer bg-light p-0">
            <button
              className="btn btn-sm btn-link"
              onClick={() => this.props.onViewPress(this.props.id, this.props.name)}
            >
              View
            </button>
            <button
              className="btn btn-sm btn-link"
              onClick={() =>
                this.props.onDeletePress(this.props.id, this.props.course_id)
              }
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    );
  }
}

export default Card;
