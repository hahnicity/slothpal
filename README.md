slothpal
========
A RESTful PayPal client for Python. Pun is: too much REST is sloth.

## Rationale
The paypalrestsdk project is non-pythonic, and is not thread safe.
Slothpal was designed to remedy the problems of using global variables, 
un-idiomatic coding styles and non-pep8 conformity.
To ensure thread safety we use the requests package as an alternative to 
using httplib2.

## Status
As with couch, this is an incomplete project. I was able to get the 
following items 

 * PayPal OAuth2 mechanism is well defined and tested
 * Can make requests for user information
 * Global Proxies for configuration management
 * Attribute dictionary for ease of use with the proxy

 This project, along with couch is a stub, but hopefully it will help
 people in the future if they are interested in integrating with the
 PayPal REST SDK
