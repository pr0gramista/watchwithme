import React from 'react';
import {connect} from 'react-redux';
import TextField from 'material-ui/TextField';
import FloatingActionButton from 'material-ui/FloatingActionButton';
import ContentAdd from 'material-ui/svg-icons/content/add';
import Dialog from 'material-ui/Dialog';
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import FlatButton from 'material-ui/FlatButton';


class Playlists extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currentPlaylist: null,
            dialogOpened: false,
            addPlaylistString: ""
        };

        this.handleDialogClose = this.handleDialogClose.bind(this);
        this.handleAddPlaylist = this.handleAddPlaylist.bind(this);
        this.handlePlaylistChange = this.handlePlaylistChange.bind(this);
        this.onPlaylistStringChange = this.onPlaylistStringChange.bind(this);
        this.handleAddPlaylistDialogFAB = this.handleAddPlaylistDialogFAB.bind(this);
    }

    handlePlaylistChange(event, index, value) {
        this.setState({currentPlaylist: value});
    }

    handleAddPlaylist() {
        // TODO: Send playlist id/url to the server
        this.setState({dialogOpened: false, addPlaylistString: ""});
    }

    handleAddPlaylistDialogFAB() {
        this.setState({dialogOpened: true});
    }

    handleDialogClose() {
        this.setState({dialogOpened: false});
    }

    onPlaylistStringChange(event, newString) {
        this.setState({addPlaylistString: newString});
    }

    render() {
        const playlistsItems = this.props.playlists.map((playlist, index) => <MenuItem key={playlist.id}
                                                                                       value={playlist}
                                                                                       primaryText={playlist.title}/>);
        const actions = [
            <FlatButton
                label="Close"
                onClick={this.handleDialogClose}
            />,
            <FlatButton
                label="Add"
                primary={true}
                onClick={this.handleAddPlaylist}
            />,
        ];

        return (
            <div id="playlist">
                <SelectField
                    id="playlistSelect"
                    fullWidth={true}
                    floatingLabelText="Playlist"
                    value={this.state.currentPlaylist}
                    onChange={this.handlePlaylistChange}
                >
                    {playlistsItems}
                </SelectField>
                <FloatingActionButton onClick={this.handleAddPlaylistDialogFAB}
                                      style={{position: "absolute", bottom: 20, right: 20}}>
                    <ContentAdd/>
                </FloatingActionButton>
                <Dialog
                    title="Add playlist"
                    actions={actions}
                    modal={false}
                    open={this.state.dialogOpened}
                >
                    <TextField
                        onChange={this.onPlaylistStringChange}
                        value={this.state.addPlaylistString}
                        fullWidth={true}
                        hintText="Playlist ID or URL"
                    />
                </Dialog>
            </div>
        );
    }
}

const mapStateToProps = (state) => {
    return {playlists: state.playlists};
};

export default Playlists = connect(mapStateToProps)(Playlists);