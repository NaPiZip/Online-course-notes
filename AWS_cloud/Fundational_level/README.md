<img src="https://blog.scottlogic.com/dsmith/assets/featured/aws-logo.png" alt="AWS logo" height="42px" width="84px" align="left"><br>

# AWS Foundational Level Notes
<div>
    <a href="https://github.com/NaPiZip/Tipps-and-tricks">
        <img src="https://img.shields.io/badge/Document%20Version-0.0.1-brightgreen"/>
    </a>  
</div>

## List of Tutorials
This section lists some tutorials which I did, some of them are not worth doing it but everyone needs to decide on that by himself. The recommendable list is already ordered in a way I would start with the tutorials if you don't have any experience with AWS at all. The AWS training and certification platform provides some good tutorials to start with, see [here](https://www.aws.training/LearningLibrary?filters=classification%3A6&filters=language%3A1&search=&tab=digital_courses).

**Not worth the pain:**
- Introduction to AWS Inferentia and Amazon EC2 Inf1 Instances

**Recommendable:**
- IAM Best Practices
- The AWS Well-Architected Framework
- AWS Cloud Practitioner Essentials (Second Edition): Module 1 - 6

- Javapoint AWS-Tutorial

### IAM Best Practices
The very first thing to do is to understand the IAM Best Practices. In order to make sure that your AWS account is set up securely, you should work through the following article, see [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials).

The bare minimum is listed here:
- Lock Away Your AWS Account Root User Access Keys
- Create Individual IAM Users
- Use Groups to Assign Permissions to IAM Users
- Grant Least Privilege

I would recommend in creating 2 users an `admin` as well as an `experimental` one whit less privileges, the `admin` should use MFA.

### The AWS Well-Architected Framework
What is the [Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)?  What is important to know? What should I keep in mind?</br>
The WAF contains best practices and ways to measure your architecture design. It focuses onto five different areas:
- [Operational excellence](https://d1.awsstatic.com/whitepapers/architecture/AWS-Operational-Excellence-Pillar.pdf)
 Understand business and customer needs, also create supporting processes which should be able to evolve.
- [Security](https://d1.awsstatic.com/whitepapers/architecture/AWS-Security-Pillar.pdf)
Protect information and system using detective controls, data protection, access management, and incident response.
- [Reliability](https://d1.awsstatic.com/whitepapers/architecture/AWS-Reliability-Pillar.pdf)
The ability to recover from failure.
- [Performance efficiency](https://d1.awsstatic.com/whitepapers/architecture/AWS-Performance-Efficiency-Pillar.pdf)
The ability to use computing resources efficiently.
- [Cost effectiveness](https://d1.awsstatic.com/whitepapers/architecture/AWS-Cost-Optimization-Pillar.pdf)
Avoid unneeded cost with the help of e.g. auto scaling.

The key is to understand `design decisions in a cloud native way` and it's impact, by providing general design principles.

The course can be found [here](https://www.aws.training/Details/eLearning?id=42036).

### AWS Cloud Practitioner Essentials (Second Edition): Module 1 Introduction to the AWS Cloud
The key concept of the cloud is the on-demand content delivery of IT resources. Before cloud computing, it was important to host own server and resources, which meant a lot of architectural design choices had to be made in advance, which needed a lot of work up front as well as assumptions which where likely to change during the product development live cycle. Cloud computing introduced `elasticity` the possibility to adapt infrastructure on demand. This lead to reducing operational risks and increasing flexibility and scalability also known as `agility`.

AWS offers tree ways to create and manage resources.:

- AWS Management Console
  Graphical interface web browser based.
- AWS Command Line Interface (CLI)
  Interface which is programming language-agnostic.
- AWS software development kits (SDKs)
  Integration into different programming languages.

The course can be found [here](https://www.aws.training/Details/eLearning?id=29699).

### AWS Cloud Practitioner Essentials (Second Edition): Module 2 AWS Core Services
This module talks about key services and their common uses cases, covering the following services:
- Elastic Compute Cloud (EC2)
A service which spins off virtual machines.
- Elastic Block Store (EBS)
A storage device for EC2 instances.
- Simple Storage Service (S3)
A standalone storage service.
- Virtual Private Cloud (VPC)
Isolate networks of services within the cloud.

This module shows a lot of set up using the AWS Management Console which I will not be covering.

The course can be found [here](https://www.aws.training/Details/eLearning?id=29700).

### AWS Cloud Practitioner Essentials (Second Edition): Module 3 AWS Integrated Services
The integrated services module focuses on services which are helpful for managing, logging or scaling to truly provide the power of the cloud, see [here](https://www.aws.training/Details/eLearning?id=29701) for details.

**Application Load Balancer**
A common load balancer distributes workloads across multiple computing resources or in our case services. A example use case, is the ability to use container to host micro services and route to those services on the same EC2 instance but on different ports, via setting up routing routes.

- Listeners
A process who checks for a specified connection requests.
- Target
A destination for traffic, based on the setup rules.
- Target Group
A collection of targets for the load balancer.


**Auto Scaling**
Ensure to have the right amount of EC2 instance running, based on the application need, e.g. a maximum CPU utilization threshold as trigger. Auto scaling needs tree elements:
- Launch Configuration
Defines what will be launched, what kind of EC2 instance and what image does it have.
- Auto Scaling Group
Defines where and what the boundaries of the deployment are.
- Auto Scaling Policy
Describes when the auto scaling happens, or on what events.

**Route 53**
Is a basic DNS (Domain Name System) service which provides domain names for IP routes of AWS services endpoints.

**Amazon Relational Database Services (RDS)**
Provides a database instance running a preferred database stack. There is no need for managing the instance OS, storage and scaling, since the service provides build in measures.

**AWS Lambda**
Is a compute service which lets you run code without managing instances. It uses a event driven execution policy. It can be used for server less applications, or as simple executors.

**AWS Elastic Bean Stalk**
A platform as a service system for launching apps with as minimal overhead as possible. "With Elastic Beanstalk, you can quickly deploy and manage applications in the AWS Cloud without having to learn about the infrastructure that runs those applications. Elastic Beanstalk reduces management complexity without restricting choice or control. You simply upload your application, and Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.", source can be found [here](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html).

**Simple Notification Service (SNS)**
Is a messaging and notification service. "Amazon Simple Notification Service (Amazon SNS) is a web service that coordinates and manages the delivery or sending of messages to subscribing endpoints or clients. In Amazon SNS, there are two types of clients—publishers and subscribers—also referred to as producers and consumers.", see source [here](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).

**Amazon CloudWatch**
Is a monitoring system for tracking various information such as CPU utilization, data transfer, monitor services ... It can be used to trigger alarms via SNS or for auto scaling events. CloudWatch can also create logs in real time.

**Amazon CloudFront**
Is a content delivery network (CDN) which caches content, such that the content is faster accessible in different regions.

**Amazon CloudFormation**
A fully managed service to create stacks consisting of different resource types such as EC2 instances, VPC, databases ... Its one of the most powerful tools of AWS.


### AWS Cloud Practitioner Essentials (Second Edition): Module 4 Architecture
The architecture module describes the 5 pillars of the `Well-Architected-Framework` in a very brief manner which consists of the following five pillars (the tutorial can be found [here](https://www.aws.training/Details/eLearning?id=29702)):
- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Operational Excellence

For more details take a look at the [Well-Architected-Framework](https://www.aws.training/Details/eLearning?id=42036) tutorial.

**Fault Tolerance**
The ability for a system to maintain operational after faults, build in redundant manner. The following services can be used to increase the fault tolerance:
- Simple Queue Service SQS
Messages system for distribution of notifications.
- Simple Storage Service S3
Fault tolerant redundant data storage.
- Relational Database Service RDS
Fault tolerant database, via automated back ups, snapshot and multi availability zones for deployment.  


**High Availability**
System is always functioning, with as less down time as possible. This can be achieved with multiple server, on different regions as well availability zones. The following services can be used to increase the availability:
- Elastic Load Balancer
Distributes incoming loads between instances.
- Elastic IP Address
Static IP's for masking failure between resources.
- Route 53
DNS service for translating domain names and IP addresses.
- Auto Scaling
Launching and terminating instances based on events.
- CloudWatch
Monitoring of events, by creating metrics.

### AWS Cloud Practitioner Essentials (Second Edition): Module 5 AWS Security
This tutorial covers a basic introduction into security and the shared responsibility model.

**Shared Responsibility Model**
The application stack gets divided into several pieces depending on if AWS or the app owner is responsible for securing. The key concept lies in the fact that the responsibility is shared between owner and AWS, such that both parties have to make sure security measures are given. The tutorial can be found [here](https://www.aws.training/Details/eLearning?id=29703).

<center>

|  User Data  |
|:-----------:|
| Application |
|   Guest OS  |
|  Hypervisor |
|   Network   |
|   Physical  |

</center>

Amazon is ensuring that the data centers are <b>physical</b> secured using access control, security guards as, cameras etc. The <b>network</b> is also covered by Amazon. Amazon does not provide a lot of information about these two topics due to security concerns, AWS is certified by third parties which can be found [here](https://aws.amazon.com/compliance/). <b>Hypervisor</b> is [Xen](https://en.wikipedia.org/wiki/Xen) based and also disclosed by Amazon. The user is responsible for the <b> guest OS, application and user data</b>.

**Identity and Access Management IAM**
Describes user, groups, roles and policies:
- User
Is a permanent named operator.
- Group
Is a collection of users.
- Role
Is not a permission, it is an authentication method which is temporarily.
- Policy
Are permissions sets which defines actions among user, group, and roles.

**Amazon Inspector**
Is an automated security assessment service, it helps to identify security issues and vulnerabilities in order to asses compliance. "Amazon Inspector helps you discover potential security issues by using security rules to analyze your AWS resources. Amazon Inspector monitors and collects behavioral data (telemetry) about your resources. The data includes information about the use of secure channels, network traffic among running processes, and details of communication with AWS services.", see reference [here](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_assessments.html).

**AWS Shield**
AWS shield is a managed DDos protection service. Web application firewalls WAFs can be used in order to complement application layer based attacks. Traffic analysis, anomaly detection and different measures are used to prevent downtime.


### AWS Cloud Practitioner Essentials (Second Edition): Module 6 Pricing and Support
This module describes the way how pricing works on AWS, see [here](https://www.aws.training/Details/eLearning?id=29704) for the tutorial. AWS pricing is dependent on the type of service you choose and many other factors, such as:
- Outbound data transfer
- Machine type
- Region
- Storage size
- etc.

The most important thing is to check the costs up front depending on the service, a link can be found [here](https://aws.amazon.com/pricing/).

**AWS Trusted Advisor**
It is a service which helps to uncover cost saving potential, performance issues, security issues as well as fault tolerance problems. Its main goal consists of optimizing usage.

### Run a Serverless "Hello, World!"
This hands on example shows how to run a serverless function using the AWS Lambda service. The descriptions can be found [here](https://aws.amazon.com/getting-started/tutorials/run-serverless-code/?trk=gs_card&e=gs&p=gsrc). The tutorial is pretty straight forward but there are a couple of questions coming up in my mind:
- What is a real use case?
- How can I trigger a lambda function with custom input?
- How can I access different services within a lambda?

I found a blog addressing some of my questions, see [www.contino.io](https://www.contino.io/insights/5-killer-use-cases-for-aws-lambda). The suggested use cases are:
- Operating serverless websites
- Log analysis on the fly
- Automated backups and everyday tasks
- Processing uploaded S3 objects
- Filtering and transforming data on the fly

The first point sounds very interesting to me, hosting a websites on S3 and serving the dynamic content with the help of an RDS and embedded HTTPS API calls. I will try to set up an example.

@TODO S3, RDS and Lambda hosted static website with lambda invocation for serving dynamic content.
starting point is [here](https://d0.awsstatic.com/whitepapers/AWS_Serverless_Multi-Tier_Architectures.pdf).

### A bit more practical content using AWS Lambda
Because of the previous tutorial I still had questions about a real use case and wanted more exposure. I think the AWS Lambda function is a good starting point as it provides quick and easy compute access, I decided that the AWS API Gateway getting started would be a good start to get more information about the lambda service. Here is the [link](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html). I am not going into detail since the getting started is pretty self explanatory. And also, a couple of pretty nice tutorial videos, can be found [here](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-videos.html).

### AWS Serveless Application Model (SAM)
The AWS Serverless Application Model (SAM) is an open-source framework for building serverless applications, see [here](https://www.youtube.com/watch?v=CIdUU6rNdk4). The nice thing about it is that you can run it locally and use upload it into Cloud Formation for deployment. To run the SAM tutorial follow the steps below:
  1. Create a new service application
  ```
  $ sam init --runtime python3.8
  ```
  2. Navigate to the `sam-app` dir.
  ```
  $ cd /sam-app
  ```
  3. Build the app
  ```
  $ sam build
  ```
  4. Start the Api
  ```
  $ sam local start-api -t template.yaml
  ```
  5. Interact with the app
  ```
  $ curl http://127.0.0.1:3000/hello
  {"message": "hello world"}
  ```
*Note:*
Sometimes while building the following error message occurs:
  ```
  $sam build                Building resource 'DetectTextInImage'

  Build Failed
  Error: PythonPipBuilder:None - Binary validation failed!
  ```
Use run the build using the debug option `--debug`. The debug message showed the issue:
```
...
Expected version: python3.6, Found version: C:\Program Files\Python38\python.EXE.
...
```
The problem is that the python version needs to be the same on the local platform and as defined in `template.yaml`.

### Small project: S3 image OCR parser with AWS Lambda
I would like to invoke a lambda when a file gets uploaded to a S3 bucket, the lambda should perform an action on the file. A pretty good example can be found [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-s3.html). I am using `localstack` for testing purposes. `localstack` is a nice tool for running AWS services locally, see [link](https://localstack.cloud/). This comes in handy for development, so you don't have to actually use the paid AWS service.

  <p align="center">
  <img src="https://localstack.cloud/images/diagram.png" alt="localstack example"/></p>

  The exercise contains of the following tasks:
  1. Trigger lambda on file upload in S3.
   `sam local invoke --event SampleEvent.json` [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-s3.html#serverless-example-s3-test-locally).
  2. Lambda display file information e.g. file name and type, but using a local s3 endpoint.
  ```python
    s3 = boto3.resource('s3', endpoint_url = 'http://192.168.99.100:4572',
                              aws_access_key_id     = 'AccessKey',
                              aws_secret_access_key = 'SecertKey')

    bucket = s3.Bucket('my-bucket')

    def lambda_handler(event, context):
      for obj in bucket.objects.all():
            print(obj.key)
            # display content
            print(obj.get()['Body'].read().decode(encoding="utf-8",errors="ignore"))
  ```
  3. Lambda download file locally file.
  4. Lambda perform operation on file.
  5. Lambda save operation result in special S3 location.





### The AWS recommended learning path
A link can be found [here](https://d1.awsstatic.com/training-and-certification/ramp-up-guides/RampUp_Developer_122019_final.pdf). Some content was already covered in the previous tutorials, because of that I am only covering new content.

#### Phase 0: Overview of Amazon Web Services
See [here](https://d1.awsstatic.com/whitepapers/aws-overview.pdf). Some helpful definitions are:

**Cloud Computing Models**
Infrastructure as a Service (IaaS)
Provides building blocks of IT infrastructure like virtual or dedicated hardware and storage.

Platform as a Service (PaaS)
Removes the need for organizing the underneath infrastructure. It provides the environment where the software is executed.

Software as a Service (SaaS)
SaaS is most commonly know as the provision of a software product which is hosted and maintained by the vendor e.g. a web based e-mail client.

#### Phase 1: Architecting for the Cloud AWS Best Practices
See [here](https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf). This whitepaper introduces best practices and design patterns particular tailored for cloud development. Most stuff is pretty generic and I am only capturing a couple things which I thought stand out.

**Differences Between Traditional and Cloud Computing Environments**
In a traditional computing environment, capacity is based on an estimation of the theoretical maximal peak usage. Where as in cloud computing you could dynamically scale based on current usage. In cloud computing you optimize for performance as well as for costs, not only focus on the functional architecture is important.

**Design Principles**
Some key principle of the AWS Cloud include scalability, disposable resources, automation, loose coupling. Some important elements to keep track off are:
  - Scalability
  Support the growth in users, traffic and data size, without loosing performance. Either by scaling horizontally, e.g. with the help of more instances or by scaling vertically by using a more performant instance.
  - Stateless applications
  A stateless app is an app which does not need knowledge of previous operations, and thus can easily scale horizontally.
  - Distribute loads
  A push model e.g. an Elastic Load Balancer (ELB) can help to distribute traffic. A pull model can be used with the help of a Simple Queue Service (SQS), processing asynchronous events.
  - Distributed processing
  Divide big loads of data processing into smaller work loads.
  - Automate bootstrapping
  Scripts which install software, copy dat or bring instances into a certain state. Golden images can be created form Elastic Block Storage (EBS), also Amazon Machine Images (AMI) can be generated for faster scaling.
  - Loose coupling
  A desirable attribute of an IT system is that it can be broken into smaller, loosely coupled components. Design in a way which reduces dependencies.  


### Javapoint AWS-Tutorial
Tis tutorial is giving a overall overview of the most important things of AWS for a beginner.

To Do:
https://www.javatpoint.com/aws-tutorial
https://www.guru99.com/aws-tutorial.html

## Overview of most important AWS services


### Not worth doing: Introduction to AWS Inferentia and Amazon EC2 Inf1 Instances
[AWS Inferentia](https://www.aws.training/Details/Video?id=42195) covers machine learning inference processing challenges. This video gives just a brief introduction into the `AWS Inf1` service, its more of an sales pitch, thus barely having technical information.

[Job Roles in the Cloud](https://www.aws.training/Details/eLearning?id=11987).
This tutorial describes roles in the AWS cloud, I think this tutorial is not adding to much value, since the roles are not important for learning the usage of the AWS cloud.

## Contributing
To get started with contributing to my GitHub repository, please contact me [Slack](https://join.slack.com/t/napi-friends/shared_invite/enQtNDg3OTg5NDc1NzUxLWU1MWNhNmY3ZTVmY2FkMDM1ODg1MWNlMDIyYTk1OTg4OThhYzgyNDc3ZmE5NzM1ZTM2ZDQwZGI0ZjU2M2JlNDU).
