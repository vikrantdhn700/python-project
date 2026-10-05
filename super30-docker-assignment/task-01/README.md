Task 01 — Pull latest Ubuntu and run interactively

Commands:

```powershell
# Pull latest Ubuntu image
docker pull ubuntu:latest

# Run an interactive container
docker run --rm -it ubuntu:latest bash
```

Inside the container, run at least five Linux commands, e.g.:

```sh
ls -la
pwd
whoami
apt-get update
uname -a
```