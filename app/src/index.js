const path = require("path");
const express = require("express");
const morgan = require("morgan");
const dotenv = require("dotenv");

// Load environment variables from file if present
const envFile = process.env.ENV_FILE || `.env.${process.env.NODE_ENV || "dev"}`;
dotenv.config({ path: path.join(__dirname, "..", envFile) });

const app = express();
const port = process.env.PORT || 3000;

// Basic request logging with level from env
app.use(
  morgan(process.env.LOG_LEVEL === "debug" ? "dev" : "combined", {
    skip: () => process.env.LOG_LEVEL === "error",
  })
);

app.get("/", (_req, res) => {
  res.json({
    message: "Hello from multi-env pipeline demo",
    environment: process.env.NODE_ENV || "dev",
    config: {
      debug: process.env.DEBUG === "true",
      logLevel: process.env.LOG_LEVEL,
      dbUrl: process.env.DB_URL,
    },
  });
});

app.listen(port, () => {
  console.log(
    `Server running on port ${port} with NODE_ENV=${process.env.NODE_ENV || "dev"}`
  );
});


