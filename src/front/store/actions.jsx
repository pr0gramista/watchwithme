const RECEIVE_MESSAGE = 'RECEIVE_MESSAGE';
const SET_CURRENT_PLAYLIST = 'SET_CURRENT_PLAYLIST';

export const receiveMessage = text => {
    return {
        type: RECEIVE_MESSAGE,
        text
    }
};

export const setCurrentPlaylist = playlist => {
    return {
        type: SET_CURRENT_PLAYLIST,
        playlist
    }
};