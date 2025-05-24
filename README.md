# EigenBox - by Team Smiley (Hackaburg 2025 Project)
More info on [Devpost](https://devpost.com/software/eigenbox-by-team-smiley).

## Inspiration
We are living in the era of AI, where nothing is more valuable than data. That's one more reason to keep your data safe at home. But almost everyone relies on the services of large companies for things like email, cloud storage, calendar, and more. 
Many companies that offer such services have dubious privacy policies and subsequently misuse your data for profit. Your data is at risk of being in a data breach. It is important for companies to comply with certain standards and regulations, which can only be guaranteed when keeping the hosting in-house.
The current solution for that would be self-hosting every service, which is basically impossible for non-technical people, as there are two main problems coming up: 
1. There is big room for failure to configure everything correctly which leaves a high risk of being exposed to potential cyber threats. Even if configured correctly, the software must be actively maintained and kept up to date.
2. The knowledge required to get the system up and running is much greater than what most people possess. Even if an individual manages to get all desired components working, making them interact with one another can take a long time and exceeds the skill level of most people. 

## Our business case
Cloud storage, email, calendar and many other services are used by billions of people everyday. These services often have dubious privacy policies and may suffer from data breaches thus sharing user data against the will of the user.
Many people are interested in protecting their data but may not find the idea of setting up and managing their own infrastructure so appealing or they simply lack the ability to do so. What if it were much easier? What if someone could buy a preconfigured server for their home or company and simply plug it in while not having to worry about network access, service installation and all the like.
We have developed this solution: the EigenBox.

## What it does
Our Solution, a device called the EigenBox, is essentially a small homeserver that can run these services without the need for complex configurations. When the device is hooked up with power and Ethernet, it automatically connects to our own tunneling proxy server and thus allows external users to reach specific services without the need for port forwarding or further configuration. This means a user with no technical expertise at all is able to set it up. The EigenBox offers a simple yet intuitive web interface that allows users to take full control over which services should and should not be hosted on the machine.  

## How we built it
For our proof-of-concept we used a raspberry pi. (In production different options of small to medium sized computers may be used instead thus allowing for better adaption to customer needs.)
The EigenBox currently features a web service (frontend: React, backend: FastAPI Python) providing a dashboard to manage services (currently this is achieved using Docker containers). In order to offer remote access to services on the box (e.g. VPN) the EigenBox automatically connects to our own reverse proxy server (currently hosted using cloud VMs) - therefore no port forwarding is required. 

## Challenges we ran into
- port forwarding
- running out of space  on the raspberry pi

## Accomplishments that we're proud of
Setting up a scalable infrastructure that essentially has everything that is needed to build the first EigenBoxes.

## What we learned
Much about networking, tunneling, and DDNS, as well as Docker.

## What's next for Eigenbox
Before Eigenbox could launch:
- implementing more services
- allowing more fine-grained control over how each service is exposed to the internet
-  better integration between the services

Furthermore through certifications corporate customers may be able to skip the process of hiring professionals to set up their services or certify them as the box is already compliant.  
