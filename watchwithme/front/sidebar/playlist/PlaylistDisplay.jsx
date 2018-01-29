import React from 'react';

export default class PlaylistDisplay extends React.Component {
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