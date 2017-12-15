import {
    pink700, pink500,
    grey600,
    pinkA100, pinkA200, pinkA400,
    fullWhite, indigo800
} from 'material-ui/styles/colors';
import {fade} from 'material-ui/utils/colorManipulator';
import spacing from 'material-ui/styles/spacing';

export default {
    spacing: spacing,
    fontFamily: 'Roboto, sans-serif',
    borderRadius: 2,
    palette: {
        primary1Color: pink500,
        primary2Color: pink700,
        primary3Color: grey600,
        accent1Color: pinkA200,
        accent2Color: pinkA400,
        accent3Color: pinkA100,
        textColor: fullWhite,
        secondaryTextColor: fade(fullWhite, 0.7),
        alternateTextColor: '#303030',
        canvasColor: indigo800,
        borderColor: fade(fullWhite, 0.3),
        disabledColor: fade(fullWhite, 0.3),
        pickerHeaderColor: fade(fullWhite, 0.12),
        clockCircleColor: fade(fullWhite, 0.12),
    },
};