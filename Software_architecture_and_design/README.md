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

**Structural diagrams**<br>
Class model diagram<br>
Is a static view of a system, containing of classes, methods/operations as well as attributes describing their relationships. The following image shows a basic example class diagram:

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P2L1/ClassDiagram_example_general_components.JPG" alt="Class diagram example"/></p>

The center of the image shows the class `Counter`, which has an attribute called `counter` of the type integer, the red minus is indicating that this attribute is private. The `Counter` class also has several methods/operations which are public, the operation `set` takes a input parameter called `aCounter` of type integer. The class `Pile` has a relationship of type *dependency* of the class `Counter`, meaning `Pile` uses the class `Counter`. On the other side `Counter` has a *association* to `leave`, this means `Leave` is affection `Counter`. `Leave` is also a *generalization* of the `Tree` class, it's a kind of class of `Tree`. More details can be found on [Wikipedia](https://en.wikipedia.org/wiki/Class_diagram), since the above diagram does not contain all elements such as *aggregations* and *compositions*.

Object diagram<br>
The object diagram is similar to the class diagram, the only major difference is the fact that the object diagram is referring to instances of particular class objects.

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P2L1/ObjectDiagram_example.JPG" alt="Object diagram example" width="70%" height="70%" /></p>

The example shows the instance `p1` of class type `Pile` and it has an instance `c1` of class type `Counter`.

Composite structure diagram<br>
It shows the internal structure of a class and the collaborations that this structure makes possible. This diagram can include internal parts, ports through which the parts interact with each other or through which instances of the class interact with the parts and with the outside world, and connectors between parts or ports [Wikipedia](https://en.wikipedia.org/wiki/Composite_structure_diagram).

<p align="center">
<img src="https://www.uml-diagrams.org/examples/composite-structure-example-bank-atm.png" alt="Composite structure diagram example"/></p>

The example above shows the composite structure of a `Bank ATM`, it is typically made up of several devices such as central processor unit (CPU), cryptoprocessor, memory, customer display, function key buttons (usually located near the display), magnetic and/or smart chip card reader, encrypting PIN Pad, customer receipt printer, vault, modem.
 A detailed example can be found [here](https://www.uml-diagrams.org/bank-atm-uml-composite-diagram-example.html?context=cst-examples).

Component diagram<br>
Static implementation view, which describes the organization and wiring of the physical components in a system. A component is a logical unit block of the system, which is not the same as a class.

<p align="center">
<img src="https://cdn.visual-paradigm.com/guide/uml/what-is-component-diagram/06-component-diagram-with-subsystem.png" alt="Component diagram example"/></p>

The example above shows the `OnlineStore` subsystem component, it has tree ports represented by the squared elements on the right hand side. The ports expose the provided interfaces  `Customer` and `StoreAdmin`, as well as the required interface `Payment`. The `OnlineStore` component contains multiple subcomponents which interact with each other, for example the `StoreFront` access the `Catalogue` component through the `SQLColumn` interface. The full example can be found [here](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-component-diagram/).

Deployment diagram<br>
The deployment diagram describes the physical allocation of software components on hardware components.

<p align="center">
<img src="https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/what-is-a-deployment-diagram-in-UML/deployment_diagram_real_estate-700x573.png" alt="Deployment diagram example"/></p>

The example shows three different nodes represented by rectangles, the `Bank Server`, `Real Estate Server` and `Individual Machine`. The `Bank Server` has a component named `Mortgage Application` which has a dependency represented by a dashed line to the `Customer DB` artefact. The node `Individual Machine` has an association with the `Bank Server` node, which indicates a communication channel vi TCP/IP with the `Bank Server`. The `Individual Machine` node has also a dependency to the interface of the `Mortage Application` of the `Bank Server` node, shown in green. The full example can be found [here](https://www.lucidchart.com/pages/uml-deployment-diagram#top-info).

Package diagram<br>
A package is an organized group of elements. A package may contain structural things like classes, components, and other packages in it.

<p align="center">
<img src="https://d3n817fwly711g.cloudfront.net/uploads/2012/02/Package-Diagram.jpg" alt="Package diagram example"/></p>

The example shows that the `Accounting` package uses the `HR` and the `Invoice` package, each of those tow packages is providing different methods/operands e.g. the `Invoice` package provides the public method/operand `Customer invoice`. The full example can be found [here](https://creately.com/blog/diagrams/uml-diagram-types-examples/).

Profile diagram<br>
Profile diagram is structure diagram which describes lightweight extension mechanism to the UML by defining custom stereotypes, tagged values, and constraints, it provides a generic extension mechanism for customizing UML models for particular domains and platforms [Wikipedia](https://en.wikipedia.org/wiki/Profile_(UML).  A detailed example can be found [here](https://www.uml-diagrams.org/profile-diagrams.html).

**Behavioral diagrams**<br>

## Conclusions
Answers to the following questions:
  - What was good?
  - What was bad?
  - What would I change next time?

## Future
Additional things I would like to improve?
