import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/Header';
import Dashboard from './gallery/Dashboard';

class App extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <div>
                <Dashboard/>
                </div>
            </Fragment>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));