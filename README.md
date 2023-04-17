# Rasa Deployment
Deploying Rasa Bot over Google Cloud Platform using Docker.

## Prerequisites:
- Docker
- Docker Compose


## Instructions:

### For deploying over Server:
- Create the VM instance of Ubuntu over Compute Engine
- once the instance is created login to the VM using SSH
- Run the below commands and clone our Docker app:

 - > sudo apt-get update
 
#### 1) Install Docker

- > curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add 
- > sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
- > sudo apt-get update
- >  apt-cache policy docker-ce
- > sudo apt-get install -y docker-ce
- > sudo systemctl status docker
     
#### 2) Install [Docker-Compose](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04)

- > sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

- > sudo chmod +x /usr/local/bin/docker-compose
- > docker-compose --version

#### 3) Clone the Docker App

- > git clone https://github.com/athenasaurav/babblebots_demo.git
- > cd babblebots_demo

#### 4) Build the Docker app and run the services:

- > docker-compose build

It will download the necessary docker images and will build the containers for
us. Once the containers are ready , we can run the following command to
make the containers up in running state:

- > sudo docker-compose up -d

- Check whether the services are up and running using below command:
- > docker ps -a

- Once you see all the services up and running, open the ip address of the machine in the browser and test the bot


#### 5) To update the existing images after re-cloning

Reclone the github with changes

shutdown docker with 

- >docker-compose down

Re build the docker image with 

- >docker-compose build

then just do 

- >docker-compose up -d
