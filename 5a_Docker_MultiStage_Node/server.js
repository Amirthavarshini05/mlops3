const express = require("express");
const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
    res.send("Node.js Docker Optimization Demo");
});

app.get("/health", (req, res) => {
    res.json({ status: "healthy" });
});

app.listen(PORT, () => console.log(`Server running on ${PORT}`));
