import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Sidebar from "../views/Sidebar.vue";

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
];

const router = new VueRouter({
    routes,
});

export default router;
