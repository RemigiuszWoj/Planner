<template>
    <section>
        <div class="column is-half">
            <b-field grouped group-multiline>
                <b-button
                    label="Clear checked"
                    type="is-danger"
                    icon-left="close"
                    class="field"
                    @click="checkedRows = []"
                />

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
                        :checkbox-position="checkboxPosition"
                    >
                        <!-- 
                    <template #bottom-left>
                        <b>Total checked</b>: {{ checkedRows.length }}
                    </template>
                    -->
                    </b-table>
                </b-tab-item>
                <!--
                <b-tab-item label="Checked rows">
                    <pre>{{ checkedRows }}</pre>
                </b-tab-item>
                -->
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
                    label: "First Name",
                    centered: true,
                },
                {
                    field: "last_name",
                    label: "Last Name",
                    centered: true,
                },
                {
                    field: "email",
                    label: "Email",
                    centered: true,
                },
                {
                    field: "phone_number",
                    label: "Phone_Number",
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
    },
    computed: {
        ...mapState("user", ["users"]),
    },
};
</script>
