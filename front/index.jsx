import React from 'react';
import {render} from 'react-dom';
import Sidebar from './Sidebar.jsx';
import Player from './Player.jsx';

class App extends React.Component {
    render() {
        return (
            <div>
                <Player />
                <Sidebar/>
            </div>
        );
    }
}

render(<App/>, document.getElementById('app'));