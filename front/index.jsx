import React from 'react';
import {render} from 'react-dom';
import Sidebar from './Sidebar.jsx';
import Player from './Player.jsx';
import './sass/main.scss';
import UsernameDialog from './UsernameDialog.jsx';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import wwmTheme from './wwmTheme.jsx';
import io from 'socket.io-client';
import socket from './Socket.jsx';
import Cookies from 'js-cookie';
import FlatButton from 'material-ui/FlatButton';

class App extends React.Component {
    constructor(props) {
        super(props);

        console.log("Cookie: " + Cookies.get('nickname'));
        this.state = {
            open: Cookies.get('nickname') === undefined,
            nickname: ""
        };
        socket.setNickname(Cookies.get('nickname') || 'I am ugly');

        this.handleSetNickname = this.handleSetNickname.bind(this);
        this.handleGoAnonymously = this.handleGoAnonymously.bind(this);
        this.handleOnNicknameChange = this.handleOnNicknameChange.bind(this);

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

render(<App/>, document.getElementById('app'));