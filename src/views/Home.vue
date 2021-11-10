<template>
    <div class="main-content">
        <div class="buttons">
            <div class="btn-container-1">
                <b-button type="is-success" @click="newUser = true" class="newuser-btn"
                    >Add user</b-button
                >
                <!-- <b-modal
                v-model="newUser"
                has-modal-card
                trap-focus
                :destroy-on-hide="false"
                aria-role="dialog"
                aria-label="Upload Modal"
                :can-cancel="['escape', 'outside']"
            >
                <User />
            </b-modal> -->
            </div>
            <div class="btn-container-2">
                <b-button type="is-info" @click="createPlan" class="create-btn"
                    >Create plan</b-button
                >
            </div>
        </div>

        <div class="random-database-btn-container">
            <b-button type="is-info" class="random-database-btn"
                >Random database</b-button
            >
        </div>

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
    },
    computed: {
        ...mapState("user", ["users"]),
    },
    created() {
        this.$store.dispatch("user/fetchUsers");
    },
};
</script>

<style scoped>
.create-btn {
    box-shadow: 0 0 30px 1px rgb(1 1 1 / 30%);
    transition: all 0.6s ease-in-out;
    width: 500px;
}

.create-btn:hover {
    font-size: 76px;
}

.newuser-btn {
    box-shadow: 0 0 30px 1px rgb(1 1 1 / 30%);
    transition: all 0.4s ease-in-out;
    width: 500px;
}
.newuser-btn:hover {
    font-size: 76px;
}

.buttons {
    /* Center vertically and horizontally */
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    height: 75%;
    display: flex;
    justify-content: space-evenly;
    margin-top: 10%;
}

.newuser-btn,
.create-btn {
    font-size: 72px;
}

.main-content {
    position: relative;
}

html {
    background-color: #1d1d1d !important;
}

.random-database-btn {
    position: fixed;
    bottom: 20%;
    font-size: 48px;
    left: 50%;
    right: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 0 30px 1px rgb(1 1 1 / 30%);
    transition: all 0.4s ease-in-out;
    display: none;
}

.random-database-btn:hover {
    font-size: 50px;
}
</style>
