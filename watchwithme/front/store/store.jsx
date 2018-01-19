import {createStore} from 'redux';
import wwmApp from './reducers.jsx';

const store = createStore(wwmApp);
export default store;