import React from 'react';
import FontIcon from 'material-ui/FontIcon';
import {BottomNavigation, BottomNavigationItem} from 'material-ui/BottomNavigation';
import Paper from 'material-ui/Paper';
import Chat from './sidebar/Chat.jsx';
import Playlists from './sidebar/Playlists.jsx';

const chatIcon = <FontIcon className="material-icons">chat</FontIcon>;
const listIcon = <FontIcon className="material-icons">list</FontIcon>;
const settingsIcon = <FontIcon className="material-icons">settings</FontIcon>;

export default class Sidebar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedIndex: 0,
        };
    }

    select(index) {
        this.setState({selectedIndex: index});
    }

    render() {
        const selectedIndex = this.state.selectedIndex;
        let current_content = null;

        if (selectedIndex === 0)
            current_content = <Chat/>;
        else if (selectedIndex === 1)
            current_content = <Playlists/>;
        else if (selectedIndex === 2)
            current_content = <p>this is 2</p>;

        return (
            <div id="sidebar">
                <Paper zDepth={1}>
                    <BottomNavigation selectedIndex={this.state.selectedIndex}>
                        <BottomNavigationItem
                            label="Chat"
                            icon={chatIcon}
                            onClick={() => this.select(0)}
                        />
                        <BottomNavigationItem
                            label="Playlist"
                            icon={listIcon}
                            onClick={() => this.select(1)}
                        />
                        <BottomNavigationItem
                            label="Settings"
                            icon={settingsIcon}
                            onClick={() => this.select(2)}
                        />
                    </BottomNavigation>
                </Paper>
                {current_content}
            </div>
        );
    }
}