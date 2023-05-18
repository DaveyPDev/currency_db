### Conceptual Exercise

Answer the following questions below:

What are important differences between Python and JavaScript?

* Python has a more clean and simple syntax. JS has a more complex syntax.
* Python is determined at runtime. JS can change during runtime
* Python is used for many tasks like data, machine learning, web development. JS is mostly used for interactive interfaces and web development.
*  Python is server side and JS is mainly on the client side

Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

*   get()
*   try:

What is a unit test?

* small sections of code tested before adding to a whole project


 What is an integration test?
 
* testings sections of code together to see if they function properly

 What is the role of web application framework, like Flask?
 
*  tools like modules and libraries to help develope applicatins faster

 You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  
*   the route approach /foods/pretzel is normally done with a RESTful API
*   the url query is used for searching / filtering for data criteria
  

 How do you collect data from a URL placeholder parameter using Flask?
 
*  passes a variable name as an argument to a specific function

 How do you collect data from the query string using Flask?
 
*  request.args is a dictionary object that maps parameters to their values 

 How do you collect data from the body of the request using Flask?
 
*  request.data / request.get_data()

 What is a cookie and what kinds of things are they commonly used for?
 
*  data stores on a users computer sent to a web server with the users preferences on that website

 What is the session object in Flask?
 
*  stores a users data server side used for requests and responses

 What does Flask's `jsonify()` do?
 
*  response that returns json data from a python object
