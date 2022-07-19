export default {
    SET_EMPLOYEES(state, employees) {
        state.items = employees;
        state.itemsLoaded = true;
    },
    ADD_EMPLOYEE(state, employee) {
        state.items.push(employee);
    },
    EDIT_EMPLOYEE(state, employee){
        let index = state.items.findIndex(item => item.id === employee.id)
        for (let key in employee){
            state.items[index][key] = employee[key];
        }
    }
}