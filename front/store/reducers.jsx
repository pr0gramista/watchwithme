const initialState = {
    messages: []
};

function wwmApp(state = initialState, action) {
    console.log(action);
    switch (action.type) {
        case 'RECEIVE_MESSAGE':
            console.log("I am here");
            return Object.assign({}, state, {
                messages: state.messages.concat([action.text])
            });
        default:
            return state
    }
}

export default wwmApp