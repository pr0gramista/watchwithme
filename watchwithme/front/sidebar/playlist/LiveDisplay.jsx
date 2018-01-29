import React from 'react';

export default class LiveDisplay extends React.Component {
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