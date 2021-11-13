import axios from "axios";
import Cookies from "js-cookie";

export default axios.create({
    baseURL: "/api",
    timeou: 0,
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": Cookies.get("csrftoken"),
    },
});
