import React from 'react';
import socket from './Socket.jsx';

export default class Player extends React.Component {
    constructor(props) {
        super(props);
        this.player = null;
        this.state = {
            video: ''
        };

        this.stopFirst = false;
        this.ignore = false;

        this.onPlayerReady = this.onPlayerReady.bind(this);
        this.onPlayerStateChange = this.onPlayerStateChange.bind(this);
        this.onLiveVideoChanged = this.onLiveVideoChanged.bind(this);
        this.onPlaylistVideoChanged = this.onPlaylistVideoChanged.bind(this);
        this.onPlay = this.onPlay.bind(this);
        this.onPause = this.onPause.bind(this);
        this.suppress = this.suppress.bind(this);

        socket.io.on('play', this.onPlay);
        socket.io.on('pause', this.onPause);
        socket.io.on('live_video_changed', this.onLiveVideoChanged);
        socket.io.on('playlist_video_changed', this.onPlaylistVideoChanged);
    }

    suppress() {
        this.ignore = true;
        let f = function () {
            this.ignore = false
        }.bind(this);
        setTimeout(f, 300)
    }

    onLiveVideoChanged(video) {
        this.setState({
            video: video
        });

        const setVideoEventually = (id) => {
            if (this.player != null) {
                this.player.loadVideoById(id);
                this.suppress();
            } else {
                setTimeout(() => {
                    setVideoEventually(id);
                }, 2000);
            }
        };
        setVideoEventually(video.id);
    }

    onPlaylistVideoChanged(video) {
        this.setState({
            video: video
        });
        this.player.loadVideoById(video.id);
        this.suppress();
    }

    onPlay(time) {
        const player = this.player;
        if (Math.abs(player.getCurrentTime() - time) > 3 || player.getPlayerState() !== 1) {
            player.seekTo(time);
            player.playVideo();
            this.suppress()
        }
    }

    onPause(time) {
        const player = this.player;
        if (Math.abs(player.getCurrentTime() - time) > 3 || player.getPlayerState() !== 2) {
            player.seekTo(time);
            player.pauseVideo();
            this.suppress()
        }
    }

    onPlayerReady(event) {
    }

    onPlayerStateChange(event) {
        if (event.data === 0) { // Ended
            socket.getNextVideoIfPossible(this.state.video.id);
            return;
        }

        if (this.stopFirst && event.data === 1) {
            event.target.pauseVideo();
            this.stopFirst = false;
        }

        if (!this.ignore) {
            if (event.data === 2) {
                socket.pause(this.player.getCurrentTime());
            } else if (event.data === 1) {
                socket.play(this.player.getCurrentTime());
            }
        }
    }

    componentDidMount() {
        const tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        const firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

        let youtube_api_ready = function onYouTubeIframeAPIReady() {
            this.player = new YT.Player('player', {
                videoId: 'feA64wXhbjo',
                events: {
                    'onReady': this.onPlayerReady,
                    'onStateChange': this.onPlayerStateChange
                }
            });
        };
        youtube_api_ready = youtube_api_ready.bind(this);
        window.onYouTubeIframeAPIReady = youtube_api_ready;
    }

    render() {
        return (
            <div id="player"></div>
        );
    }
}