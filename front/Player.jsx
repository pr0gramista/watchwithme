import React from 'react';

export default class Player extends React.Component {
    constructor(props) {
        super(props);
        this.player = null;

        this.onPlayerReady = this.onPlayerReady.bind(this);
        this.onPlayerStateChange = this.onPlayerStateChange.bind(this);
    }

    onPlayerReady(event) {
        console.log("onPlayerReady! ");
        console.log(event);
    }

    onPlayerStateChange(event) {
        console.log("onPlayerStateChange");
        console.log(event.data);
    }

    componentDidMount() {
        const tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        const firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

        let youtube_api_ready = function onYouTubeIframeAPIReady() {
            this.player = new YT.Player('player', {
                videoId: '1aEqd4bl6Bs',
                playerVars: {'autoplay': 0},
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