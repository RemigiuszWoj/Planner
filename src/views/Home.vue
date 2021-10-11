<template>
    <div>
        <b-navbar>
            <template #brand>
                <b-navbar-item tag="router-link" :to="{ path: '/' }">
                    <img
                        src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
                        alt="Lightweight UI components for Vue.js based on Bulma"
                    />
                </b-navbar-item>
            </template>
            <template #start>
                <b-navbar-item href="#"> Home </b-navbar-item>
                <b-navbar-item href="#"> Documentation </b-navbar-item>
                <b-navbar-dropdown label="Info">
                    <b-navbar-item href="#"> About </b-navbar-item>
                    <b-navbar-item href="#"> Contact </b-navbar-item>
                </b-navbar-dropdown>
            </template>

            <template #end>
                <b-navbar-item tag="div">
                    <div class="buttons">
                        <a class="button is-primary">
                            <strong>Sign up</strong>
                        </a>
                        <a class="button is-light"> Log in </a>
                    </div>
                </b-navbar-item>
            </template>
        </b-navbar>
        <div class="my-button">
            <b-button @click="getUser">Get users</b-button>
        </div>
        <b-field class="my-input">
            <b-numberinput v-model="id"></b-numberinput>
        </b-field>
    </div>
</template>

<script>
import userService from "@/services/userService";
// import { mapState } from "vuex";
export default {
    data() {
        return {
            id: 0,
        };
    },
    methods: {
        getUser() {
            userService
                .getUser(this.id)
                .then((data) => {
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: `Get data from endpoint: ${this.id}.`,
                        type: "is-success",
                    });
                    console.log("DATA: ", data);
                })
                .catch(() => {
                    this.$buefy.notification.open({
                        duration: 3000,
                        message: "Not found record in database",
                        type: "is-danger",
                    });
                });
        },
    },
};
</script>

<style>
.my-button {
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0.5rem;
}
.my-input {
    max-width: 20%;
    margin-left: auto;
    margin-right: auto;
}
</style>
