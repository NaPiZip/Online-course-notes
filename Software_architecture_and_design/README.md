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
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P2L1/ObjectDiagram_example.JPG" alt="Object diagram example"/></p>

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
Profile diagram is structure diagram which describes lightweight extension mechanism to the UML by defining custom stereotypes, tagged values, and constraints, it provides a generic extension mechanism for customizing UML models for particular domains and platforms [Wikipedia](https://en.wikipedia.org/wiki/Profile_(UML). A detailed example can be found [here](https://www.uml-diagrams.org/profile-diagrams.html).

**Behavioral diagrams**<br>
Use case diagram<br>
Describes a sequence of user visible actions with it's corresponding system responses.

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P2L1/UseCaseDiagram_example.JPG" alt="Package diagram example"/></p>

The example shows a simple use case diagram for a text editor application. It contains two use cases `EditText` and `DisplayText`. The `DisplayText` use case may be extended by the behavior of `LoadFile`. `EditText` has an additional include of the usecase of `DisplayText`. A detailed example can be found [here](https://www.visual-paradigm.com/VPGallery/diagrams/UseCase.html#extend).

Context diagram<br>
Showing the system and interaction between system actors.

<p align="center">
<img src="https://static.jamasoftware.com/www/imports/2014/02/defining-project-and-use-case-diagrams-2.png" alt="Context diagram example"/></p>

The example shows the `Cafeteria Ordering System` in the middle as well as its interactions with the system actors, for example the `Cafeteria Ordering System` interacts with the `Menu Manager` by providing `menu feedback`.
A detailed example can be found [here](https://www.jamasoftware.com/blog/defining-project-scope-context-use-case-diagrams/).

Sequence diagram<br>
The sequence diagram is used primarily to show the interactions between objects in the sequential order that those interactions occur. The main purpose of a sequence diagram is to define event sequences that result in some desired outcome. The focus is less on messages themselves and more on the order in which messages occur; nevertheless, most sequence diagrams will communicate what messages are sent between a system's objects as well as the order in which they occur.

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/CheckEmail.svg/800px-CheckEmail.svg.png" alt="Sequence diagram example" width="70%" height="70%"/></p>

Communication diagram<br>
Similar to Sequence Diagram, the Communication Diagram is also used to model the dynamic behavior of the use case. When compare to Sequence Diagram, the Communication Diagram is more focused on showing the collaboration of objects rather than the time sequence.

<p align="center">
<img src="https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/uml/communication-diagram/communication-diagram-example-700x385@2x.jpg" alt="Communication diagram example"/></p>

The example shows the process to add an event to a calendar. The exact commands and requests being shared between various steps in the process are shown. The numbers on each line represent the order and options in which they are activated. We know that some actions happen concurrently because of the use of letters. A detailed example can be found [here](https://www.lucidchart.com/pages/uml-communication-diagram).

Activity diagram<br>
In its basic form, an activity diagram is a simple and intuitive illustration of what happens in a workflow, what activities can be done in parallel, and whether there are alternative paths through the workflow.

<p align="center">
<img src="https://www.ibm.com/developerworks/rational/library/content/RationalEdge/jan02/t_activityDiagrams_fig1.gif" alt="Activity diagram example"/></p>

Interaction overview diagram<br>
The interaction overview diagram is similar to the activity diagram, in that both visualize a sequence of activities. The difference is that, for an interaction overview, each individual activity is pictured as a frame which can contain a nested interaction diagram. This makes the interaction overview diagram useful to "deconstruct a complex scenario that would otherwise require multiple if-then-else paths to be illustrated as a single sequence diagram.

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Uml-Iod-Diagram1.svg/340px-Uml-Iod-Diagram1.svg.png" alt="Interaction overview diagram example"/></p>

The example shows combined fragment `sd AccessCcontrol` which displays the interaction for entering a code by the user and the resulting sequence flow. A detailed example can be found [here](https://en.wikipedia.org/wiki/Interaction_overview_diagram).

Timing diagram<br>
Timing diagrams are used to explore the behaviors of objects throughout a given period of time. A timing diagram is a special form of a sequence diagram.

<p align="center">
<img src="https://www.uml-diagrams.org/timing-diagrams/timing-diagrams-overview.png" alt="Timing diagram example"/></p>

A detailed example can be found [here](https://www.uml-diagrams.org/timing-diagrams.html).

State diagram<br>
UML state machine diagrams depict the various states that an object may be in and the transitions between those states. A state represents a stage in the behavior pattern of an object, and like UML activity diagrams it is possible to have initial states and final states. An initial state, also called a creation state, is the one that an object is in when it is first created, whereas a final state is one in which no transitions lead out of. A transition is a progression from one state to another and will be triggered by an event that is either internal or external to the object.

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/en/4/45/UML_state_machine_Fig1.png" alt="Timing diagram example"/></p>

A detailed example can be found [here](https://en.wikipedia.org/wiki/UML_state_machine#Basic_UML_state_diagrams).


## Conclusions
Answers to the following questions:
  - What was good?
  - What was bad?
  - What would I change next time?

## Future
Additional things I would like to improve?
