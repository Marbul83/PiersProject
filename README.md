# DnD
### Deployed app http://35.234.150.82/

## Contents
* [Installation](#Installation)
* [Introduction](#Introduction)
* [Planning](#Planning)
* [Use Cases](#Use)
* [Risk Analysis](#Risk)
* [Front End Design](#Design)
* [Testing](#Testing)
* [CI Pipeline & Deployment](#Deployment)
* [Project Conclusion](#Conclusion)

![Presentation](https://github.com/PCMBarber/PiersProject/blob/master/Media/DnDPresentation.pptx)

<a name="Introduction"></a>
## Introduction
### Project Brief
* To produce a service oriented Flask application, deployed with docker.
* Test application using pytest
* Plan Project using kanban and diagrams
* Fully document and provide installation guide

<a name="Installation"></a>
## Installation
* Set up two VM's using GCP noting the Public IP Address'
* Log in to Gcloud using terminal
* Install ansible
* Clone repository
* Replace IP addresses in "inventory" with your own
* From project root run : "bash .install"

<a name="Planning"></a>
## Planning
Trello was used for initial planning of this project and throughout to keep track. The reason I used this is it is a free and easy to use software
![alt text](https://github.com/PCMBarber/PiersProject/blob/master/Media/Trello.PNG)

<a name="Use"></a>
## Use Cases
These two use cases are currently the only ways to use my app, In the future I would like to implement a user-class system like my previous project, to allow users more control of how they use the app
![alt text](https://github.com/PCMBarber/PiersProject/blob/master/Media/UseCase.PNG)

<a name="Risk"></a>
## Risk Analysis
I identified and treated a number of risks for this project. Only one of the risks occurred (Deployment VM Crashing) and was easily recoved due to the steps I took to mitigate.
![alt text](https://github.com/PCMBarber/PiersProject/blob/master/Media/riskAssesment.PNG)

<a name="Design"></a>
## Design
My app is made up of 4 services communicating using JSON aided by docker, the Front-end serves the user HTML's takes user input and orchestrates the other services. Service1 rolls 8 random numbers, discards the lowest two and returns the remaining 6. Service2 randomly selects a Background for your character and returns it to the Front-end.  The Back-end takes the user inputs and the outputs from service 1 & 2 and uses it to create a user object to the specifications the user has defined.
![alt text](https://github.com/PCMBarber/PiersProject/blob/master/Media/Design.PNG)

My initial ERD diagram contains 3 tables, non of these have relation as they are used purely for datastorage
![alt text](https://github.com/PCMBarber/PiersProject/blob/master/Media/InitialERD.PNG)

The final ERD diagram sees the background table dropped in favour of a code based solution
![alt text](https://github.com/PCMBarber/PiersProject/blob/master/Media/FinalERD.PNG)

<a name="Testing"></a>
## Testing
I am disappointed in the testing suite I have produced. Only being able to test the front-end service. In the future 
![alt text](https://github.com/PCMBarber/PiersProject/blob/master/Media/PytestCov.PNG)

<a name="Deployment"></a>
## CI Pipeline & Deployment
I deployed my app using a continuous integration pipeline:
![alt text](https://github.com/PCMBarber/PiersProject/blob/master/Media/CIPipeline.png)

This Diagram shows the completion of my Jenkins pipeline for performing rolling updates.
![alt text](https://github.com/PCMBarber/PiersProject/blob/master/Media/jenkins.png)

<a name="Conclusion"></a>
## Conclusion
Many things changed from my initial plan to deployment, My database structure was cut down, serveral features were cut due to time contraints. In the future there are countless features I would like to implement and my successful deployment of a rolling update as well as being able to tear down my VM and remake it will serve me well in the future.
