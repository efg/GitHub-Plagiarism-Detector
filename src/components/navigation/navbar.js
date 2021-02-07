import React, { Component } from 'react';
import './navbar.css'
class Navbar extends Component {
    render() {
        return (
            <nav class="navbar navbar-expand-lg navbar-light bg-white custom-navbar">
                <a class="navbar-brand" href="#">GitHub Plag Checker</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item active">
                            <a class="nav-link" href="#" onClick={() => window.location.reload()}>Courses <span class="sr-only">(current)</span></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#" onClick={this.props.onLogOut}>Logout</a>
                        </li>
                    </ul>
                </div>
            </nav>
        );
    }
}
export default Navbar;