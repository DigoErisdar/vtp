export default {
    SET_EMPLOYEES(state, employees) {
        state.items = employees;
        state.itemsLoaded = true;
    },
    ADD_EMPLOYE(state, employee) {
        state.items.push(employee);
    }
}