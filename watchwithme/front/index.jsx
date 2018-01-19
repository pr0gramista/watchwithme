import React from 'react';
import {render} from 'react-dom';
import {Provider} from 'react-redux';
import io from 'socket.io-client';
import wwmTheme from './wwmTheme.jsx';
import Sidebar from './Sidebar.jsx';
import Player from './Player.jsx';
import UsernameDialog from './UsernameDialog.jsx';
import socket from './Socket.jsx';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import './sass/main.scss';
import store from './store/store.jsx';

class App extends React.Component {
    constructor(props) {
        super(props);

        // Connect with server
        let s = io('http://' + document.domain + ':' + location.port);
        socket.init(window.play.room, s, store);

        socket.io.on('connect', function () {
            socket.join();
        });
    }

    render() {
        return (
            <MuiThemeProvider muiTheme={getMuiTheme(wwmTheme)}>
                <div id="main">
                    <UsernameDialog/>
                    <Player/>
                    <Sidebar/>
                </div>
            </MuiThemeProvider>
        );
    }
}


render(
    <Provider store={store}>
        <App/>
    </Provider>, document.getElementById('app'));