module.exports = {
    outputDir: "dist",
    assetsDir: "static",
    devServer: {
        // proxy: "http://localhost:8000/api",
        proxy: {
            "/api*": {
                target: "http://localhost:8000/",
            },
        },
    },
};
