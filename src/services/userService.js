import api from "@/services/api";

export default {
    createUser(dataToFetch) {
        return api
            .put(`users/`, { params: dataToFetch })
            .then((response) => response.data);
    },
    getUser() {
        console.log("jestem w service");
        return api.get(`users/`).then((response) => response.data);
    },
};
