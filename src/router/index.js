import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Plans from "../views/Plans.vue";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/plans",
        name: "Plans",
        component: Plans,
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
