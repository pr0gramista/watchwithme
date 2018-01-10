const initialState = {
    messages: [],
    currentPlaylist: null,
    playlists: [ // Example fake playlists
        {
            'id': 'PLC90FB71F6ECE17F3',
            'title': 'Hits of the 70\'s,80\'s,90\'s(1)',
            'videos': [{
                'id': 'y6120QOlsfU',
                'title': 'Darude - Sandstorm',
                'thumbnail': 'https://i.ytimg.com/vi/y6120QOlsfU/hqdefault.jpg'
            }]
        },
        {
            'id': 'RDpmxYePDPV6M',
            'title': 'Concentration \\ Programming Music 010 (part 2)',
            'videos': [{
                'id': 'y6120QOlsfU',
                'title': 'Darude - Sandstorm',
                'thumbnail': 'https://i.ytimg.com/vi/y6120QOlsfU/hqdefault.jpg'
            },
                {
                    'id': 'Be0OAjuk_1k',
                    'title': 'Scatman John - Scatman (Extended Mix) 1995',
                    'thumbnail': 'https://i.ytimg.com/vi/Be0OAjuk_1k/hqdefault.jpg'
                }]
        }
    ]
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
        default:
            return state
    }
}

export default wwmApp