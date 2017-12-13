import React from 'react';
import {render} from 'react-dom';
import Sidebar from './Sidebar.jsx';
import Player from './Player.jsx';
import './sass/main.scss';

class App extends React.Component {
    render() {
        return (
            <div id="main">
                <Player />
                <Sidebar/>
            </div>
        );
    }
}

render(<App/>, document.getElementById('app'));