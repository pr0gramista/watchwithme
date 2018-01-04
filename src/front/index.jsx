import React from 'react';
import {render} from 'react-dom';
import Sidebar from './Sidebar.jsx';
import Player from './Player.jsx';
import UsernameDialog from './UsernameDialog.jsx';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import wwmTheme from './wwmTheme.jsx';
import io from 'socket.io-client';
import socket from './Socket.jsx';
import Cookies from 'js-cookie';
import FlatButton from 'material-ui/FlatButton';
import {Provider} from 'react-redux'
import {createStore} from 'redux'
import wwmApp from './store/reducers.jsx'

class App extends React.Component {
    constructor(props) {
        super(props);

        this.handleSetNickname = this.handleSetNickname.bind(this);
        this.handleGoAnonymously = this.handleGoAnonymously.bind(this);
        this.handleOnNicknameChange = this.handleOnNicknameChange.bind(this);

        // Get nickname
        this.state = {
            open: Cookies.get('nickname') === undefined,
            nickname: ""
        };
        socket.setNickname(Cookies.get('nickname') || 'I am ugly');

        // Connect with server
        let s = io('http://' + document.domain + ':' + location.port);
        socket.init(window.play.room, s);

        socket.io.on('connect', function () {
            socket.join();
        });
    }

    handleSetNickname() {
        const nickname = this.state.nickname;

        if (nickname.trim().length > 0) {
            this.setState({open: false});
            Cookies.set('nickname', nickname);
            socket.setNickname(nickname);
        }
    }

    handleGoAnonymously() {
        Cookies.set('nickname', 'Anonymous');
        socket.setNickname('Anonymous');
        this.setState({open: false});
    }

    handleOnNicknameChange(event, nickname) {
        this.setState({nickname: nickname})
    }

    render() {
        const actions = [
            <FlatButton
                label="Let's go anonymously"
                onClick={this.handleGoAnonymously}
            />,
            <FlatButton
                label="Set"
                primary={true}
                onClick={this.handleSetNickname}
            />,
        ];

        return (
            <MuiThemeProvider muiTheme={getMuiTheme(wwmTheme)}>
                <div id="main">
                    <UsernameDialog open={this.state.open} actions={actions} nickname={this.state.nickname}
                                    onNicknameChange={this.handleOnNicknameChange}/>
                    <Player/>
                    <Sidebar/>
                </div>
            </MuiThemeProvider>
        );
    }
}

let store = createStore(wwmApp);

render(
    <Provider store={store}>
        <App/>
    </Provider>, document.getElementById('app'));