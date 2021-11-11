<template>
    <section>
        <b-field>
            <div id="flex-row-btns">
                <b-button
                    label="Back"
                    type="is-success"
                    class="main-menu-btn"
                    rounded
                    @click="redirect_to_mainmenu()"
                />
            </div>
            <div class="min-time">Optimal time: {{ this.optimalTime }}</div>
        </b-field>
        <div class="column is-half" style="display: inline-block">
            <div class="table">
                <div class="all_table">
                    <b-tabs>
                        <b-tab-item label="Doctor 1">
                            <b-table
                                :data="data1"
                                :columns="columns"
                                :checked-rows.sync="checkedRows"
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
            </div>
        </div>
        <div class="column is-half" style="display: inline-block">
            <div class="table">
                <div class="doctor_table">
                    <b-tabs>
                        <b-tab-item label="Doctor 2">
                            <b-table :data="data2" :columns="columns"> </b-table>
                        </b-tab-item>
                    </b-tabs>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import api from "@/services/api";
import { mapState, mapActions } from "vuex";

export default {
    data() {
        return {
            optimalTime: 0,
            data1: [],
            data2: [],
            checkedRows: [],
            checkboxPosition: "left",
            returnedUsers: [],
            columns: [
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
                {
                    field: "position",
                    label: "Position",
                    centered: true,
                },
            ],
        };
    },

    created() {
        this.splitData();
        api.get("user/").then((response) => {
            this.data1 = response.data;
            for (let i = 0; i < response.data.length; i++) {
                this.data1[i]["position"] =
                    this.data1[i].x.toString() + " / " + this.data1[i].y.toString();
            }
        });
        api.get("user/").then((response) => {
            this.data2 = response.data;
            for (let i = 0; i < response.data.length; i++) {
                this.data2[i]["position"] =
                    this.data2[i].x.toString() + " / " + this.data2[i].y.toString();
            }
        });
    },
    methods: {
        ...mapActions("user", ["fetchUsers"]),
        redirect_to_mainmenu() {
            this.$router.push("/Plans");
        },
        splitData() {
            this.fetchUsers();
            this.optimalTime = this.output.min_time;
            let rangeDoc1 = this.output.doc1;
            let rangeDoc2 = this.output.doc2;
            console.log("doc1: ", rangeDoc1, " doc2: ",rangeDoc2);
            console.log(this.users);
        },
    },
    computed: {
        ...mapState("user", ["users", "output"]),
    },
};
</script>

<style scoped>
.flex-row-btns {
    display: flex;
    justify-content: space-between;
    /* padding: 3px 0 10px 5px; */
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

.min-time {
    margin-top: 1px;
    margin-left: auto;
    margin-right: auto;
    width: 10em;
    border: 3px solid red;
    padding: 5px;
}
</style>
