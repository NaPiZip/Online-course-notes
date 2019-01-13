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
1.  Structural diagrams<br>
It shows the individual parts and elements of a system and the relationships. This kind of diagram is a static type.

2. Behavioral diagrams<br>
It visualizes, specifies, constructs, and documents the dynamic aspects of a system. It may represent only a certain state or event.

**Structural diagrams**<br>
Class model diagram<br>
Is a static view of a system, containing of classes, methods/operations as well as attributes describing their relationships. The following image shows a basic example class diagram:

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P2L1/ClassDiagram_example_general_components.JPG" alt="Class diagram example"/></p>

The center of the image shows the class `Counter`, which has an attribute called `counter` of the type integer, the red minus is indicating that this attribute is private. The `Counter` class also has several methods/operations which are public, the operation `set` takes a input parameter called `aCounter` of type integer. The class `Pile` has a relationship of type *dependency* of the class `Counter`, meaning `Pile` uses the class `Counter`. On the other side `Counter` has a *association* to `leave`, this means `Leave` has an association with `Counter`. `Leave` is also a *generalization* of the `Tree` class, it's a kind of `Tree`. More details can be found on [Wikipedia](https://en.wikipedia.org/wiki/Class_diagram), since the above diagram does not contain all elements such as *aggregations* and *compositions*.

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

The example above shows the `OnlineStore` subsystem component, it has tree ports represented by the squared elements on the left hand side. The ports expose the provided interfaces  `Customer` and `StoreAdmin`, as well as the required interface `Payment`. The `OnlineStore` component contains multiple subcomponents which interact with each other, for example the `StoreFront` access the `Catalogue` component through the `SQLColumn` interface. The full example can be found [here](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-component-diagram/).

Deployment diagram<br>
The deployment diagram describes the physical allocation of software components within a or multiple hardware components.

<p align="center">
<img src="https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/what-is-a-deployment-diagram-in-UML/deployment_diagram_real_estate-700x573.png" alt="Deployment diagram example"/></p>

The example shows three different nodes represented by rectangles, the `Bank Server`, the `Real Estate Server` and the `Individual Machine`. The `Bank Server` has a component named `Mortgage Application` which has a dependency represented by a dashed line to the `Customer DB` artefact. The node `Individual Machine` has an association with the `Bank Server` node, which indicates a communication channel via TCP/IP with the `Bank Server`. The `Individual Machine` node has also a dependency to the interface of the `Mortage Application` of the `Bank Server` node, shown in green. The full example can be found [here](https://www.lucidchart.com/pages/uml-deployment-diagram#top-info).

Package diagram<br>
A package is an organized group of elements. A package may contain structural things like classes, components, and other packages in it.

<p align="center">
<img src="https://d3n817fwly711g.cloudfront.net/uploads/2012/02/Package-Diagram.jpg" alt="Package diagram example"/></p>

The example shows that the `Accounting` package uses the `HR` and the `Invoice` package, each of those two packages is providing different methods/operands e.g. the `Invoice` package provides the public method/operand `Customer invoice`. The full example can be found [here](https://creately.com/blog/diagrams/uml-diagram-types-examples/).

Profile diagram<br>
Profile diagram is structure diagram which describes lightweight extension mechanism to the UML by defining custom stereotypes, tagged values, and constraints, it provides a generic extension mechanism for customizing UML models for particular domains and platforms. A detailed example can be found [here](https://www.uml-diagrams.org/profile-diagrams.html).

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
The sequence diagram is used primarily to show the interactions between objects in sequential order and those interactions that occur. The main purpose of a sequence diagram is to define event sequences that result in some desired outcome. The focus is less on messages themselves and more on the order in which messages occur; nevertheless, most sequence diagrams will communicate what messages are sent between a system's objects as well as the order in which they occur.

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/CheckEmail.svg/800px-CheckEmail.svg.png" alt="Sequence diagram example" width="70%" height="70%"/></p>

Communication diagram<br>
Similar to sequence diagrams, the communication diagram is also used to model the dynamic behavior of the use case. When compare to sequence diagram, the communication diagram is more focused on showing the collaboration of objects rather than the time sequence.

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

###  P2L3 UML Class Models
This chapter is a more detailed explanation of classes within a class model, I am not going to reproduce the same content as in the previous chapter. The following image shows my solution for the #21 Quiz.

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P2L3/P2L3_21_quiz.jpg" alt="P2L3_21_Quiz solution"/></p>

The top element is the `Diagram` class which has two children `Structured Diagram` and the `Behavioral Diagram`. The `Structured Diagram` has a main child the `Profile Diagram`, I picked it as the first child because `Profile Diagram`'s are a mechanism to extend standard UML stereotypes etc.. The next child is the `Class Model Diagram`, whit it's children `Composite Structure Diagram` and `Component Diagram`, which are diagram types who give more detailed information about a class or a component. The `Object Diagram` is a representation of instantiated classes, which was the reason for making it a child of the `Class Diagram`. The last entities are the `Package Diagram` and the `Deployment Diagram`, both of them represent an aggregation of components or classes.

The `Behavioral Diagram` has one direct child which is the `Use Case Diagram`, it is one of the most important diagram types, because it describes the behavior of a component or a system. The `Interaction Overview Diagram` and the `Timing Diagram` both have the `State Diagram` and the `Sequence Diagram` as parents. The `Interaction Overview Diagram` is a hybrid of it's parents, where as the `Timing Diagram` represents more the behavior in certain states in a sequence.

### P2L5 Library Exercise
Shows an example on how to design a system based on requirements, by using the approach described in the earlier sections. The following steps are used:

  - Analyzing the requirements<br>
  Based on the given text all relevant nouns where identified and captured. It is important to capture as many elements as possible since the outcome is used for refinement in later stages.

  - Refining and adding attributes<br>
  Here the allocation of additional attribute takes place, by grouping content which could be logically grouped to a different element and eliminating it afterwards. A noticeable fact also is that the concept of each class need to be understood to make sure that the later on created interactions make sense.

  - Operations<br>
  The specification is checked for action verbs and operations are created based on the findings, and allocated to the respective elements.

  - Adding and refining relationships<br>
  Finding associations between classes consists of linking the operations between those entities, seeing how those elements are associated with each other, for example the `Patron` has a operation  called `checkOut` which is an association between the `Item` class, meaning the `Patron` can perform the operation of checking out an `Item`. It also makes sense to add generalization dependencies to similar classes.

  - Refining the diagram<br>
  In this step the whole diagram is checked for consistency and relationships between associations in addition association classes can be created for interaction based on associations.

###  P2L6 Formal Specification Exercise
First order logic FOL / predicate calculus notation is used in order to specify general propositions. The object constraint language is part of UML which can be used to annotate FOL.
The process contains of three stages:<br>
  1. Signature<br>
  Describes the input, output parameters and the function name.
  2. Precondition<br>
  Are assumption which are made in order to generate a behavior.
  3. Postcondition<br>
  Describes how the output relates to the input, as well as side effects of the function.

**Permutation example**<br>
Given a function called `PERMUTATION` which has the following signature in C++:
```
bool PERMUTATION(std::vector<int> X, std::vector<int> Y);
```
Assuming the precondition is as followed:
```
  |X| = |Y|
```
`X` has the same length as `Y`.

The permutation postconditions for the following cases are:
  1. None empty case
  ```
  |x| = 0 =>
  PERMUTATION(X, Y)
  ```
  If the length of the vector `X` is empty, then we have a valid permutation (based on the precondition of `X` having the same length then `Y`).

  2. No matching case<br>
  The problem is divided into three segments:
  ```
                        |<- first ->|j|<-second->|     
  std::vector<int> X = {1,  2,  3,   4,  5,  6};
  std::vector<int> Y = {1,  2,  3,   4,  8,  9};
  ```
  The FOL notation is:
  ```
  Ǝ j: 1 < j < |Y| ^ (X[1] = Y[j])
  ```
  There exist some position called `j` which is greater than 1 up to the length of `Y` and the value of `Y` at position `j` must be equal to the first element of `X`. The rest of `Y` comes from concatenating  with the first and second segment:
  ```
  Y[1..j-1] ⌢ Y[j+1..|Y|]
  ```
  Followed by checking if the rest of `X` aka. `tail(X)` is a permutation:
  ```
  PERMUTATION(tail(X), (Y[1..j-1] ⌢ Y[j+1..|Y|]))
  ```
  3. Third case
  ```
  (X[1] != Y[1]) ^
  ((Ǝ j: 1 < j < |Y|) ^ X[1] = Y[j]) ^
  PERMUTATION(tail(X), (Y[1..j-1] ⌢ Y[j+1..|Y|]))
  ```
  `X` at position one must not equal the value of `Y` at position one and there exist some position called `j` which is greater than 1 up to the length of `Y` where `X` at position one is equal to some `Y` at position `j` and there is a permutation of the `tail(x)` concatenating the first and second segment of `Y`.

The full postcondition is as followed:
```
PERMUTATION(X, Y) <=>
|X| = 0 v
(|X| > 0) =>
(X[1] = Y[1] ^ PERMUTATION(tail(X), tail(y))) v
(X[1] != Y[1] ^ (Ǝ j: 1 < j < |Y| ^ (X[1] = Y[j])) ^
PERMUTATION(tail(X), (Y[1..j-1] ⌢ Y[j+1..|Y|]))
```
`X` is permutation of `Y` if and only if one of the three conditions is true. First case is for having a empty vector, or if the length of `X` is greaten than 0 and `X` at position 1 is equal to `Y` at position 1 and the tails of `X` and `Y` are both permutations or when `X` at position 1 is not equal to `Y` at position 1 and there exists a `j` which is greater than 1 but smaller then the length of `Y` and the value of `Y` at position `j` must be equal to the first element of `X` and the permutation of the tail of `X` and the concatenation of the rest of the elements of `Y` is a premutation.

### P2L7 OCL
OCL is declarative not procedural notation, it's main purpose is to overcome the limitations of UML in terms of precisely specifying detailed information's of a design. Declarative means OCL does not include constructs like assignments, it also does not contain any implementation details. The syntax of OCL looks as followed:

```
context <identifier> <constraintType>:
<Boolean expression>
```
  - `context <identifier>`<br>
  Where are we in the diagram, it's usually the class name.
  - `<constraintType>`<br>
  Either invariant `inv`, precondition `pre` or postcondition `post`.
  - `<Boolean expression>`<br>
  The actual constraint the statement is expressing.

**Invariants**<br>
Integrity constraints in OCL are represented as invariants defined in the context of a specific type, named the context type of the constraint. The statement must be always true, and usually expresses key system requirements. Integrity constrains are also handled by invariants.
```
context LargeCompany
inv: numberofEmployees > 50
```
The example shows in order to be a `LargeCompany` the `numberofEmployees` must always be greater than 50.

**Pre- and postconditions**<br>
Expressing the conditions which need to be fulfilled before the operation `precondition` and the behavior afterwards `postcondition` usually what the relationship between inputs and outputs.
```
context Real::squareRoot(): Real
pre: self >=0
post self = result * result
```
The example is showing that the precondition for the `squareRoot` function is having a value which is 0 or greater, the result then should equal the value feed in multiplied by itself.

**Expressions**<br>
An OCL expression may be used to indicate the result of a query operation. The expression must conform to the result type of the operation. Like in the pre- and postconditions, the parameters maybe used in the expression. Pre-, and postconditions, and body expressions may be mixed together after one operation context.
```
context Person::getCurrentSpouse() : Person
pre: self.isMarried = true
body: self.mariages->select( m | m.ended = false ).spouse
```

More details and additional examples can be found in the  full specification pdf here [OCL V2.4](https://www.omg.org/spec/OCL/2.4/PDF).

### P2L9 Behavior Modeling
Difference between a state and an event is described here:

State<br>
Is a description of a system at a given time. The set of states a system can occupy is known as its state space.

Event<br>
An event is a occurrence which is singly and instantaneous, the occurrence could be synchronous or asynchronous. An event can trigger actions e.g. a state transition.

Modelling technics:
  - Combinatorial<br>
  Do not have events but states. The input only determine the subsequence states, not the previous state.
    - Decision tables<br>
    Are used for example in digital logic and showing the states of the outputs depending on the inputs.
    - Decision tree<br>
    Is the graphical representation of a decision table.    
  - Sequential<br>
  Do have states which are in a linearly order of traverse. They have memory about previous activities / states. A variant is the finite state machine which only has a fixed number of states (finite number).
    - State transition table<br>
    Contains additional information about the previous state as well as the next state depending on the stimuli.
    - State transition diagram<br>
    A more concise representation of the state transition table. The downside of this type of diagram is that there is no concept of nesting and the diagram could end up messy very quick.
    - State chart<br>
    Provide several mechanism in order to deal with higher complexity.   
  - Concurrent<br>
  Do have states with unconstrained events, in nondeterministic manner.

The following state diagram shows the high level states of the [David Harels's Watch state machine](https://s3.amazonaws.com/content.udacity-data.com/courses/gt-cs6310/readings/gt-sad-harel-paper.pdf). The watch has four external control buttons, as well as a main display that can be used to show the time (hour, minutes, and seconds) or the date (weekday, day of month, and month). The buttons are `a`, `b`, `c` and `d`, `b - up` means releasing button `b` after pressing.

<p align="center">
<img src="https://s3.amazonaws.com/content.udacity-data.com/courses/gt-cs6310/notes/gt-sad-p2l9-watch-diagram.png" alt="David Harel's Watch - High Level State Diagram"/></p>

The state of the watch is either `dead` or `alive`, the events `bt - in`, `bt rm`, `bt - dy` and `bt wk` signify, respectively, the insertion, removal, expiration, and weakening of the battery. We use `t-hits - tm` to signify that the internal time of the watch has reached
the internal time setting of the alarm, and `t-hits hr` to signify that it has reached a whole hour. Also, `beep- rt` occurs when either any button is pressed or 2 minutes have elapsed since entering beep, and `beep-st` occurs 2 seconds after entering `c -beep`. The first of the five components in the image, `main`, specifies the transitions between displaying and beeping... .

This chapter is pretty self explanatory  or most information can be looked up online, which was the reason for me to just take minimal notes.

### P2L10 Clock Radio Exercise
The radio is powered by electricity out of a wall socked. The radio has two manual knobs, `volume` and `tuning`, the frequency is displayed by the white bar, the display has a `12-hour clock` and two small lights, the upper left light is on for `am` and off for `pm`, the light in the lower right corner indicates if the alarm is on. The radio has additionally 2 switches, one for AM/FM frequency band, the second switch has 4 position for alarm `on`, `off`, `radio wake` and `beeping wake`. Four button are on the left side and there are used for various timer `hour`, `min`, `Wake` and `sleep`. The `wake` button enables setting the wake time by then pressing `hour` and `min`, the same goes for the `sleep` button. The `snooze` button is used for shutting off an active alarm for a defined period of time. The image below shows a sketch of the clock and its

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P2L10/Clock_sketch_with_all_precepts.jpg" alt="Sketch of the clock" width="50%" height="50%" /></p>

| Number         | Name     | States
| :------------- | :------------- |:-------------         |
| 1)             | AM/FM indicator light| ON - OFF        |
| 2)             | Time display         | HH:MM           |
| 3)             | Frequency bar        | Position: 0-100 |
| 4)             | Wake button          | Pushed: TRUE, FALSE|
| 5)             | Sleep button         | Pushed: TRUE, FALSE|
| 6)             | Hour button          | Pushed: TRUE, FALSE|
| 7)             | Minute button        | Pushed: TRUE, FALSE|
| 8)             | Mode switch         | ON - OFF - RADIO - BEEP|
| 9)             | Snooze button        | Pushed: TRUE, FALSE|
| 10)            | Volume knob          | Position: 0-100 |
| 11)            | Tune knob            | Position: 0-100 |
| 12)            | AM/FM switch         | AM - FM         |
| 13)            | Alarm indicator light| ON - OFF|
| 14)            | Power cable          | CONNECTED, DISCONNECTED|
| 15)            | Speaker              | ON - OFF|               

The following image shows some use cases of the radio.

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P2L10/UseCaseDiagram_example_of%20_some_clock_features.JPG" alt="Sketch of the clock"/></p>

<p align="center">
<img src="https://s3.amazonaws.com/content.udacity-data.com/courses/gt-cs6310/notes/gt-sad-p2l10-clock-state-final.png" alt="State Chart"/></p>

### P3L1 KWIC Exercise
KWIC is an acronym for Key Word In Context, the most common format for concordance lines. The term KWIC was first coined by Hans Peter Luhn. The system was based on a concept called keyword in titles which was first proposed for Manchester libraries in 1864 by Andrea Crestadoro.

A KWIC index is formed by sorting and aligning the words within an article title to allow each word (except the stop words) in titles to be searchable alphabetically in the index. It was a useful indexing method for technical manuals before computerized full text search became common.

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P3L1/BoxAndArrowDiagram_KWIC.JPG" alt="Box and arrow diagram KWIC"/></p>

The above image is showing my solutions for the KWIC exercise. The top diagram shows the sentence which the index should be based on, the next step is omitting the stop words (this is a alternative version), the words in the new sentence are then counted and the sentence is then shifted in circular fashion n times. The second diagram works in a similar way the number of words are counted, the first word and the tail are extracted out of the sentence, the front is then switched whit the tail and then saved back, the process is reaped for n times. The full solution to multiple architectures is described [here](https://s3.amazonaws.com/content.udacity-data.com/courses/gt-cs6310/readings/gt-sad-garlan-and-shaw-paper.pdf).

### P3L2 Overview of Architectural Styles
Informal definition of software architecture is the organization of a subsystem into component subsystems or modules. It is usually done in layers and is usually done in styles.

  - Abstract data types<br>
  The definition of ADT only mentions what operations are to be performed but not how these operations will be implemented. It does not specify how data will be organized in memory and what algorithms will be used for implementing the operations. It is called “abstract” because it gives an implementation independent view. The process of providing only the essentials and hiding the details is known as abstraction. A stack for example is a ADT with push and pop operations.

  - Blackboard architecture<br>
  Blackboard allows multiple processes (or agents) to communicate by reading and writing requests and information to a global data store. Each participant agent has expertise in its own field, and has a kind of problem solving knowledge (knowledge source) that is applicable to a part of the problem, i.e., the problem cannot be solved by an individual agent only. Agents communicate strictly through a common blackboard whose contents is visible to all agents (see [Wikipedia](https://en.wikipedia.org/wiki/Blackboard_(design_pattern)).
  - Coroutines<br>
  Coroutines are computer-program components that generalize subroutines for non-preemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. Coroutines are well-suited for implementing familiar program components such as cooperative tasks, exceptions, event loops, iterators, infinite lists and pipes.

  - Data centric architecture<br>
  Data centric refers to an architecture where data is the primary and permanent asset, and applications come and go.  In the data centric architecture, the data model precedes the implementation of any given application and will be around and valid long after it is gone.

  - Domain driven design<br>
  The philosophy of domain-driven design (DDD) – first described by Eric Evans in his book of the same name – is about placing our attention at the heart of the application, focusing on the complexity that is intrinsic to the business domain itself. We also distinguish the core domain (unique to the business) from the supporting sub-domains (typically generic in nature, such as money or time), and place appropriately more of our design efforts on the core. Domain-driven design consists of a set of patterns for building enterprise applications from the domain model out. In your software career you may well have encountered many of these ideas already, especially if you are a seasoned developer in an OO language. But applying them together will allow you to build systems that genuinely meet the needs of the business.


  - Implicit invocation
  - Master control architecture
  - Message bus architecture
  - Object oriented architecture
  - Pipe and filter
  - Process control
  - Production subsystems
  - Representational state transfer (REST)
  - Service oriented architecture (SOA)

Most content of this lesson describes different styles of architectures, I am not going to repeat the content since in my opinion it only makes sense to combine the styles with exercise related to them.

### P3L3 Architectural Views
This section is covering content related to the fact of which important "Views" exists. Views are architectural frameworks which focus on specific key concepts and main focuses, the following image shows [Philippe Kruchten's](https://en.wikipedia.org/wiki/4%2B1_architectural_view_model) model:

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/4%2B1_Architectural_View_Model.svg/354px-4%2B1_Architectural_View_Model.svg.png" alt="Architectural views, 4+1"/></p>


  - Logical view
  The logical view is concerned with the functionality that the system provides to end-users. UML diagrams used to represent the logical view include, class, box and arrow, interaction overview, collaboration and component and connectors diagrams.

  - Developmental view
  The development view illustrates a system from a programmer's perspective and is concerned with software management. This view is also known as the implementation view. It uses the UML component diagram to describe system components. UML diagrams used to represent the development view include the package diagram.

  - Process view
  The process view deals with the dynamic aspects of the system, explains the system processes and how they communicate, and focuses on the runtime behavior of the system. The process view addresses concurrency, distribution, integrators, performance, and scalability, etc. UML diagrams to represent process view include the activity diagram.

  - Physical view
  The physical view depicts the system from a system engineer's point of view. It is concerned with the topology of software components on the physical layer as well as the physical connections between these components. This view is also known as the deployment view. UML diagrams used to represent the physical view include the deployment diagram.

  - Scenarios / use case view
  The description of an architecture is illustrated using a small set of use cases, or scenarios, which become a fifth view. The scenarios describe sequences of interactions between objects and between processes. They are used to identify architectural elements and to illustrate and validate the architecture design. They also serve as a starting point for tests of an architecture prototype. This view is also known as the use case view.

There exist many additional view models besides the 4+1 model view of Kruchen's, the following section shows a selection of different important view models:

  - Context view
  The Context view of a system defines the relationships, dependencies, and interactions between the system and its environment—the people, systems, and external entities with which it interacts. It defines what the system does and does not do; where the boundaries are between it and the outside world; and how the system interacts with other systems, organizations, and people across these boundaries, see [here](https://www.viewpoints-and-perspectives.info/home/viewpoints/context/).

  - Features view
  The feature view mainly focuses on functional sets which are visible for the user or containing a complete functional entity, an example could be the auto zoom feature of a camera or the flash feature.

  - Non functional view
  Are aspects which define how a system is supposed to be rather then what it is supposed to do. It could contain requirements as: The GUI should be easy and intuitive to use, the application should be easy maintainable, extensible, portable ... .

### P3L4 Text Browser Exercise
The following image shows the use case diagram for the text browser exercise:

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P3L4/UseCaseDiagram_text_browser.JPG" alt="Use case diagram text browser."/></p>

The main use case of the text browser is to display text, the use case also includes loading a particular file. The second use case is to scroll the current `ViewPort` content with the help of the `ScrollBar`, if the user scrolls then the content is moved in the `ViewPort` accordingly. The last use case is the event of resizing the window which also changes the content of the `ViewPort`.

**Phase 0: System relationship between environment**
In addition to the described scenarios in the use case diagram above we have the following behavioral expectations. The `ScrollBar` handle size is defined as followed:
```
handleSize = nVisibleLinesInVieport / nLinesInFile
```
This also means if the `ViewPort` resizes then the size of the `ScrollBar` adjusts accordingly.

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P3L4/Example_of_the_text_browser_GUI_and_its_events.JPG" alt="Example of the text browser GUI and it's events."/></p>

**Phase 1: Decomposing the system into its components**<br>
The system so far contains of the `Viewport`, the `ScrollBar` and the `FileManager`. The following component properties are defined.
```
{ context ScrollBar::moveHandle(newPosition : int) : void
  post: handlePosition = newPosition
}

{ context ViewPort::resizeWindow(newSize : int) : void
  pre: newSize => 0
  post: height = newSize  
}

{ context displayDocument
  inv: ViewPort::viewContens = FileManager.document->subsequence(ScrollBar::handlePosition, ScrollBar::handlePosition + ViewPort::height -1)
}
```

**Phase 2: Determine the systems architecture**<br>
Layered implicit invocation:<br>
[Garland and Shaw](http://www.cs.cmu.edu/afs/cs/project/able/ftp/intro_softarch/intro_softarch.pdf) describe implicit invocation systems: "The idea behind implicit invocation is that instead of invoking a procedure directly, a component can announce (or broadcast) one or more events. Other components in the system can register an interest in an event by associating a procedure with the event. When the event is announced the system itself invokes all of the procedures that have been registered for the event. Thus an event 'implicitly' causes the invocation of procedures in other modules."

The following OCL constrains have been added:
```
{ context ViewPort
  inv: ScrollBar.handleSize = height / FileManager::document->size()  
}

{ context ViewPort
  inv: viewContens->size() = min(height, FileManager::document->size())  
}

{ context ScrollBar::updateHandleSize(size : int) : void
  pre: s > 0
  post: handleSize = s
}
```

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P3L4/ClassDiagram_text_browser_components.JPG" alt="Text browser class diagram."/></p>

Invariant maintenance strategies:<br>
  - Aggregated responsibility
  One component owns the other two, for example the event of scrolling the handle, the `ViewPort` has pointer or instances to the other components, the `ViewPort` gets the notification of the scroll event and forward the behaviour to the `ScrollBar`, then the `ViewPort` has to change the content accordingly, by making the request for different content to the `FileManager`.

  - Distributed responsibility
  Each component handles a part of the events e.g. the `ScrollBar` gets the event of scrolling and updates it's position and issues a request to notify the `ViewPort`. The `ViewPort` then will make a request to the `FileManager` in order to get the right content.

  - Mediators
  A new implementation element is introduced for each invariant called the `Mediator`, he knows the dependent components. Each event and it's component must inform it's corresponding `Mediator`, for example the `ScrollBar` receives the resize event and notifies the `Mediator`, which requests the new position and requests new content form the `FileManager` and pass it to the `ViewPort`.

### P3L6 Connectors
Component interaction is embodied in the notion of software connectors. Connectors manifest themselves in a software system as shared variable accesses, table entries, buffers, instructions to a linker, procedure calls, networking protocols, pipes, SQL links between a database and an application, and so forth [Mehta et. al. Paper](https://s3.amazonaws.com/content.udacity-data.com/courses/gt-cs6310/readings/gt-sad-mehta-paper.pdf).

The base elements are called `ducts` those are the base channel. `Ducts` provide a mechanism for transmitting data and control information among components. Connectors go beyond `ducts` and provide the protocol.

Services in this context represents the broad interaction role that the connector fulfils, it describes the purpose of the connection. The following four category are mention in the paper:
  - Communication (t), for transmitting data.
  - Coordination (o), for transferring control.
  - Conversion (x), typically converting data formats so components can interact.
  - Facilitation, mediation / optimization operation.

Types of connectors:
  - Procedure call connectors
  Procedure call connectors model the flow of control among components through various invocation techniques (coordination). They also perform transfer of data among the interacting components through the use of parameters (communication).

  - Event connectors
  An event can be defined as “the instantaneous effect of the (normal or abnormal) termination of the invocation of an operation on an object, and it occurs at that object's location”. Event connectors are similar to procedure call connectors in that they model the flow of control among components (coordination).

  - Data access connectors
  Data access connectors allow components to access data maintained by a data store component (communication). Data access often requires preparation of the data store
  before and clean-up after access has been completed.

  - Linkage connectors
  Linkage connectors are used to tie the system components together and hold them in such a state during their operation. Linkage connectors enable the establishment of ducts, the channels for communication and coordination, which are then used by higher-order connectors to enforce interaction semantics (facilitation).

  - Stream connectors
  Streams are used to perform transfers of large amounts of data between autonomous processes (communication). Streams are also used in client-server systems with data transfer protocols to deliver results of computation.

  - Arbitrator connectors
  When components are aware of the presence of other components but cannot make assumptions about their needs and state, arbitrators streamline system operation and resolve any conflicts (facilitation), and redirect the flow of control (coordination).

  - Adaptor connectors
  Adaptor connectors provide facilities to support interaction between components that have not been designed to interoperate. Adaptors involve matching communication policies and interaction protocols among components (conversion). These connectors are necessary for interoperation of components in heterogeneous environments, such as different programming languages or computing platforms.

  - Distributor connectors
  Distributor connectors perform the identification of interaction paths and subsequent routing of communication and coordination information among components along these paths (facilitation). They never exist by themselves, but provide assistance to other connectors, such as streams or procedure calls.

### P3L8 Refinement
It is necessary to abstract problems by hiding details in order to come up with the bigger picture, it's about managing the complexity by carefully refining a design. Solving a problem often needs to divide it into subproblems and then solving each lower level problem ensuring the lower level problems contribute to the high level objectives.

**Divide and Conquer**<br>
In computer science, divide and conquer is an algorithm design paradigm based on multi-branched recursion. A divide-and-conquer algorithm works by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to give a solution to the original problem [Wikipedia](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm).

Proper Refinement means moving from an architecture to an implementation. Three probertites must be followed:
  1. The top level must represent the requirements.  
  2. Each level must be internal consistent.
  3. Each lower level must represent its upper level.

Refinement Example:<br>
- The user can make a deposit of any positive number.
- The user may make a withdrawal of any positive number of dollars so long as at least that number of dollars is currently held in the account.
- The user may request the current value of the bank balance, which is defined as the net value of all deposits made minus the sum of all withdrawals.
- Initially, the bank account is empty.


| Account     |
| :------------- |
| transactions: Sequence (Integer)   |
| deposit (amount : Integer)<br> withdrawal (amount : Integer)<br> balance( ) : Integer|

```
{ context Account::deposit(amount : Integer)
  pre: amount > 0
  post: transactions = transactions@pre.append(a)
}

{ context Account::withdrawal(amount : Integer)
  pre: amount > 0 and transitions->sum() >= amount
  post: transactions = transactions@pre.append(-a)
}

{ context Account::balance() : Integer
  post: result = transactions->sum()
}

{ context Account::transactions
  init: transactions = {}
}
```

**Notation**<br>
P<sub>i </sub>: Abstract operation<br>
S : Set of abstract states<br>
s : Element of an S<br>
s': Abstract state after operation<br>
inv : Invariant<br>
invA : Abstract invariant<br>
invC :  Concrete invariant>
Pre-P<sub>i</sub> : Precondition for operation i<br>
Post-P<sub>i</sub> : Postcondition for operation i<br>
& : And <br>
=> : Implies <br>

Example:
```
(invA(s) & Pre-Pi(s, args) &
Post-Pi(s, args, s', res)) => invA(s')
```
Abstract invariant `invA` over state `s` and the precondition of `s` and the postcondition of `s` and it's `args` lead to `s'` and `res` which implies that the `invA` is over `s'`. This means after the operation the invariant must still be true for the state after the operation.

Q<sub>i </sub>: Concrete operation<br>
t : Set of concrete states<br>
T : Element of an T<br>
retr : Retrieve function which maps concrete states to abstract states, retr(t) = s<br>

```
∀s ∈ S: invA(s)
(∃ t ∈ T: invC(t) & s = retr(t))
```
For all abstract state elements `s` in the abstract set `S` the abstract invariant `invA` of `s` must be true, then there must exist a concrete state element `t` in the concrete set `T` so that the concrete invariant `invC` is true such that applying the retrieve function to the concrete element of state `t` must yield in a abstract element of `s`.

**Summary**<br>
1. The top level specification must matches the requirements.
2. Operations at each level must preserve invariants.
3. Each refinement is adequate.
4. Each refinement is total.
5. Concrete operation preconditions and post conditions model their abstract counterparts

### P3L9 Middleware
Middleware is computer software that provides services to software applications beyond those available from the operating system. It can be described as "software glue".

Middleware makes it easier for software developers to implement communication and input/output, so they can focus on the specific purpose of their application [Wikipedia](https://en.wikipedia.org/wiki/Middleware).

**Exercise:**<br>
Come up with an architecture for a website and it's infrastructure. The user uses the website to vote anonymous on a set of questions, after the user is done the website responds with a feedback how other people voted on the questions. The choices are recorded and anonymous.

The following characteristic issues should be addressed:
  - Network communication<br>
  How are errors handled, for example synchronous errors when a particular request is made and the system is waiting for a response or asynchronous, spontaneous issuing of some notifications. The primary concern is the reliable delivery of those messages. It also is important to think about how data is represented on different system. How to manage concurrent transactions an consistency of data, as well as serialization / marshalling, byte ordering, character sets, word length on different systems. A solution could be a self definition, not only sending the data but also sending the representation. Transactions should be ACID, atomic, consistency-perceiving, isolated and durable.
    - Atomic
    A transaction should be treated as on step, with no intermediate steps in between.
    - Consistency-perceiving
    The database should maintain integrity.
    - Isolated
    Other transaction should not see intermediate transactions.
    - Durable
    After a commit the transaction should be persistent.


  - Coordination<br>
  Action need to be synchronized between system, this could either be synchronous or asynchronous. The control structure need to be defined, who is in charge e.g. for updating content, the client polling or the server broadcasting? The system has to be robust, it should be able to handle on parts of the application going down. The system should also have a certain availability.

  - Reliability<br>
  Component of distributed systems fail sometimes. What is the ratio of down time to total time. There could also be issues with handling of failure to deliver or multiple deliveries. Different policies can be defined in order to cover those cases.

  - Scalability<br>
  How can we deal with higher load, how easy is it to grow? To what extend will adding machines change system architecture or components.

  - Heterogeneity<br>
  What kind of hardware, operating system, protocols, API's, programming languages are we using? A solution could be using standard API's and protocols.

There are four types of middle ware:
  1. Transactional middleware<br>
  Supports transactions involving components that run on distributed hosts.
  2. Message-Oriented Middleware<br>
  Message-oriented middleware (MOM) supports the communication between distributed system components by facilitating message exchange.
  3. Procedural Middleware<br>
  Is an external function call which is usually synchronous.
  4. Object and Component Middleware<br>
  Is an extension of 3, the idea here is to make object-oriented principles, such as object identification through references and inheritance, available for the development of distributed systems.

Web services<br>
A software system designed to support interoperable machine to machine interaction over a network. Web services are frequently just web API's that can be accessed over a network, such as the internet and executed on a remote system hosting the requested services.

Service oriented architecture<br>
A service-oriented architecture (SOA) is a style of software design where services are provided to the other components by application components, through a communication protocol over a network. The basic principles of service-oriented architecture are independent of vendors, products and technologies. A service is a discrete unit of functionality that can be accessed remotely and acted upon and updated independently, such as retrieving a credit card statement online [Wikipedia](https://en.wikipedia.org/wiki/Service-oriented_architecture).

### P4L1 Components
**What is a software component?**<br>
A software component is a software element that conforms to a component model and can be independently deployed and composed without modification according to a composition standard.

**What is a component model?**<br>
A component model defines specific interaction and composition standards. A component model implementation is the dedicated set of executable software elements required to support the execution of components that conform to the model.

**What is a composition?**<br>
The combination of two or more software components yielding a new component behavior at a different
level of abstraction. The characteristics of the new
component behavior are determined by the components being combined and by the way they are combined [Bill Councill](http://heim.ifi.uio.no/~frank/inf5040/CBSE/Component-Based_Software_Engineering_-_ch1.pdf).

Does it make sense to use a 3rd party solution in order to solve the problem?

### P4L2 Coffee Maker Exercise
Exercise consists if using the textual description of the coffee  maker and its API description to create a class diagram.

**The Mark IV Special Coffee Maker**<br>
The **Mark IV Special** makes up to 12 *cups of coffee* at a time. The user places a *filter* in the *filter holder*, fills the *filter* with *coffee grounds*, and slides the **filter holder** into its *receptacle*. The user then pours up to 12 cups of *water* into the **water strainer** and presses the *Brew button*. The *water* is heated until boiling. The *pressure* of the evolving *steam* forces the *water* to be sprayed over the *coffee grounds*, and *coffee* drips through the *filter* into the *pot*. The *pot* is kept warm for extended periods by a **warmer plate**, which only
turns on if there is *coffee* in the *pot*. If the *pot* is removed from the *warmer plate* while water is being sprayed over the *grounds*, the flow of *water* is stopped so that brewed *coffee* does not spill on the *warmer plate*. The following hardware needs to be monitored or controlled:

- The heating element for the boiler. It can be turned on or off.
- The heating element for the warmer plate. It can be turned on or off.
- The sensor for the warmer plate. It has three states: warmerEmpty, potEmpty, potNotEmpty.
-  A sensor for the boiler, which determines whether there is water present. It has
two states: boilerEmpty or boilerNotEmpty.
- The Brew button. This is a momentary button that starts the brewing cycle. It has an indicator that lights up when the brewing cycle is over and the coffee is ready.
- A pressure-relief valve that opens to reduce the pressure in the boiler. The drop in
pressure stops the flow of water to the filter. It can be opened or closed.

The hardware for the Mark IV has been designed and is currently under development.
The hardware engineers have even provided a low-level API for us to use, so we don’t
have to write any bit-twiddling I/O driver code. The code for these interface functions is
shown in Listing 11–1. If this code looks strange to you, just keep in mind that it was written
by hardware engineers [Heuristics and Coffee](https://s3.amazonaws.com/content.udacity-data.com/courses/gt-cs6310/readings/gt-sad-martin-chapter-11.pdf).

**Identify hardware components**<br>
The following coffee maker hardware components are available in the system:

| Description    | States     |
| :------------- | :------------- |
| Heating element boiler  | On - Off  |
| Heating element warmer plate| On - Off  |
| Sensor warmer plate| warmerEmpty - potEmpty - potNotEmpty  |
| Sensor boiler | boilerEmpty - boilerNotEmpty  |
| Brew button | pressed - notPressed  |
| Indicator that light | On - Off  |
| A pressure-relief valve | opened - closed |

**Identify hardware component operations**<br>
The following API calls are provided:

| Signature    | Description     |
| :------------- | :------------- |
| int getWarmerPlateStatus()      | This function returns the status of the warmer-plate sensor. This sensor detects the presence of the pot and whether it has coffee in it.|
| int getBoilerStatus()      | This function returns the status of the boiler switch. The boiler switch is a float switch that detects if there is more than 1/2 cup of water in the boiler. |
| int getBrewButtonStatus()      | This function returns the status of the brew button. The brew button is a momentary switch that remembers its state. Each call to this function returns the remembered state and then resets that state to BREW_BUTTON_NOT_PUSHED. |
| void setBoilerState(int boilerStatus)     | This function turns the heating element in the boiler on or off  |
| setWarmerState(int warmerState)      | This function turns the heating element in the warmer plate on or off.  |
| void setIndicatorState(int indicatorState)     | This function turns the indicator light on or off. The indicator light should be turned on at the end of the brewing cycle. It should be turned off when the user presses the brew button. |
| void setReliefValveState(int reliefValveState)     | This function opens and closes the pressure-relief valve. When this valve is closed, steam pressure in the boiler will force hot water to spray out over the coffee filter. When the valve is open, the steam in the boiler escapes into the environment, and the water in the boiler will not spray out over the filter. |

Steps in order to solve the exercise using the OOP approach:
  1. Identify objects.
  2. Optimizing the objects based on the API calls.
  3. Optimizing the objects adding attributes.
  4. Identify possible operations.
  5. Removing unneeded operations.
  6. Use Cases for the coffee maker.
  7. Sequence description for the use cases.
  8. State diagram.
  9. Class diagram.

**1. Identify objects**<br>
After examining the specification the following objects have been identified:
  - Mark IV Special coffee maker
  - Cups
  - Filter holder
  - Filter receptacle
  - Filter
  - Water strainer
  - Warmer plate
  - Coffee grounds
  - Pot
  - Brew button

**2. Optimizing the objects based on the API calls**<br>
The list from step 1 is used in order to remove unneeded objects and allocate API calls to the existing ones in such way it make sense.<br>
  - CoffeeMaker
    - `setIndicatorState`
    - `getBrewButtonStatus`
  - WarmerPlate
    - `getWarmerPlateStatus`
    - `setWarmerState`
  - WaterStrainer
    - `getBoilerStatus`
    - `setBoilerState`
    - `setReliefValveState`

**3. Optimizing the objects adding attributes**<br>
The following list shows additional added attributes.
- CoffeeMaker
  - `bool isBrewing`
  - `bool isBrewingDone`
- WarmerPlate
 - `bool isPlateOn`
- WaterStrainer
  - `bool isBoilerOn`

**4. Identify possible operations**<br>
The following operations or events are available based on action verbs found in the specification:
  - Filter loaded
  - Filter in receptacle
  - Water provided
  - User presses brew button
  - Heating water
  - Water heated
  - Water running over ground coffee
  - Pot filling
  - Pot filled
  - Pot in place
  - Warmer heating
  - Pot removed
  - Heater off
  - Coffee brewed

**5. Removing unneeded operations**<br>
Not all operations make sense, some would require additional hardware, but since the hardware and it's API is already provided we are able to remove some of the identified operations. It would make sense to use the identified elements if we could design the hardware based on our needs, but this is not the case for this exercise:<br>
- ~~Filter loaded~~<br>
We are not able to detect if a filter is loaded, thus this operation is not needed.
- ~~Filter in receptacle~~<br>
Same as above applies.
- Water provided<br>
Covered by `getBoilerStatus`.  
- User presses brew button<br>
Covered by `getBrewButtonStatus`.
- Heating water<br>
Covered by `bool isBrewing`.
- ~~Water heated~~<br>
The water will automatic start poring onto the coffee if the `ReliefValve` is open, so we only need to make sure that the valve is open after the heater is turned on.
- Water running over ground coffee<br>
Covered by statement before as well as by `bool isBrewing`.
- Pot filling<br>
Covered by statement before as well as by `bool isBrewing`.
- Pot filled<br>
Covered by `getWarmerPlateStatus`.
- Pot in place<br>
Covered by `getWarmerPlateStatus`.
- Warmer heating<br>
Covered by `bool isPlateOn`.
- Pot removed<br>
Covered by `getWarmerPlateStatus`.
- Heater off<br>
Covered by `bool isPlateOn`.
- Coffee brewed<br>
Covered by `bool isBrewingDone`.

**6. Use Cases for the coffee maker**<br>
The following use cases are relevant for the coffee maker:<br>
1.  Brewing coffee and keep fresh brewed coffee warm
3.  Warm existing coffee in pot

**7. Sequence description for the use cases**<br>
Brewing coffee and keep warm<br>
It's assumed that the user placed a filter with coffee grounds into the filter holder and the filter holder is closed.<br>
- Press brew button.
- Check if water is in water strainer `getBoilerStatus()`.
- Check if empty pot is on warmer plate `getWarmerPlateStatus()`.
- Close Valve `setReliefValveState(VALVE_CLOSED)`.
- Heat water in boiler as long as boiler contains water.
- Water flows over coffee into pot.
- Warmer plate turns on after brewing is done.
- Light indicator when coffee is done.
- Turn warmer plate off if pot is empty

Warm existing coffee in pot<br>
This feature warms or keeps already brewed coffee warm, if a pot with a certain level of a liquid is detected.
- Press brew button.
- Check if pot with liquid is on warmer plate.
- Turn on warmer plate.
- Light indicator.
- Turn warmer plate off if pot is empty

**8. State diagram**<br>

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P4L2/StateDiagram_coffee_machine_OOP.JPG" alt="State diagram Coffee machine OOP."/></p>

The initial state of the coffee maker state machine is the `PowerOff` state, as soon as the machine gets plugged in `[a.]: [isMachinePlugedIn]` the machine powers on. Within the main state machine `CoffeeMachine` there are two possibilities of an implementation, `A` or `B`, `B` consists of two parallel running state machines the `WaterStrainer` machine state describing the state of the boiler, and the `WarmerPlate` state. The detailed description of the state transitions is listed below:<br>

```
A
[Idle]: during:
{
  setReliefValveState(VALVE_CLOSED);
  setBoilerState(BOILER_OFF);
  setWarmerState(WARMER_OFF);
  setIndicatorState(INDICATOR_OFF);

  isBrewing   = FALSE;
  isBoilerOn  = FALSE;
  isPlateOn   = FALSE;
}
[Brewing]: during:
{
  setReliefValveState(VALVE_OPEN);
  setBoilerState(BOILER_ON);

  isBrewing   = TRUE;
  isBoilerOn  = TRUE;
}
[Warming]: during:
{
  setWarmerState(WARMER_ON);
  setIndicatorState(INDICATOR_ON);

  isBrewing   = FALSE;
  isBoilerOn  = FALSE;
  isPlateOn   = TRUE;
}

B
[BoilerOff]: during:
{
  setReliefValveState(VALVE_CLOSED);
  setBoilerState(BOILER_OFF);

  isBrewing   = FALSE;
  isBoilerOn  = FALSE;
}

[BoilerOn]: during:
{
  setReliefValveState(VALVE_OPEN);
  setBoilerState(BOILER_ON);

  isBrewing   = FALSE;
  isBoilerOn  = FALSE;
}

[PlateOff]: during:
{
  setWarmerState(WARMER_OFF);

  isPlateOn   = FALSE;
}

[PlateOn]: during:
{
  setWarmerState(WARMER_ON);

  isPlateOn   = TRUE;
}

[1.][7.]: [(getBrewButtonStatus() == BREW_BUTTON_PUSHED) && (getWarmerPlateStatus() == POT_NOT_EMPTY)]
[2.][5]: [(getBrewButtonStatus() == BREW_BUTTON_PUSHED) && (getBoilerStatus() == BOILER_NOT_EMPTY) && getWarmerPlateStatus() == POT_EMPTY]
[2.1]: [getWarmerPlateStatus() == WARMER_EMPTY]
[3.]: [(getBoilerStatus() == BOILER_EMPTY)]
[4.][8]: [getWarmerPlateStatus() == POT_EMPTY]
[6.]: [getWarmerPlateStatus() == WARMER_EMPTY] / setIndicatorState(INDICATOR_ON);
```

**9. Class diagram**<br>
The following image shows a possible solution for the class diagram:<br>

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P4L2/ClassDiagram_coffee_machine_OOP.JPG" alt="Class diagram Coffee machine OOP."/></p>

**Use case approach, role based design**<br>
Martin also describes the possibility to start with the use cases and then use a superposition of collaboration diagrams in order to come up with a architecture.

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Software_architecture_and_design/Images_and_diagrams/P4L2/CollaborationDiagram_coffee_machine_OOP.JPG" alt="Collaboration diagram Coffee machine OOP."/></p>

The above image shows the message flow for different invariants of a use case:
  - a: `User Interface` gets triggered and checks if `Hot Water Source isReady`. The next step then is to check the `Containment Vessel isReady` and then start the `Hot Water Source` and after wards the `Containment Vessel`.
  - b: Is the use case for pausing and resuming the boiling process of the `Hot Water Source`.
  - c: Is the use case the brewing is complete, the `Containment Vessel` needs to be informed that the process is done, because it needs to monitor the warming process, as well as the `User Interface` needs to be informed.
  - d: Is the use case for the warmer plate to turn off after either a certain amount of time or if no coffee is left.

**Dependency inversion**<br>
Including API directly as class methods leads to direct coupling which should be avoided in order to be as generic and extensible as possible.

Dependency inversion principle is a software design principle which provides us the guidelines to write loosely coupled classes. According to the definition of Dependency inversion principle:

High-level modules should not depend on low-level modules. Both should depend on abstractions.
Abstractions should not depend upon details. Details should depend upon abstractions [Code Project](https://www.codeproject.com/Articles/615139//Articles/615139/An-Absolute-Beginners-Tutorial-on-Dependency-Inver).

### P4L3 Object Design
The challenge of coming up with a OOD is quit difficult, because the result from OOA can not be directly translated in actual code, some concepts are not supported in programming languages, or the mapping is not obvious. The following elements need to be defined in respect to the implementation:<br>
  1. Methods
  - New classes
  - Generalization
  - Associations
  - Dependencies
  - Implementing control
  - Abstract classes and interfaces

**1. Methods**<br>
Where do the methods come from? Methods are usually signals from the analysis class model. They could also com from dynamic models, and they are usually events, actions, activities. The methods need to be allocated to classes. In addition common methods could be included in order to construct and destruct, setters and getters ... .

**2. New classes**<br>
Classes should represent or reflect system components in order to provide traceability and consistency. Classes implement associations and relationships between components. Classes can be part of new levels of abstractions.

**3. Generalization**<br>
How to model UML relationships? Object oriented programming languages usually support inheritance via subclassing. Generalizations between two classes means that all instances of the derived class are also instances of the parent class. Inheritance is an implementation technique whereby messages sent to a child may be delegated to a parent, it can be uses in order to implement generalization. Children classes can add features but they should not override only if the behavior is consistent with its parent, it should contain the same behavior as baseline.

**4. Associations**<br>
Associations are not directly supported, the directionality is very important, as well as cardinality, meaning the 1 to n relationship need to be defined. There a to main types of associations:<br>
  - One way associations<br>
  They can be easily implemented by using a pointer to a target instance. This is also possible for multiple instances.
  - Two way associations<br>
  They can be similar implemented with the usage of two pointer similar to a linked list, this could lead to integrity issues because of tight coupling which could be solved by reference counting. As a different solution a collection class could be used in order to keep track of multiple entities, for example a hash map.

**5. Dependencies**<br>
Dependencies can be implemented in many different ways. The significant is that one classes use some part of the other class. It could be containing a instance of the target class or just using elements of it e.g. of a global class. You could also just receive elements of the depended class e.g. as a return value of a method. The target could also be imported into the current class.  

**6. Implementing control**<br>
Means describing the allowable behavior between classes, it's tightly coupled with states, meaning attributes must be changed depended on invocation and interactions.

**7. Abstract classes and interfaces**<br>
In order to increase maintainability, abstractions can be introduced. The corresponding elements for the implementation are interfaces or virtual classes.

### P4L4 Design patterns
Design patterns represent the best practices used by experienced object-oriented software developers. Design patterns are solutions to general problems that software developers faced during software development. These solutions were obtained by trial and error by numerous software developers over quite a substantial period of time.

**The composite pattern**<br>
Composite pattern is one of the most widely used patterns in the industry and addresses a very significant and subtle problem. It is used whenever the user wants to treat the individual object in the same way as the collection of those individual objects for e.g you might want to consider a page from the copy as same as the whole copy which is basically a collection of the pages or if you want to create a hierarchy of something where you might want to consider the whole thing as the object .
Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly [GeeksforGeeks](https://www.geeksforgeeks.org/composite-pattern-cpp/).

**Creational Pattern**<br>
Creational design patterns are design patterns that deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design. Creational design patterns solve this problem by somehow controlling this object creation [sourcemaking](https://sourcemaking.com/design_patterns/creational_patterns).

- Abstract Factory<br>
Creates an instance of several families of classes.
- Builder<br>
Separates object construction from its representation.
- Factory Method<br>
Creates an instance of several derived classes.
- Prototype<br>
A fully initialized instance to be copied or cloned.
- Singleton<br>
A class of which only a single instance can exist.

**Structural Pattern**<br>
structural design patterns are design patterns that ease the design by identifying a simple way to realize relationships among entities [sourcemaking](https://sourcemaking.com/design_patterns/structural_patterns).

- Adapter<br>
Match interfaces of different classes.
- Bridge<br>
Separates an object’s interface from its implementation.
- Composite<br>
A tree structure of simple and composite objects.
- Decorator<br>
Add responsibilities to objects dynamically.
- Facade<br>
A single class that represents an entire subsystem.
- Flyweight<br>
A fine-grained instance used for efficient sharing.
- Private Class Data<br>
Restricts accessor/mutator access.
- Proxy<br>
An object representing another object.

**Behavioral Pattern**<br>
behavioral design patterns are design patterns that identify common communication patterns between objects and realize these patterns. By doing so, these patterns increase flexibility in carrying out this communication [sourcemaking(https://sourcemaking.com/design_patterns/behavioral_patterns).

### P4L5 Design principles
Software design principles represent a set of guidelines that helps us to avoid having a bad design. Developing design is a cumbersome process as most expansive errors are often introduced in this phase. Moreover, if these errors get unnoticed till later phases, it becomes more difficult to correct them. Therefore, a number of principles are followed while designing the software. These principles act as a framework for the designers to follow a good design practice [ecomputernotes](http://ecomputernotes.com/software-engineering/principles-of-software-design-and-concepts).

- Coupling<br>
Coupling is the degree of interdependence between software modules; a measure of how closely connected two routines or modules are; the strength of the relationships between modules.

- Cohesion<br>
Cohesion is the extend to which a model has a single purpose. Cohesion also refers to the level of strength and unity with which different components of a software program are inter-related with each other.

- Orthogonality<br>
Orthogonality is an important concept, addressing how a relatively small number of components can be combined in a relatively small number of ways to get the desired results. It is associated with simplicity; the more orthogonal the design, the fewer exceptions.

- Information hiding<br>
information hiding is the principle of segregation of the design decisions in a computer program that are most likely to change, thus protecting other parts of the program from extensive modification if the design decision is changed.

**Design principle catalogue**<br>
**Liskov substitution**<br>
The principle defines that objects of a superclass shall be replaceable with objects of its subclasses without breaking the application. That requires the objects of your subclasses to behave in the same way as the objects of your superclass [stackify](https://stackify.com/solid-design-liskov-substitution-principle/).

**Law of demeter**<br>
The Law of Demeter (LoD) is a simple style rule for designing object-oriented systems. "Only talk to your friends" is the motto.
- Each unit should have only limited knowledge about other units: only units "closely" related to the current unit.
- Each unit should only talk to its friends; don't talk to strangers.
- Only talk to your immediate friends.

Example an object `A` can request a service (call a method) of an object instance `B`, but object `A` should not "reach through" object `B` to access yet another object, `C`, to request its services. Doing so would mean that object `A` implicitly requires greater knowledge of object `B`'s internal structure. Instead, `B`'s interface should be modified if necessary so it can directly serve object `A`'s request, propagating it to any relevant subcomponents. Alternatively, `A` might have a direct reference to object `C` and make the request directly to that. If the law is followed, only object `B` knows its own internal structure [Wikipedia](https://en.wikipedia.org/wiki/Law_of_Demeter).

**Hollywood principles**<br>
At its most basic level, the principle is about reducing the coupling in a software system. It gets back to the well known phrase in software development: loose coupling and high cohesion. You can keep classes loosely coupled by ensuring that you don’t have unnecessary references and you are referencing classes and other subsystems properly [matthewtmead](http://matthewtmead.com/blog/hollywood-principle-dont-call-us-well-call-you-4/).

**Dependency inversion principle**<br>
The general idea of this principle is as simple as it is important: High-level modules, which provide complex logic, should be easily reusable and unaffected by changes in low-level modules, which provide utility features. To achieve that, you need to introduce an abstraction that decouples the high-level and low-level modules from each other.

Based on this idea, Robert C. Martin’s definition of the Dependency Inversion Principle consists of two parts:

- High-level modules should not depend on low-level modules. Both should depend on abstractions.
- Abstractions should not depend on details. Details should depend on abstractions.

**Open-Closed principle**<br>
“Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.” The general idea of this principle is great. It tells you to write your code so that you will be able to add new functionality without changing the existing code. That prevents situations in which a change to one of your classes also requires you to adapt all depending classes
