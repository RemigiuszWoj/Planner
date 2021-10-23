import api from "@/services/api";

export default {
    getUser(id) {
        return api.get(`user/${id}`).then((response) => response.data);
    },
    createUser(data) {
        return api.post("user/", data);
    },
    fetchUsers() {
        return api.get("user/").then((response) => response.data);
    }
};
