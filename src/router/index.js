import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Sidebar from "../views/Sidebar.vue";
import DoctorSite from "../views/DoctorSite.vue";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/sidebar",
        name: "Sidebar",
        component: Sidebar,
    },
    {
        path: "/Doctor",
        name: "DoctorSite",
        component: DoctorSite,
    },
];

const router = new VueRouter({
    routes,
    mode: "history",
});

export default router;
