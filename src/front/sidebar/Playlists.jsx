import React from 'react';
import {connect} from 'react-redux';
import TextField from 'material-ui/TextField';
import FloatingActionButton from 'material-ui/FloatingActionButton';
import ContentAdd from 'material-ui/svg-icons/content/add';
import Dialog from 'material-ui/Dialog';
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';


class Playlists extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currentPlaylist: null,
        };

        this.handlePlaylistChange = this.handlePlaylistChange.bind(this);
    }

    handlePlaylistChange(event, index, value) {
        this.setState({currentPlaylist: value});
    }

    render() {
        const playlistsItems = this.props.playlists.map((playlist, index) => <MenuItem key={playlist.id}
                                                                                       value={playlist}
                                                                                       primaryText={playlist.title}/>);

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
                <FloatingActionButton style={{position: "absolute", bottom: 20, right: 20}}>
                    <ContentAdd/>
                </FloatingActionButton>
                <Dialog
                    title="Add playlist"
                    modal={false}
                    open={false}
                >
                    <TextField
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