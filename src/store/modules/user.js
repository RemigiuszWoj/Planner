import userService from "../../services/userService";

const state = {
    users: [],
};

const getters = {};

const actions = {
    fetchUsers({ commit }) {
        return new Promise((resolve, reject) => {
            userService
                .fetchUsers()
                .then((users) => {
                    commit("setUsers", users);
                    resolve();
                })
                .catch((err) => {
                    reject(err);
                });
        });
    },
};

const mutations = {
    setUsers(state, users) {
        state.users = users;
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};
