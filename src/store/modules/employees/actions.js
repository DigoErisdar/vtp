import api from "@/plugins/api";

export default {
    fetchEmployees(context) {
        return api.get('employees/123213')
            .then(response => {
                return response.data
            })
            .then(data => {
                context.commit('setEmployees', data.results)
            })
            .catch(response => {
                console.log(response)
            })
        // return fetch("employees.json")
        //     .then(response => {
        //         return response.json()
        //     })
        //     .then(data => {
        //         context.commit('setEmployees', data);
        //     });
    },
    appendEmploye(context, employee) {
        employee['id'] = new Date().valueOf();
        context.commit('appendEmploye', employee);
    }
}