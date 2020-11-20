import React, { Component } from 'react';
import Card from '../card/card'; 

class CheckView extends Component{
    constructor(props){
        super(props);
        this.getCard = this.getCard.bind(this);
    }
    getCard(check){
        return  (
            <Card key={check.id}
                  name={check.name} 
                  infoAttr="Start Date"
                  infoVal={check.start_date}
                  attr="Language"
                  attrVal={check.language}
                //   onViewPress={this.getChecks}
            />);
    }
    render(){
        return(
            <div class="container">
                <div class="card overflow-hidden mb-3">
                    <div class="card-body p-2">
                        <div class="row justify-content-between align-items-center pd">
                            <div class="col">
                                Checks
                            </div>
                            <div class="col">
                                <button class="btn btn-falcon-primary float-right" onClick={this.handleSubmit}>New Check</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row mr-1">
                    {this.props.checks.map((check) => this.getCard(check))}
                </div>
            </div>
        );
    }
}
export default CheckView;