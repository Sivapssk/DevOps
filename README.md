# Multi-Environment Dev/Test/Prod Demo

Simple Express app demonstrating environment-based configuration, Dockerization, and GitHub Actions CI/CD for dev, test, and prod.

## Layout
- `app/src/index.js`: Express app that reads env vars (port, debug, log level, DB URL).
- `app/.env.dev|.env.test|.env.prod`: Environment-specific configs.
- `app/Dockerfile`: Container build (ARG `NODE_ENV`).
- `.github/workflows/*.yml`: CI/CD pipelines for each environment.

## Run locally
```bash
cd app
npm install
npm run dev           # uses .env.dev defaults via NODE_ENV
NODE_ENV=test node src/index.js   # or set ENV_FILE=.env.test
```

## Build & run with Docker
```bash
cd app
docker build -t myapp:dev --build-arg NODE_ENV=development .
docker run --env-file .env.dev -p 3000:3000 myapp:dev
```

## Workflows
- `dev-deploy.yml`: on push to `dev`; install, test, build, push image, placeholder deploy.
- `test-deploy.yml`: on push to `test`; install, test, audit, build, push image, placeholder deploy.
- `prod-deploy.yml`: on push to `main` or release; install, test, build, push image, placeholder deploy/notify.

Replace the placeholder deploy steps with your target (SSH to EC2, kubectl apply to namespaces `dev|test|prod`, etc.). Use secrets for registry credentials, SSH keys, kubeconfig, and any API keys.

