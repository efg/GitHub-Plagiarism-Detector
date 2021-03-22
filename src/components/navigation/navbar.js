import React, { Component } from 'react';
import './navbar.css'
class Navbar extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-lg navbar-light bg-white custom-navbar">
                <a className="navbar-brand" href="#">GitHub Plag Checker</a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="nav-item active">
                            <a className="nav-link" href="#" onClick={() => window.location.reload()}>Courses <span className="sr-only">(current)</span></a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="#" onClick={this.props.onLogOut}>Logout</a>
                        </li>
                    </ul>
                </div>
            </nav>
        );
    }
}
export default Navbar;