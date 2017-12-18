import React from 'react';
import {render} from 'react-dom';
import Sidebar from './Sidebar.jsx';
import Player from './Player.jsx';
import './sass/main.scss';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import wwmTheme from './wwmTheme.jsx';
import io from 'socket.io-client';
import socket from './Socket.jsx';

class App extends React.Component {
    constructor(props) {
        super(props);

        let s = io('http://' + document.domain + ':' + location.port);
        socket.init(window.play.room, s);

        socket.io.on('connect', function () {
            socket.join();
        });
    }

    render() {
        return (
            <MuiThemeProvider muiTheme={getMuiTheme(wwmTheme)}>
                <div id="main">
                    <Player/>
                    <Sidebar/>
                </div>
            </MuiThemeProvider>
        );
    }
}

render(<App/>, document.getElementById('app'));