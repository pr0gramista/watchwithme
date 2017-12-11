import React from 'react';

export default class Player extends React.Component {
    constructor (props) {
        super(props);
        this.player = null;
    }

    componentDidMount () {
        const tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        const firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

        let youtube_api_ready = function onYouTubeIframeAPIReady() {
            this.player = new YT.Player('player', {
                videoId: '1aEqd4bl6Bs',
                playerVars: {'autoplay': 0 }
            });
        };
        youtube_api_ready = youtube_api_ready.bind(this);
        window.onYouTubeIframeAPIReady = youtube_api_ready;

    }

    render () {
        return (
            <div id="player"></div>
        );
    }
}