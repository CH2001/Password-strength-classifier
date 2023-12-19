# Password-strength-classifier

## About 
A password strength classifier is essential for bolstering cybersecurity. With increasingly sophisticated cyber threats, enforcing robust password policies is paramount. This project helps users identify and enhance the resilience of their passwords, promoting secure online practices. By categorizing passwords into low, moderate, and high strengths, individuals and organizations can proactively fortify their digital defenses, mitigating the risk of unauthorized access and potential data breaches. Linear SVC model performs the best with F1-score of 0.64. 
## Summary 
Data visualization | Model building | Model deployment 

## How to run? 
**Run locally**
1. Run `docker pull python:3.10.4-slim` to download the python image image from the Docker Hub registry to local machine. 
2. Run `docker build -t <name>:<tag-optional> .` to build docker image.
3. Run `docker run -it -p <port>:<port> <name>:<tag-optional>` to build docker image. Can use 8081 as port if available in system. 

**Deploy**
1. On the same folder, run `eb init -p docker <name>` to initialize an Elastic Beanstalk environment for a Docker application. Make sure an AWS account has been created as `aws-access-id` and `aws-secret-key` would be prompted.
2. Run `eb create <name>` to create a new environment the application. 
3. Run `eb terminate <name>` to stop and delete existing Elastic Beanstalk environment after finish testing.

## Sample results/ output
![image](https://github.com/CH2001/Password-strength-classifier/assets/65500133/b3dec2d5-79b0-40ef-8369-0994b000eab6)

## Links 
Dataset: [Password strength dataset]([https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset])
