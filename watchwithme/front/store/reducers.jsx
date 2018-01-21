const initialState = {
    nickname: 'Anonymous',
    messages: [],
    currentPlaylist: "live",
    playlists: [],
    liveHistory: [],
    currentVideo: null
};

function wwmApp(state = initialState, action) {
    switch (action.type) {
        case 'RECEIVE_MESSAGE':
            return Object.assign({}, state, {
                messages: state.messages.concat([action.text])
            });
        case 'SET_CURRENT_PLAYLIST':
            return Object.assign({}, state, {
                currentPlaylist: action.playlist
            });
        case 'ADD_PLAYLIST':
            return Object.assign({}, state, {
                playlists: state.playlists.concat([action.playlist])
            });
        case 'ADD_TO_HISTORY':
            return Object.assign({}, state, {
                liveHistory: state.liveHistory.concat([action.video])
            });
        case 'SET_NICKNAME':
            return Object.assign({}, state, {
                nickname: action.nickname
            });
        case 'SET_CURRENT_VIDEO':
            return Object.assign({}, state, {
                currentVideo: action.videoId
            });
        default:
            return state
    }
}

export default wwmApp;