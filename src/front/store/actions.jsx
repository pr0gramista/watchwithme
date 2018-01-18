const RECEIVE_MESSAGE = 'RECEIVE_MESSAGE';
const SET_CURRENT_PLAYLIST = 'SET_CURRENT_PLAYLIST';
const ADD_PLAYLIST = 'ADD_PLAYLIST';
const ADD_TO_HISTORY = 'ADD_TO_HISTORY';

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

export const addPlaylist = playlist => {
    return {
        type: ADD_PLAYLIST,
        playlist
    }
};

export const addToHistory = video => {
    return {
        type: ADD_TO_HISTORY,
        video
    }
};