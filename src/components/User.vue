<template #default="props">
    <section>
        <form method="post">
            <div class="modal-card" style="width: auto">
                <header class="modal-card-head">
                    <p class="modal-card-title">Add User</p>
                    <button type="button" class="delete" @click="$parent.close()" />
                </header>
                <section class="modal-card-body">
                    <b-field label="Name">
                        <b-input
                            v-model="firstName"
                            type="text"
                            placeholder="Enter your name"
                            required
                        >
                        </b-input>
                    </b-field>

                    <b-field label="Surname">
                        <b-input
                            v-model="lastName"
                            type="text"
                            placeholder="Enter your surname"
                            required
                        >
                        </b-input>
                    </b-field>

                    <b-field label="Phone number">
                        <b-input
                            v-model="phoneNumber"
                            type="text"
                            placeholder="Enter your phone number"
                            required
                        >
                        </b-input>
                    </b-field>

                    <b-field label="Email">
                        <b-input
                            type="email"
                            v-model="email"
                            placeholder="Your email"
                            required
                        >
                        </b-input>
                    </b-field>

                    <b-field label="Position">
                        <b-input
                            type="text"
                            v-model="xPosition"
                            placeholder="X-Position"
                            required
                        >
                        </b-input>

                        <b-input
                            type="text"
                            v-model="yPosition"
                            placeholder="Y-Position"
                            required
                        >
                        </b-input>
                    </b-field>
                </section>
                <footer class="modal-card-foot">
                    <b-button
                        label="Register Now"
                        type="is-primary"
                        @click="createUser"
                    />
                    <b-button label="Close" @click="$parent.close()" />
                </footer>
            </div>
        </form>
    </section>
</template>
<script>
import userService from "@/services/userService.js";

export default {
    data() {
        return {
            firstName: "",
            lastName: "",
            email: "",
            phoneNumber: "",
            xPosition: "",
            yPosition: "",
        };
    },
    methods: {
        createUser() {
            let data = {
                first_name: this.firstName,
                last_name: this.lastName,
                email: this.email,
                phone_number: this.phoneNumber,
                x: this.xPosition,
                y: this.yPosition,
            };
            userService
                .createUser(data)
                .then(() => {
                    this.$buefy.notification.open({
                        duration: 2000,
                        message: "User was created!",
                        type: "is-success",
                    });
                })
                .catch((err) => {
                    this.$buefy.notification.open({
                        duration: 3000,
                        message: err.data,
                        type: "is-danger",
                    });
                });
        },
    },
};
</script>

<style></style>
