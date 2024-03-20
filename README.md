TITLE : PRANJAL KUMAR JHA 

FOLLOWING IS MY APPROACH TO THE SOLUTION OF THIS PROBLEM (GAS UTILITY REQUEST HANDLING SYSTEM)

LOGIN SYSTEMS: 
  The solution requires 2 login systems 1) for the customer(user) and (2) for the customer service 
   we will require seperate storage systems for each of the above entries 


 DATABASES: 
(1)	Login details of customers 
 username,password,possibly email if we want to automatically send email about the status of their request 
     (2)Login system of customer service 
             username,password 
      (3)status of each user request 
username,request type,request status(for tracking) ,request date ,last updated date of the request status(for tracking) 
             
             both the user and the customer service have access to this(*point 3) database but the users can only see their own data 
             once the status of a request has been closed it cannot be opened again. A new request should be opened again 

FLOW OF THE WEBSITE
 HOMEPAGE
  1. The homepage that has two buttons each for customer and the customer service by clicking on them they are taken to respective login pages 
 LOGIN PAGE
   1. each login page has username and password fields for authentication
  
 AFTER AUTHENTICATION

 CUSTOMER HOMEPAGE 
   1. shows username 
   2. shows past requests that have been closed 
   3. shows currently active requests 
   4. making a new request is as simple as filling a form containing username,request type,password (username and password are necessary to avoid fake requests on someones
                                                                                                                                                                         username getting leaked) 
   5. submit button to submit the form and create a new entry in the existing list of requests

SERVICE HOMEPAGE 
   1.shows currently active requests 
    2. updating a request is as simple as filling form containing the username of the user and the new request status 

HOW TO TRACK? 
  with every request the status of request is visible (status- open,person appointed,working,closed) 
  with every request the last modified date of the status and request opened date is also visible  

HOW IS CONCURRENCY HANDLED? 
  using asynchronous code we can handle concurrent requests very well 

HOW IS FAST ACCESS OF DATA HANDLED? 
  using a nosql database like postgreSQL,or mongodb  

CURRENT FLAWS AND THEIR FIXES IN THE IMPLEMENTATION OF THE PROJECT: 
  1. lack of user registration system 
can be fixed by: creating 1 more page with form field being username,password for the user. But for the customer service it has to have an extra layer of autherization possibly to the admin
 
  2. lack of database (reason is that the database to be used was not known inorder to avoid the issue of the website not even running JSON was used)  
can be fixed by: linking a database and then performing CRUD operation through that 

  3. lack of proper user authentication  
      can be fixed by: linking a database 
  
  4. lack of any frontend 
can be fixed by: using html structuring  and some basic css

  

   
