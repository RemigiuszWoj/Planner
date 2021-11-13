<template>
    <section>
        <b-loading is-full-page v-model="loading" :can-cancel="true"></b-loading>
        <b-field>
            <div class="flex-row-btns">
                <b-button
                    label="Clear checked"
                    type="is-danger"
                    class="clear-btn"
                    @click="checkedRows = []"
                    rounded
                    outlined
                />
                <b-button
                    label="Main menu"
                    type="is-success"
                    class="main-menu-btn"
                    rounded
                    @click="redirect_to_mainmenu()"
                />
                <b-button
                    label="Calculate"
                    type="is-primary"
                    class="submit-btn"
                    rounded
                    @click="submit()"
                />
            </div>
        </b-field>
        <div class="table">
            <div class="all_table">
                <b-tabs>
                    <b-tab-item label="patient_table">
                        <b-table
                            :data="data"
                            :columns="columns1"
                            :checked-rows.sync="checkedRows"
                            checkable
                        >
                        </b-table>
                    </b-tab-item>
                </b-tabs>
            </div>
        </div>
    </section>
</template>

<script>
import api from "@/services/api";
import userService from "@/services/userService";
import { mapActions, mapState } from "vuex";

export default {
    data() {
        return {
            data: [],
            checkedRows: [],
            checkboxPosition: "left",
            returnedUsers: [],
            loading: false,
            columns1: [
                {
                    field: "id",
                    label: "ID",
                    width: "40",
                    numeric: true,
                },
                {
                    field: "first_name",
                    label: "First name",
                    centered: true,
                },
                {
                    field: "last_name",
                    label: "Last name",
                    centered: true,
                },
                {
                    field: "phone_number",
                    label: "Phone number",
                    centered: true,
                },
                {
                    field: "visit_time",
                    label: "Visit time",
                    centered: true,
                },
            ],
        };
    },

    mounted() {
        api.get("user/").then((response) => (this.data = response.data));
    },
    computed: {
        ...mapState("user", ["users", "output"]),
    },
    methods: {
        ...mapActions("user", ["calculateRoutes"]),

        redirect_to_mainmenu() {
            this.$router.push("/");
        },
        async submit() {
            this.loading = true;
            this.calculateRoutes(this.checkedRows);
        },
        calculateRoutes(data) {
            userService
                .calcUsers(data)
                .then((output) => {
                    this.loading = false;
                    this.$store.commit("user/setOutput", output.data);
                })
                .finally(() => {
                    this.$router.push("/Route");
                });
        },
    },
};
</script>

<style scoped>
.flex-row-btns {
    display: flex;
    justify-content: space-between;
    padding: 3px 0 10px 5px;
}

.clear-btn {
    box-shadow: 0 0 30px 1px rgb(1 1 1 / 30%);
    transition: all 0.6s ease-in-out;
}

.clear-btn:hover {
    font-size: 17px;
}

.main-menu-btn {
    box-shadow: 0 0 30px 1px rgb(1 1 1 / 30%);
    transition: all 0.6s ease-in-out;
}

.submit-btn {
    box-shadow: 0 0 30px 1px rgb(1 1 1 / 30%);
    transition: all 0.6s ease-in-out;
}

.submit-btn:hover {
    font-size: 17px;
}

.main-menu-btn:hover {
    font-size: 17px;
}

.flex-row-btns {
    margin: 20px 10px 0px 10px;
}
</style>
