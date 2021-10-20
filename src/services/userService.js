import api from "@/services/api";

export default {
    getUser(id) {
        return api.get(`user/${id}`).then((response) => response.data);
    },
    createUser(data) {
        return api.post("user/", data);
    },
};
