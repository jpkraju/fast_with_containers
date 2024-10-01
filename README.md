# Dev container setup in vscode
1. Open this project folder in VSCode.
2. Press F1 to open the Command Palette.
3. Type "Dev Containers: Reopen in Container" and select it.

# build container
docker-compose up --build
open app url http://localhost:8000

# docker hub commands for push/pull
docker-compose up --build (if not done yet)

docker login
docker tag fast_with_containers-app jpkraju/fast_with_containers-app:latest
docker push jpkraju/fast_with_containers-app:latest

docker pull jpkraju/fast_with_containers-app:latest
docker run -p 8000:8000 jpkraju/fast_with_containers-app:latest

# use vscode DevContainers to open the linux folder direct access
uvicorn main:app --reload
or 
debugg code with F5

# Docker container stop and start
just close and open vscode to stop/start container in docker-desktop