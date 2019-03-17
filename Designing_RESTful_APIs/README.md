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

## Lesson 1: What's and Why's of APIs
**What are APIs**<br>
APIs are application programming interfaces, APIs can be described as building blocks of software components or applications. A comprehensive metaphor is a wall socket, the socket represents a interface to a service better know as electricity. The user is comfortable able to use the service if he is in compliance with the policy of the service provider, meaning if the consumer decides to agree on a contract with a energy provider, then the provider invokes the rights for the user to access the service, though out a defined interface the wall socket. The wall socket has specific properties, such as a physical shape for a plug as well as a defined voltage and a maximum current. Those properties are defined by the service provider, e.g. the API provider. A more formal definition is the following one:<br>

*In computer programming, an application programming interface (API) is a set of subroutine definitions, communication protocols, and tools for building software. In general terms, it is a set of clearly defined methods of communication among various components. A good API makes it easier to develop a computer program by providing all the building blocks, which are then put together by the programmer. An API may be for a web-based system, operating system, database system, computer hardware, or software library [Wikipedia](https://en.wikipedia.org/wiki/Application_programming_interface).*   

**Web APIs**<br>
A web API is a specific type of API which is used for either a web server or web browser, they are typically HTTP based.  The API itself defines a set of endpoints, request messages and response structures. It is a standard approach also to identify the supported response media types. XML and JSON are two favorite examples of response media types that can be easily interpreted by API consumers.

**The OSI layers**<br>
The Open System Interconnection (OSI) is a reference model for how various applications communicate over any network. The purpose behind this model was to provide developers, programmers, engineers, vendors and all the associated people a standard that can serve as a guide for them using which they would be able to create communication equipment and software inter operable. The following image shows the seven layers of the OSI model and its use protocols, a detailed description can be found [here](https://www.bmc.com/blogs/osi-model-7-layers/).

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Designing_RESTful_APIs/Images/osi-model-7.jpg" alt="OSI layer model example."/></p>

**The Web Service Layer**<br>
In a web service, the Web technology such as HTTP—originally designed for human-to-machine communication—is utilized for machine-to-machine communication, more specifically for transferring machine-readable file formats such as XML and JSON. In practice, a web service commonly provides an object-oriented web-based interface to a database server, utilized for example by another web server, or by a mobile app, that provides a user interface to the end user. Many organizations that provide data in formatted HTML pages will also provide that data on their server as XML or JSON, often through a web service to allow syndication, for example Wikipedia's Export. Another application offered to the end user may be a mashup, where a web server consumes several web services at different machines, and compiles the content into one user interface [Wikipedia](https://en.wikipedia.org/wiki/Web_service).

When talking about API (application programming interface) architectures, it’s common to want to compare SOAP vs. REST, two of the most common API paradigms.

**REST**<br>
REST determines how the API looks like. It stands for “Representational State Transfer”. It is a set of rules that developers follow when they create their API. One of these rules states that you should be able to get a piece of data (called a resource) when you link to a specific URL.

Each URL is called a request while the data sent back to you is called a response.

- REST is all about simplicity, thanks to HTTP protocols.
- REST APIs facilitate client-server communications and architectures. If it’s RESTful, it’s built on this client-server principle, with round trips between the two passing payloads of information.
- REST APIs use a single uniform interface. This simplifies how applications interact with the API by requiring they all interface in the same way, through the same portal. This has advantages and disadvantages; check with your developer to see if this will affect implementation changes down the road.
- REST is optimized for the web. Using JSON as its data format makes it compatible with browsers.
- REST is known for excellent performance and scalability. But, like any technology, it can get bogged down or bog down your app. That’s why languages like GraphQL have come along to address problems even REST can’t solve [UpWork](https://www.upwork.com/hiring/development/soap-vs-rest-comparing-two-apis/).

**SOAP**<br>
SOAP (Simple Object Access Protocol) is its own protocol, and is a bit more complex by defining more standards than REST—things like security and how messages are sent. These built-in standards do carry a bit more overhead, but can be a deciding factor for organizations that require more comprehensive features in the way of security, transactions, and ACID (Atomicity, Consistency, Isolation, Durability) compliance.

- SOAP has tighter security. WS-Security, in addition to SSL support, is a built-in standard that gives SOAP some more enterprise-level security features, if you have a requirement for them.
- Successful/retry logic for reliable messaging functionality. Rest doesn’t have a standard messaging system and can only address communication failures by retrying. SOAP has successful/retry logic built in and provides end-to-end reliability even through SOAP intermediaries.
- SOAP has built-in ACID compliance. ACID compliance reduces anomalies and protects the integrity of a database by prescribing exactly how transactions can interact with the database. ACID is more conservative than other data consistency models, which is why it’s typically favored when handling financial or otherwise sensitive transactions [UpWork](https://www.upwork.com/hiring/development/soap-vs-rest-comparing-two-apis/).

## Lesson 2: Accessing Published APIs
The Hypertext Transfer Protocol (HTTP) is an application-level protocol for distributed, collaborative, hypermedia information systems. This is the foundation for data communication for the World Wide Web (i.e. internet) since 1990. HTTP is a generic and stateless protocol which can be used for other purposes as well using extensions of its request methods, error codes, and headers.

Basically, HTTP is a TCP/IP based communication protocol, that is used to deliver data (HTML files, image files, query results, etc.) on the World Wide Web. The default port is TCP 80, but other ports can be used as well. It provides a standardized way for computers to communicate with each other. HTTP specification specifies how clients' request data will be constructed and sent to the server, and how the servers respond to these requests [tutorialspoint](https://www.tutorialspoint.com/http/http_overview.htm).

**HTTP Version**<br>
HTTP uses a <major>.<minor> numbering scheme to indicate versions of the protocol. The version of an HTTP message is indicated by an HTTP-Version field in the first line. Here is the general syntax of specifying HTTP version number:
```
HTTP-Version   = "HTTP" "/" 1*DIGIT "." 1*DIGIT
```

**Uniform Resource Identifiers**<br>
Uniform Resource Identifiers (URI) are simply formatted, case-insensitive string containing name, location, etc. to identify a resource, for example, a website, a web service, etc. A general syntax of URI used for HTTP is as follows:
```
URI = scheme:[//authority]path[?query][#fragment]

authority = [userinfo@]host[:port]
```

Here is an example:<br>
```
 https://john.doe@www.example.com:123/forum/questions/?tag=networking&order=newest#top
 |scheme|userinfo|   host       |port|   path        | query                         |
```
**HTTP Message**<br>
HTTP messages are how data is exchanged between a server and a client. There are two types of messages: requests sent by the client to trigger an action on the server, and responses, the answer from the server.

HTTP messages are composed of textual information encoded in ASCII, and span over multiple lines. In HTTP/1.1, and earlier versions of the protocol, these messages were openly sent across the connection. In HTTP/2, the once human-readable message is now divided up into HTTP frames, providing optimization and performance improvements [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messageshttps://developer.mozilla.org/en-US/docs/Web/HTTP/Messages).

<p align="center">
<img src="https://raw.githubusercontent.com/NaPiZip/Udacity_notes/master/Designing_RESTful_APIs/Images/http-msg-structure.jpg" alt="HTTP message structure example."/></p>

The image above shows a HTTP request as well as it's response. Both the request and response message have the same structure, containing the following elements, detailed information can be found [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages):
- Start line<br>
 Describing the requests to be implemented, or its status of whether successful or a failure. This start-line is always a single line.
- Optional HTTP header<br>
 An optional set of HTTP headers specifying the request, or describing the body included in the message.
- Empty line<br>
  A blank line indicating all meta-information for the request have been sent.
- Optional Body<br>
 An optional body containing data associated with the request (like content of an HTML form), or the document associated with a response. The presence of the body and its size is specified by the start-line and HTTP headers

## Lesson 3: Creating your own API Endpoints
Lesson 3 mostly contains of examples and quizzes, this section only gives a brief overview due to the fact that most information's with respect to the exercise's can be found online and thus, don't need to be discussed again. The quizzes try to cover the following content:

- Quiz 3<br>
  How does the routing with Flask work in general? Details can be found [here](http://flask.pocoo.org/docs/0.12/).
- Quiz 4<br>
  Introduces different kinds of request methods, what they do and how to implement them. Details can be found [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).
- Quiz 5<br>
  Is using `sqlalchemy` which is a ORM (Object relational Mapper) database. Details can be found [here](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html).

**Quiz 6<br>**
Is an exercise for a mashup application proofing the learned content is understood. Below is an example of an API `POST` request which should be implemented:

```
localhost:5000/restaurants?location=New+York+NY&mealType=spaghetti
```
The actions for the API `POST` request are the followed:
  1. Get the geocode of the location
  2. Find a nearby restaurant
  3. Store it into a data base
  4. Return a JSON object with restaurant information

The following example shows a `GET` request for the same route:
```
localhost:5000/restaurants
```
The actions for the API `GET` request are the followed:
 1. Return all saved restaurants containing the following information's in JSON format: `{restaurant_name, id, restaurant_address, restaurant_image}`.

In addition a more specialized `GET` request should be implemented to the following route:
```
localhost:5000/restaurants/<int:id>
```
The actions for the API `GET` request are the followed:
  1. Return the specific information querying the provided `id` of the `GET` request, the information should be in JSON format: `{restaurant_name, id, restaurant_address, restaurant_image}`.

Also a `UPDATE` request should be implemented using the following structure of an API call, which updates the specified entity, only if it already exists:
```
localhost:5000/restaurants/<int:id>?name=Some+Bar&address=New+York+NY&imageUrl=url+here
```

The last request is a `DELETE` request, it should delete the specified element, given its `id`:
```
localhost:5000/restaurants/<int:id>
```

The solutions can be found in the repository.

## Lesson 4: Securing your API
**HTTP Basic Auth**<br>
In the context of an HTTP transaction, basic access authentication is a method for an HTTP user agent (e.g. a web browser) to provide a user name and password when making a request. In basic HTTP authentication, a request contains a header field of the form Authorization: Basic <credentials>, where credentials is the base64 encoding of id and password joined by a colon. For details see [Wikipedia](https://en.wikipedia.org/wiki/Basic_access_authentication).

Client side

When the user agent wants to send authentication credentials to the server, it may use the Authorization field.

The Authorization field is constructed as follows:

- The username and password are combined with a single colon (:). This means that the username itself cannot contain a colon.
- The resulting string is encoded into an octet sequence. The character set to use for this encoding is by default unspecified, as long as it is compatible with US-ASCII, but the server may suggest use of UTF-8 by sending the charset parameter.[7]
- The resulting string is encoded using a variant of Base64.
- The authorization method and a space (e.g. "Basic ") is then prepended to the encoded string.

For example, if the browser uses Aladdin as the username and OpenSesame as the password, then the field's value is the base64-encoding of `Aladdin:OpenSesame`, or `QWxhZGRpbjpPcGVuU2VzYW1l`. Then the Authorization header will appear as:

```
Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l
```

**Token based authentication**<br>
The general concept behind a token-based authentication system is simple. Allow users to enter their username and password in order to obtain a token which allows them to fetch a specific resource - without using their username and password. Once their to ken has been obtained, the user can offer the token - which offers access to a specific resource for a time period - to the remote site. Using some form of authentication: a header, GET or POST request, or a cookie of some kind, the site can then determine what level of access the request in question should be afforded, link can be found [here](https://www.w3.org/2001/sw/Europe/events/foaf-galway/papers/fp/token_based_authentication/).

The basic workflow for token based authentication is as followed:

  - User Requests Access with Username / Password
  - Application validates credentials
  - Application provides a signed token to the client
  - Client stores that token and sends it along with every request
  - Server verifies token and responds with data

**Rate limiting**<br>
Rate limiting is used to control the amount of incoming and outgoing traffic to or from a network. For example, let’s say you are using a particular service’s API that is configured to allow 100 requests/minute. If the number of requests you make exceeds that limit, then an error will be triggered. The reasoning behind implementing rate limits is to allow for a better flow of data and to increase security by mitigating attacks such as DDoS.

Rate limiting also comes in useful if a particular user on the network makes a mistake in their request, thus asking the server to retrieve tons of information that may overload the network for everyone. With rate limiting in place however, these types of errors or attacks are much more manageable. A link to the article can be found here [link](https://www.keycdn.com/support/rate-limiting).
A [tutorial](http://flask.pocoo.org/snippets/70/) is also available. 
