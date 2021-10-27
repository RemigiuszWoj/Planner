<template>
    <section>
        <div class="column is-full">
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
                        label="Submit"
                        type="is-primary"
                        class="submit-btn"
                        rounded
                        @click="submit()"
                    />
                </div>
            </b-field>

            <b-tabs>
                <b-tab-item label="Table">
                    <b-table
                        :data="data"
                        :columns="columns"
                        :checked-rows.sync="checkedRows"
                        checkable
                    >
                        <!-- 
                    <template #bottom-left>
                        <b>Total checked</b>: {{ checkedRows.length }}
                    </template>
                    -->
                    </b-table>
                </b-tab-item>

                <!-- <b-tab-item label="Checked rows">
                    <pre>{{ checkedRows }}</pre>
                </b-tab-item> -->
            </b-tabs>
        </div>
    </section>
</template>

<script>
import api from "@/services/api";
import userService from "@/services/userService.js";
import { mapActions, mapState } from "vuex";
export default {
    data() {
        return {
            data: [],
            checkedRows: [],
            checkboxPosition: "left",
            returnedUsers: [],
            columns: [
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
                    field: "email",
                    label: "Email",
                    centered: true,
                },
                {
                    field: "phone_number",
                    label: "Phone number",
                    centered: true,
                },
            ],
        };
    },
    mounted() {
        api.get("user/").then((response) => (this.data = response.data));
    },
    methods: {
        ...mapActions("user", ["fetchUsers"]),
        redirect_to_mainmenu() {
            this.$router.push("/");
        },
        submit() {
            userService.calcUsers(this.checkedRows).then((response) => {
                this.returnedUsers = response.data;
            });
        },
    },
    computed: {
        ...mapState("user", ["users"]),
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
</style>
