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
        </b-navbar>

        <b-button type="is-success" size="is-large" @click="newUser = true"
            >Add user</b-button
        >
        <b-modal
            v-model="newUser"
            has-modal-card
            trap-focus
            :destroy-on-hide="false"
            aria-role="dialog"
            aria-label="Upload Modal"
            :can-cancel="['escape', 'outside']"
        >
            <User />
        </b-modal>
        <b-button type="is-info" size="is-large" @click="createPlan"
            >Create plan</b-button
        >
    </div>
</template>

<script>
import User from "@/components/User.vue";
export default {
    data() {
        return {
            newUser: false,
        };
    },
    components: {
        User,
    },
    methods: {
        createPlan() {
            this.$router.push("/plans");
        },
    },
};
</script>

<style></style>
