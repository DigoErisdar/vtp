export default {
    setAlert(context, alert){
        alert.isOpen = true;
        context.commit('SET_ALERT', alert);
    },
    toggleAlert(context){
        context.commit("TOGGLE_ALERT")
    }
}