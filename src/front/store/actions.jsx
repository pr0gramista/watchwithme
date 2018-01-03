const RECEIVE_MESSAGE = 'RECEIVE_MESSAGE';

function receiveMessage(text) {
    return {
        type: RECEIVE_MESSAGE,
        text
    }
}

export default receiveMessage;