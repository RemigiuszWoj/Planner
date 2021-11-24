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
            <div class="min-time">
                <span class="text">Best calculated time: </span
                ><span class="wynik">{{ this.optimalTime }}</span>
            </div>
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
                            </b-table>
                        </b-tab-item>
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
                    field: "adress",
                    label: "Adress",
                    centered: true,
                },
                {
                    field: "visit_start",
                    label: "Visit start",
                    centered: true,
                },
                {
                    field: "visit_stop",
                    label: "Visit stop",
                    centered: true,
                },
            ],
        };
    },

    created() {
        this.fetchUsers();
        this.optimalTime = this.output.min_time;
        this.data1 = this.output.doc1;
        this.data2 = this.output.doc2;
        this.start_doc1 = this.output.start_doc1;
        this.start_doc2 = this.output.start_doc2;
        this.stop_doc1 = this.output.stop_doc1;
        this.stop_doc2 = this.output.stop_doc2;

        for (let i = 0; i < this.data1.length; i++) {
            this.data1[i]["visit_start"] = this.start_doc1[i];
            this.data1[i]["visit_stop"] = this.stop_doc1[i];
        }
        for (let i = 0; i < this.data2.length; i++) {
            this.data2[i]["visit_start"] = this.start_doc2[i];
            this.data2[i]["visit_stop"] = this.stop_doc2[i];
        }
    },
    methods: {
        ...mapActions("user", ["fetchUsers"]),
        redirect_to_mainmenu() {
            this.$router.push("/Plans");
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

.field-body .field #flex-row-btns {
    padding-left: 18px !important;
    padding-top: 20px !important;
}

.min-time {
    margin-top: 10px;
    margin-left: auto;
    margin-right: auto;
    width: 200px;
    padding: 5px;
    text-align: center;
    vertical-align: middle;
    transform: translateX(-45px);
}

.text {
    vertical-align: middle;
    font-size: 20px;
}

.wynik {
    font-size: 30px;
    color: #7fff00;
}
</style>
