const initialState = {
    messages: [],
    currentPlaylist: "live",
    playlists: []
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
        default:
            return state
    }
}

export default wwmApp