const initialState = {
    messages: [],
    playlists: [ // Example fake playlists
        {
            'id': '3gk3kg9ok3g',
            'title': 'cheekybreeky'
        },
        {
            'id': 'ogk3g093ko',
            'title': 'Music for coding'
        }
    ]
};

function wwmApp(state = initialState, action) {
    switch (action.type) {
        case 'RECEIVE_MESSAGE':
            return Object.assign({}, state, {
                messages: state.messages.concat([action.text])
            });
        default:
            return state
    }
}

export default wwmApp