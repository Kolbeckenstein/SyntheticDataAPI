#git clone https://github.com/Kolbeckenstein/SyntheticDataAPI.git
# git clone https://github.com/synthetichealth/synthea.git


# apt-get install openjdk-17-jre-headless openjdk-13-jdk-headless pipenv uvicorn jq
apt-get update || apt-get upgrade || apt-get install docker 
./setup_docker_group.sh
# ./start.sh
# pipenv install
./start.sh
