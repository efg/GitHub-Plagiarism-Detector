import React, { Component } from 'react';
import { useHistory } from "react-router";
import axios from 'axios';
import './login.css';

class Login extends Component{
    constructor(props){
        super(props);
        this.state = {
            email:"",
            password:""
        };
    }
    handleChange=event=>{
        const target = event.target;
        const value = target.value;
        const name = target.name;
        this.setState({
          [name]: value
        });
        // console.log(this.state);
    }
    handleSubmit = async ()=>{
        const email = this.state.email;
        const password = this.state.password;
        
        // console.log(this.state.email);
       await axios.post('http://127.0.0.1:5000/user/login', { email, password })
      .then(res => {
        // Redirect to next page here
        console.log(res);
        console.log(res.message);
        useHistory().push("/dashboard");
      })
      .catch((error) => {
        console.log(error.response.data);
        useHistory().push("/dashboard");
      });

    }
    render(){
        return(
            <div class="container">
                <form class="sign-in-form" method="post">
                    <div class="row flex-center min-vh-50 py-6">
                        <div class="col-sm-10 col-md-8 col-lg-6 col-xl-5">
                            <div class="card">
                                <div class="card-header">
                                    <div class="col-auto fancy-font">
                                        Sign In
                                    </div>
                                </div>
                                <div class="card-body p-4 p-sm-5">
                                    <div class="form-group">
                                        {/* <label for="inputEmail" class="text-left">Email address</label> */}
                                        <input class="form-control" type="email" name="email" id="inputEmail" placeholder="Email address" onChange={this.handleChange} />
                                        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                                    </div>
                                    <div class="form-group">
                                        {/* <label for="inputPassword">Password</label> */}
                                        <input class="form-control" type="password" name="password" id="inputPassword" placeholder="Password" onChange={this.handleChange} />
                                    </div>
                                    <div class="form-group">
                                        <button class="btn btn-primary btn-block mt-3" onClick={this.handleSubmit}>Sign in  </button>
                                    </div>
                                    <div class="w-100 position-relative mt-4">
                                        <hr class="text-300" />
                                        <div class="position-absolute absolute-centered t-0 px-3 bg-white text-sans-serif fs--1 text-500 text-nowrap">or</div>
                                    </div>
                                    <div class="form-group mb-0">
                                        <div class="row no-gutters">
                                            <div class="col-sm-12"><a class="btn btn-falcon-primary btn-block mt-2" href="#"><span class="fab fa-google-plus-g mr-2" data-fa-transform="grow-8"></span> Request an account</a></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
            </div>  
        );
    }
}

export default Login;