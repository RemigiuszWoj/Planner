import userService from "../../services/userService";

const state = {
    users: [],
    output: [],
};

const getters = {};

const actions = {
    fetchUsers({ commit }) {
        return new Promise((reject) => {
            userService
                .fetchUsers()
                .then((users) => {
                    commit("setUsers", users);

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
    setOutput(state, output) {
        state.output = output;
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};
