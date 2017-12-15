import React from 'react';
import {render} from 'react-dom';
import Sidebar from './Sidebar.jsx';
import Player from './Player.jsx';
import './sass/main.scss';
import {cyan500} from 'material-ui/styles/colors';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import wwmTheme from './wwmTheme.jsx';

class App extends React.Component {
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