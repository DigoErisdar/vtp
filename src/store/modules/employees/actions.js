

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
    addEmploye(context, employee) {
        employee['id'] = new Date().valueOf();
        context.commit('ADD_EMPLOYE', employee);
    }
}