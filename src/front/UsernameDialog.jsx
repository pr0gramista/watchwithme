import React from 'react';
import Dialog from 'material-ui/Dialog';
import TextField from 'material-ui/TextField';

const style = {
    maxWidth: '500px'
};

export default class UsernameDialog extends React.Component {
    render() {
        return (
            <Dialog
                title="Name yourself"
                actions={this.props.actions}
                modal={true}
                open={this.props.open}
                contentStyle={style}
            >
                <TextField
                    onChange={this.props.onNicknameChange}
                    value={this.props.nickname}
                    fullWidth={true}
                    hintText="Nickname"
                />
            </Dialog>
        );
    }
}