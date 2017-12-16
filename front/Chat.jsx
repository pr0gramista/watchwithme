import React from 'react';
import TextField from 'material-ui/TextField';
import IconButton from 'material-ui/IconButton';
import FontIcon from 'material-ui/FontIcon';

export default class Chat extends React.Component {
    constructor(props) {
        super(props);
        this.state = {message: ''};

        this.handleChatMessageChange = this.handleChatMessageChange.bind(this);
        this.handleChatMessage = this.handleChatMessage.bind(this);
    }

    handleChatMessage(event) {
        event.preventDefault();
        console.log(this.state.message);
        // Send message
        this.setState({message: ''});
    }

    handleChatMessageChange(event) {
        this.setState({message: event.target.value});
    }

    render() {
        return (
            <div id="chat">
                <div className="fl">
                    <form onSubmit={this.handleChatMessage} className="chat-form">
                        <TextField hintText="Message" value={this.state.message} onChange={this.handleChatMessageChange} className="fl-grow"/>
                        <IconButton onClick={this.handleChatMessage}><FontIcon className="material-icons">send</FontIcon></IconButton>
                    </form>
                </div>
            </div>
        );
    }
}