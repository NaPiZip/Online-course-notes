<img src="https://blog.scottlogic.com/dsmith/assets/featured/aws-logo.png" alt="AWS logo" height="42px" width="84px" align="left"><br>

# AWS Foundational Level Notes
<div>
    <a href="https://github.com/NaPiZip/Tipps-and-tricks">
        <img src="https://img.shields.io/badge/Document%20Version-0.0.1-brightgreen"/>
    </a>  
</div>

## List of Tutorials
This section lists some tutorials which I did, some of them are not worth doing it but everyone needs to decide on that by himself. The recommendable list is already ordered in a way I would start with the tutorials if I don't have any experience with AWS at all. The AWS training and certification platform provides some good tutorial to start with, see [here](https://www.aws.training/LearningLibrary?filters=classification%3A6&filters=language%3A1&search=&tab=digital_courses).

**Not worth the pain:**
- Introduction to AWS Inferentia and Amazon EC2 Inf1 Instances

**Recommendable:**
- IAM Best Practices
- The AWS Well-Architected Framework
- Introduction to AWS Inferentia and Amazon EC2 Inf1 Instances
- AWS Cloud Practitioner Essentials (Second Edition): Introduction to the AWS Cloud
- AWS Cloud Practitioner Essentials (Second Edition): Module 4 Architecture

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

### AWS Cloud Practitioner Essentials (Second Edition): Introduction to the AWS Cloud
The key concept of the cloud is the on-demand content delivery of IT resources. Before cloud computing, it was important to host own server and recourses, which meant a lot of architectural design choices had to be made in advance, which needed a lot of work up front as well as assumptions which where likely to change during the product development live cycle. Cloud computing introduced `elasticity` the possibility to adapt infrastructure on demand. This lead to reducing operational risks and increasing flexibility and scalability also known as `agility`.

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
Fault tolerant database, via automated back ups, snapshot and multi availability zone deplo  


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


### Javapoint AWS-Tutorial
Tis tutorial is giving a overall overview of the most important things of AWS for a beginner.





To Do:
https://www.javatpoint.com/aws-tutorial
https://www.guru99.com/aws-tutorial.html


### Not worth doing: Introduction to AWS Inferentia and Amazon EC2 Inf1 Instances
[AWS Inferentia](https://www.aws.training/Details/Video?id=42195) covers machine learning inference processing challenges. This video gives just a brief introduction into the `AWS Inf1` service, its more of an sales pitch, thus barely having technical information.


## Overview of most important AWS services

## Contributing
To get started with contributing to my GitHub repository, please contact me [Slack](https://join.slack.com/t/napi-friends/shared_invite/enQtNDg3OTg5NDc1NzUxLWU1MWNhNmY3ZTVmY2FkMDM1ODg1MWNlMDIyYTk1OTg4OThhYzgyNDc3ZmE5NzM1ZTM2ZDQwZGI0ZjU2M2JlNDU).
