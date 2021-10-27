import api from "@/services/api";

export default {
    getUser(id) {
        return api.get(`user/${id}`).then((response) => response.data);
    },

    createUser(data) {
        return api.post("user/", data).then((response) => response.data);
    },

    fetchUsers() {
        return api.get("user/").then((response) => response.data);
    },

    calcUsers(users) {
        let data = {
            users,
            flaga: true,
        };
        return api.post("user/", data).then((response) => response.data);
    }
};
