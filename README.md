# End to end Text-Summarizer-Project

Link for the data = https://github.com/shivdattaredekar/TextSummarizer/raw/main/samsum.zip

Workflows
Update config.yaml
Update params.yaml
Update entity
Update the configuration manager in src config
update the conponents
update the pipeline
update the main.py
update the app.py

How to run?
STEPS:
Clone the repository

https://github.com/entbappy/End-to-end-Text-Summarization

STEP 01- Create a conda environment after opening the repository
conda create -n summary python=3.8 -y
conda activate summary
STEP 02- install the requirements
pip install -r requirements.txt
# Finally run the following command
python app.py
Now,

# open up you local host and port
Author: shivdatta redekar
Data Scientist
Email: shivdattaredekar@gmail.com

# AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


# Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

# Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 058264298927.dkr.ecr.ap-south-1.amazonaws.com/text-s
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker


6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one

7. Setup github secrets:
    =

AWS_SECRET_ACCESS_KEY=

AWS_REGION = ap-south-1

AWS_ECR_LOGIN_URI = demo>>  058264298927.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = text-s


