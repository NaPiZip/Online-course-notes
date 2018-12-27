<img src="https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.l8H7yN_ZVoz_SCzv3qD4ngHaFd%26pid%3D15.1&f=1" alt="Udacity Logo" height="42px" width="42px" align="left">

# Software Architecture and Design
<div>
    <a href="https://github.com/NaPiZip/Docker_GUI_Apps_on_Windows">
        <img src="https://img.shields.io/badge/Document%20Version-1.0.0-brightgreen.svg"/>
    </a>
    <a href="https://www.microsoft.com">
        <img src="https://img.shields.io/badge/Windows%2010%20x64-10.0.17134%20Build%2017134-blue.svg"/>
    </a>
    <a href="https://www.genmymodel.com/">
        <img src="https://img.shields.io/badge/GenMyModel-UML2.5-blue.svg"/>
    </a>
</div>

## Objectives
These are my notes of the Udacity course `Software Architecture and Design`. I am only covering details which I think are important for me. This document is not supposed to be a summary of all the content covered by the course, it's just a centralized place to store information in order to support my learning process. A lot of information is online nowadays and I think it's not needed to memorize all details, it's more important to have a solid overview and to know where to look for the details.

## Lessons
This section displays the notes I took during different lessons as well as my solutions of the assignments, I am not covering the answers to particular lessons since I am not providing a solution for the course.

###  P2L1 Review of UML
**Diagram types**<br>
UML consists of two main category of diagrams:
1.  Structural diagrams
It shows the individual parts and elements of a system and the relationships. This kind of diagram is a static type.

2. Behavioral diagrams
It visualizes, specifies, constructs, and documents the dynamic aspects of a system. It may represent only a certain state or event.

**Structual diagrams**<br>
Class model diagram<br>
Is a static view of a system, containing of classes, methods/operations as well as attributes describing their relationships. The following image shows a basic example class diagram:<br>

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P2L1/ClassDiagram_example_general_components.JPG" alt="Class diagram example"></p>
The center of the image shows the class `Counter`, which has an attribute called `counter` of the type integer, the red minus is indicating that this attribute is private. The `Counter` class also has several methods/operations which are public, the operation `set` takes a input parameter called `aCounter` of type integer. The class `Pile` has a relationship of type *dependency* of the class `Counter`, meaning `Pile` uses the class `Counter`. On the other side `Counter` has a *association* to `leave`, this means `Leave` is affection `Counter`. `Leave` is also a *generalization* of the `Tree` class, it's a kind of class of `Tree`.

More details can be found on [Wikipedia](https://en.wikipedia.org/wiki/Class_diagram), since the above diagram does not contain all elements such as *aggregations* and *compositions*.


## Conclusions
Answers to the following questions:
  - What was good?
  - What was bad?
  - What would I change next time?

## Future
Additional things I would like to improve?
