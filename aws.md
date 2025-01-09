# AWS Notes

## How to build and deploy docker in AWS EKS
### Requirements:
- Build Server
- DockerFile to build the container

### Steps:
- SSH to build server
- pull latest commit
- build container, you can copy from AWS panel
  - `aws configure`, insert access key and secret key
  - `aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 1234.dkr.ecr.ap-southeast-1.amazonaws.com`
  - `docker build --build-arg GIT_COMMIT=$(git rev-parse HEAD) -t project-name .`
  - `docker tag project-name:latest 1234.dkr.ecr.ap-southeast-1.amazonaws.com/project-name:latest`
  - `docker push 1234.dkr.ecr.ap-southeast-1.amazonaws.com/project-name:latest`

## Public access to S3
```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Statement1",
			"Principal": "*",
			"Effect": "Allow",
			"Action": [
				"s3:GetObject"
			],
			"Resource": [
				"arn:aws:s3:::your.domain.name/*"
			]
		}
	]
}``````