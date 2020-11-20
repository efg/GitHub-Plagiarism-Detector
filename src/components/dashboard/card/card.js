import React, { Component } from 'react';
import './card.css';

class Card extends Component{
    constructor(props){
        super(props);
        this.state = {};
    }
    render(){
        return(
            <div class="col-sm-3 pr-0">
                <div class="card mb-3 shadow-sm">
                    <div class="card-body">
                        <h6 class="pb-0">{this.props.name}</h6>
                        <p class="card-text pb-1"><small class="text-muted">{this.props.infoAttr}: {this.props.info}</small></p>           
                    </div>
                    <div class="card-body fs--1 pt-0">
                        <div class="list-group-flush">
                            <div class="list-group-item bg-transparent d-flex justify-content-between px-0 py-1">
                                <p class="mb-0">{this.props.attr}</p>
                                <p class="mb-0">{this.props.attrCount}</p>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer bg-light p-0">
                    {this.props.onViewPress}
                        <button class="btn btn-sm btn-link btn-block py-2" onClick={() => this.props.onViewPress(this.props.key)}>View</button>
                    </div>
                </div>
            </div>
        );
    }
}

export default Card;