import React from 'react';
import {render} from 'react-dom';
import Sidebar from './Sidebar.jsx';
import Player from './Player.jsx';
import './sass/main.scss';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import wwmTheme from './wwmTheme.jsx';
import io from 'socket.io-client';

class App extends React.Component {
    constructor(props) {
        super(props);

        window.socket = io('http://' + document.domain + ':' + location.port);
        window.socket.on('connect', function () {
            window.socket.emit('join', window.play.room);
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