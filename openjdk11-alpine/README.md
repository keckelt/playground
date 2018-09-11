# New Repo
I moved this to a separate repo: https://github.com/keckelt/openjdk11-alpine

----



# Build
```
docker build -t alpine-jdk11 .
```


# Run
Run interactive (`-i`) to use jshell:
```
docker run -it alpine-jdk11
```
## JShell
Leave:
```
/exit 0
```

# Usage with docker compose
You can reference the Dockerfile in `build` and launch your jar via `command`:
```
version: '2.0'
services:
  jar_container:
    build:
      context: https://github.com/keckelt/playground.git#:openjdk11-alpine
    volumes:
      - './hello_world.jar:/Main.jar'
    command: java -jar /Main.jar
```
docker-compose.yml
