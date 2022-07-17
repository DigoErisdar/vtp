export default {
    setEmployees(state, employees) {
        state.items = employees;
    },
    appendEmploye(state, employee) {
        state.items.push(employee);
    }
}