export default {
    SET_ALERT(state, alert){
        for (let key in alert){
            state.alert[key] = alert[key];
        }
    },
    TOGGLE_ALERT(state){
        state.alert.isOpen = !state.alert.isOpen;
    }
}