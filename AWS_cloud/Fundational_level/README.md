<img src="https://blog.scottlogic.com/dsmith/assets/featured/aws-logo.png" alt="AWS logo" height="42px" width="84px" align="left"><br>

# AWS Foundational Level Notes
<div>
    <a href="https://github.com/NaPiZip/Tipps-and-tricks">
        <img src="https://img.shields.io/badge/Document%20Version-0.0.1-brightgreen"/>
    </a>  
</div>

## List of Tutorials
This section lists some tutorials which I did, some of them are not worth doing it but everyone needs to decide on that by himself. The recommendable list is already ordered in a way I would start with the tutorials if I don't have any experience with AWS at all.

**Not worth the pain:**
- Introduction to AWS Inferentia and Amazon EC2 Inf1 Instances

**Recommendable:**
- IAM Best Practices
- The AWS Well-Architected Framework
- Introduction to AWS Inferentia and Amazon EC2 Inf1 Instances
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
