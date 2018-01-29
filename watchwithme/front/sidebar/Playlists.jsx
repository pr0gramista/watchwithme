import React from 'react';
import {connect} from 'react-redux';
import TextField from 'material-ui/TextField';
import FloatingActionButton from 'material-ui/FloatingActionButton';
import ContentAdd from 'material-ui/svg-icons/content/add';
import Dialog from 'material-ui/Dialog';
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import IconButton from 'material-ui/IconButton';
import FontIcon from 'material-ui/FontIcon';
import FlatButton from 'material-ui/FlatButton';
import {setCurrentPlaylist} from '../store/actions.jsx';
import socket from '../Socket.jsx';

const LIVE = "live";


class PlaylistDisplay extends React.Component {
    render() {
        const videoItems = this.props.playlist.videos.map((video, index) =>
            <li key={video.id} video={video.id} className="video" onClick={this.props.changeVideo}>
                <img src={video.thumbnail}/>
                <h1>{video.title}</h1>
            </li>);

        return (
            <ul className="playlist">
                {videoItems}
            </ul>
        );
    }
}


class LivePlaylistDisplay extends React.Component {
    render() {
        const historyItems = this.props.history.map((video, index) =>
            <li key={video.id} video={video.id} className="video" onClick={this.props.changeVideo}>
                <img src={video.thumbnail}/>
                <h1>{video.title}</h1>
            </li>);
        let display = null;
        if (historyItems.length > 0) {
            display = <ul className="playlist">{historyItems}</ul>;
        } else {
            display = <div id="empty-history">History is empty now</div>
        }

        return (
            <div className="history">
                <h3>History</h3>
                {display}
            </div>
        );
    }
}


class Playlists extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currentPlaylist: null,
            dialogOpened: false,
            addPlaylistString: "",
            liveVideoString: ""
        };
    }

    handlePlaylistChange(event, index, value) {
        if (value === LIVE) {
            socket.changePlaylist(LIVE);
        } else {
            socket.changePlaylist(value.id);
        }
        this.props.setCurrentPlaylist(value);
    }

    handleLiveStringChanged(event, newString) {
        this.setState({liveVideoString: newString});
    }

    handleSetLiveVideo() {
        socket.setLiveVideo(this.state.liveVideoString);
        this.setState({liveVideoString: ""});
    }

    handleAddPlaylist() {
        socket.addPlaylist(this.state.addPlaylistString);
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
        let playlistsItems = this.props.playlists.map((playlist, index) => <MenuItem key={playlist.id}
                                                                                     value={playlist}
                                                                                     primaryText={playlist.title}/>);
        playlistsItems.unshift(<MenuItem key={"live"} value={LIVE} primaryText={"🔴 Live"}/>);

        // Actions for add playlist dialog
        const actions = [
            <FlatButton
                label="Close"
                onClick={() => this.handleDialogClose}
            />,
            <FlatButton
                label="Add"
                primary={true}
                onClick={() => this.handleAddPlaylist}
            />,
        ];

        // Determine display (playlist or live)
        let display = null;
        if (this.props.currentPlaylist !== null)
            if (this.props.currentPlaylist !== LIVE)
                display = <PlaylistDisplay playlist={this.props.currentPlaylist} changeVideo={(event) => {
                    socket.changePlaylistVideo(event.currentTarget.getAttribute('video'));
                }}/>;
            else
                display = <LivePlaylistDisplay history={this.props.liveHistory} changeVideo={(event) => {
                    socket.setLiveVideo(event.currentTarget.getAttribute('video'));
                }}/>;

        // Show text field if now on live
        let liveInput = null;
        if (this.props.currentPlaylist === LIVE) {
            liveInput =
                <form onSubmit={() => this.handleSetLiveVideo} className="live-form fl">
                    <TextField
                        onChange={() => this.handleLiveStringChanged}
                        value={this.state.liveVideoString}
                        fullWidth={true}
                        hintText="Video id or url"
                        className="fl-grow"
                    />
                    <IconButton onClick={() => this.handleSetLiveVideo}><FontIcon
                        className="material-icons">send</FontIcon></IconButton>
                </form>;
        }

        return (
            <div id="playlist">
                <SelectField
                    id="playlistSelect"
                    fullWidth={true}
                    floatingLabelText="Playlist"
                    value={this.props.currentPlaylist}
                    onChange={() => this.handlePlaylistChange}
                >
                    {playlistsItems}
                </SelectField>
                {liveInput}
                <FloatingActionButton onClick={() => this.handleAddPlaylistDialogFAB}
                                      style={{position: "absolute", bottom: 20, right: 20, zIndex: 100}}>
                    <ContentAdd/>
                </FloatingActionButton>
                {display}
                <Dialog
                    title="Add playlist"
                    actions={actions}
                    modal={false}
                    open={this.state.dialogOpened}
                >
                    <TextField
                        onChange={() => this.onPlaylistStringChange}
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
    return {
        playlists: state.playlists,
        currentPlaylist: state.currentPlaylist,
        liveHistory: state.liveHistory
    };
};

const mapDispatchToProps = dispatch => {
    return {
        setCurrentPlaylist: playlist => {
            dispatch(setCurrentPlaylist(playlist))
        }
    }
};

export default Playlists = connect(mapStateToProps, mapDispatchToProps)(Playlists);