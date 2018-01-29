import React from 'react';
import {connect} from 'react-redux';
import Cookies from 'js-cookie';
import Dialog from 'material-ui/Dialog';
import TextField from 'material-ui/TextField';
import FlatButton from 'material-ui/FlatButton';
import {setNickname} from "./store/actions.jsx";

const style = {
    maxWidth: '500px'
};

class UsernameDialog extends React.Component {
    constructor(props) {
        super(props);

        const cookieNickname = Cookies.get('nickname');
        console.log(cookieNickname);
        if (cookieNickname !== undefined) {
            this.props.setNickname(cookieNickname);
        }

        this.state = {
            open: cookieNickname === undefined,
            newNickname: "",
        };
    }

    onNicknameChange(event, value) {
        this.setState({newNickname: value});
    }

    handleSetNickname() {
        const newNickname = this.state.newNickname;

        if (newNickname.trim().length > 0) {
            this.setState({open: false});
            this.props.setNickname(newNickname);
        }
    }

    handleGoAnonymously() {
        this.props.setNickname("Anonymous");
        this.setState({open: false});
    }

    render() {
        const actions = [
            <FlatButton
                label="Let's stay anonymous"
                onClick={() => this.handleGoAnonymously}
            />,
            <FlatButton
                label="Set"
                primary={true}
                onClick={() => this.handleSetNickname}
            />,
        ];

        return (
            <Dialog
                title="Name yourself"
                actions={actions}
                modal={true}
                open={this.state.open}
                contentStyle={style}
            >
                <TextField
                    onChange={() => this.onNicknameChange}
                    value={this.state.newNickname}
                    fullWidth={true}
                    hintText="Nickname"
                />
            </Dialog>
        );
    }
}

const mapStateToProps = (state) => {
    return {
        nickname: state.nickname
    };
};

const mapDispatchToProps = dispatch => {
    return {
        setNickname: nickname => {
            dispatch(setNickname(nickname))
        }
    }
};

export default UsernameDialog = connect(mapStateToProps, mapDispatchToProps)(UsernameDialog);