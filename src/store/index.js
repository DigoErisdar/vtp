import {createStore} from "vuex";
import state from './state';
import mutations from './mutations';
import actions from './actions';
import getters from './getters';
import employees from './modules/employees';

const store = createStore({
    state,
    mutations,
    actions,
    getters,
    modules: {
        employees,
    }
})

export default store;