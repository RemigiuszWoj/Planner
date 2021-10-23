<template>
    <div>
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
import { mapState } from "vuex";
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
        fetchAll() {
            console.log(this.users);
        },
    },
    computed: {
        ...mapState("user", ["users"]),
    },
    created() {
        this.$store.dispatch("user/fetchUsers");
    },
};
</script>

<style></style>
