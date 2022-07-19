

export default {
    fetchEmployees(context) {
        if (context.state.itemsLoaded){
            return context.state.items;
        } else {
            return fetch("/employees.json")
            .then(response => {
                return response.json()
            })
            .then(data => {
                context.commit('SET_EMPLOYEES', data);
            });
        }

    },
    addEmployee(context, employee) {
        employee['id'] = new Date().valueOf();
        context.commit('ADD_EMPLOYEE', employee);
    },
    editEmployee(context, employee){
        context.commit('EDIT_EMPLOYEE', employee)
    }
}