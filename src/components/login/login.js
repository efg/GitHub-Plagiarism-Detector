import React, { Component } from 'react';

class Login extends Component{
    constructor(props){
        super(props);
        this.state = {};
    }
    render(){
        return(
            <div class="container">
                <form class="sign-in-form" method="post" action="">
                    <div class="row flex-center min-vh-50 py-6">
                        <div class="col-sm-10 col-md-8 col-lg-6 col-xl-5">
                            <div class="card">
                                <div class="card-header">
                                    <div class="col-auto">
                                        Sign In
                                    </div>
                                </div>
                                <div class="card-body p-4 p-sm-5">
                                    <div class="form-group">
                                        {/* <label for="inputEmail" class="text-left">Email address</label> */}
                                        <input class="form-control" type="email" name="email" id="inputEmail" placeholder="Email address" />
                                        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                                    </div>
                                    <div class="form-group">
                                        {/* <label for="inputPassword">Password</label> */}
                                        <input class="form-control" type="password" name="password" id="inputPassword" placeholder="Password" />
                                    </div>
                                    <div class="form-group">
                                        <button class="btn btn-primary btn-block mt-3" type="submit">Sign in  </button>
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