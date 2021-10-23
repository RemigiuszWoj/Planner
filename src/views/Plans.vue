<template>
    <section>
        <div class="column is-half">
            <b-field>
                <div class="flex-row-btns">
                    <b-button
                        label="Clear checked"
                        type="is-danger"
                        class="clear-btn"
                        @click="checkedRows = []"
                        rounded="true"
                        outlined="true"
                    />
                    <b-button
                        label="Main menu"
                        type="is-success"
                        class="main-menu-btn"
                        rounded="true"
                        @click="redirect_to_mainmenu()"
                    />
                    <b-button
                        label="Submit"
                        type="is-primary"
                        class="submit-btn"
                        rounded="true"
                    />
                </div>

                <!-- Comment 
            <b-select v-model="checkboxPosition">
                <option value="left">Checkbox at left</option>
                <option value="right">Checkbox at right</option>
            </b-select>
            -->
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
//import userService from "@/services/userService";
import { mapActions, mapState } from "vuex";
export default {
    data() {
        return {
            data: [],
            checkedRows: [],
            checkboxPosition: "left",
            //checkedRows: [data[1], data[3]],
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
        //this.data = this.users;
    },
    methods: {
        ...mapActions("user", ["fetchUsers"]),
        redirect_to_mainmenu() {
            this.$router.push("/");
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
