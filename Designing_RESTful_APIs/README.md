<img src="https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.l8H7yN_ZVoz_SCzv3qD4ngHaFd%26pid%3D15.1&f=1" alt="Udacity Logo" height="42px" width="42px" align="left">

# Designing RESTful APIs
<div>
    <a href="https://github.com/NaPiZip/Docker_GUI_Apps_on_Windows">
        <img src="https://img.shields.io/badge/Document%20Version-1.0.0-brightgreen.svg"/>
    </a>
    <a href="https://www.microsoft.com">
        <img src="https://img.shields.io/badge/Windows%2010%20x64-10.0.17134%20Build%2017134-blue.svg"/>
    </a>
</div>

## Objectives
These are my notes of the Udacity course `Designing RESTful APIs`. I am only covering details which I think are important for me. This document is not supposed to be a summary of all the content covered by the course, it's just a centralized place to store information in order to support my learning process. A lot of information is online nowadays and I think it's not needed to memorize all details, it's more important to have a solid overview and to know where to look for the details.

##  What's and Why's of APIs

**What are APIs**<br>
APIs are application programming interfaces, APIs can be described as building blocks of software components or applications. A comprehensive metaphor is a wall socket, the socket represents a interface to a service better know as electricity. The user is comfortable able to use the service if he is in compliance with the policy of the service provider, meaning if the consumer decides to agree on a contract with a energy provider, then the provider invokes the rights for the user to access the service, though out a defined interface the wall socket. The wall socket has specific properties, such as a physical shape for a plug as well as a defined voltage and a maximum current. Those properties are defined by the service provider, e.g. the API provider. A more formal definition is the following one:<br>

*In computer programming, an application programming interface (API) is a set of subroutine definitions, communication protocols, and tools for building software. In general terms, it is a set of clearly defined methods of communication among various components. A good API makes it easier to develop a computer program by providing all the building blocks, which are then put together by the programmer. An API may be for a web-based system, operating system, database system, computer hardware, or software library [Wikipedia](https://en.wikipedia.org/wiki/Application_programming_interface).*   

**Web APIs**<br>
A web API is a specific type of API which is used for either a web server or web browser, they are typically HTTP based.  The API itself defines a set of endpoints, request messages and response structures. It is a standard approach also to identify the supported response media types. XML and JSON are two favorite examples of response media types that can be easily interpreted by API consumers.

**The OSI layers**<br>
The Open System Interconnection (OSI) is a reference model for how various applications communicate over any network. The purpose behind this model was to provide developers, programmers, engineers, vendors and all the associated people a standard that can serve as a guide for them using which they would be able to create communication equipment and software inter operable.


<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P2L1/ObjectDiagram_example.JPG" alt="Object diagram example"/></p>
