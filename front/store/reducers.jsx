const initialState = {
    messages: []
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