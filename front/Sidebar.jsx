import React from 'react';
import FontIcon from 'material-ui/FontIcon';
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import {BottomNavigation, BottomNavigationItem} from 'material-ui/BottomNavigation';
import Paper from 'material-ui/Paper';
import FloatingActionButton from 'material-ui/FloatingActionButton';
import ContentAdd from 'material-ui/svg-icons/content/add';
import Chat from './Chat.jsx';

const chatIcon = <FontIcon className="material-icons">chat</FontIcon>;
const listIcon = <FontIcon className="material-icons">list</FontIcon>;
const settingsIcon = <FontIcon className="material-icons">settings</FontIcon>;

export default class Sidebar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedIndex: 0,
            currentPlaylist: 0,
        };

        this.handlePlaylistChange = this.handlePlaylistChange.bind(this);
    }

    select(index) {
        this.setState({selectedIndex: index});
    }

    handlePlaylistChange(event, index, value) {
        this.setState({currentPlaylist: value});
    }

    render() {
        const selectedIndex = this.state.selectedIndex;
        let current_content = null;

        if (selectedIndex === 0)
            current_content = <Chat/>;
        else if (selectedIndex === 1)
            current_content = (
                <div id="playlist">
                    <SelectField
                        id="playlistSelect"
                        fullWidth={true}
                        floatingLabelText="Playlist"
                        value={this.state.currentPlaylist}
                        onChange={this.handlePlaylistChange}
                    >
                        <MenuItem value={0} primaryText="Music"/>
                        <MenuItem value={1} primaryText="Funny videos"/>
                        <MenuItem value={2} primaryText="Catbringer"/>
                        <MenuItem value={3} primaryText="80s hits"/>
                        <MenuItem value={4} primaryText="ASMR"/>
                    </SelectField>
                    <FloatingActionButton style={{position: "absolute", bottom: 20, right: 20}}>
                        <ContentAdd/>
                    </FloatingActionButton>
                </div>
            );
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