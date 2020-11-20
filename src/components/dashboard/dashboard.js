import React, { Component } from 'react';
// import { BrowserRouter, Route, Switch } from 'react-router-dom';
// import Login from './../login/login';
// import './dashboard.css';
import Card from './card/card';
class Dashboard extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <div class="container">
                <div class="card overflow-hidden mb-3">
                    <div class="card-body p-2">
                        <div class="row justify-content-between align-items-center">
                            <div class="col">
                                Test
                            </div>
                        </div>
                    </div>
                </div>
                <Card name="Test Name" info="Test Info" attr="Count" attrCount="3"/>
            </div>
        );
    }
}
export default Dashboard;   