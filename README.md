The SNHU CS-340 course was multi-faceted. 
We some fundamental principles of MongoDB using the shell such as:

•	How to create a database using various forms of data such as a CSV file

•	How to create new documents

•	How to perform simple and complex queries

•	How to update documents

•	How to delete documents

•	How to create new users and configure access control

•	How to construct a data aggregation pipeline

In the next phase of the course we created a CRUD module (Create, Read, Update, Delete) in Python using PyMongo which could establish a connection with the MongoDB server through a supplied username and password. This Python module could then interface with the database in a variety of ways including simple CRUD functionality.
Finally, we used Dash, by Plotly, to create a user-interface via a web page. In an earlier project we demonstrated log-in capabilities, but in the final project we were asked to hard-code authentication. For the final project, we were asked to implement a data exploration tool which would enable a non-technical end user to navigate the database and locate documents based on certain filtering criteria. We were also asked to implement interactive elements which would process the data into graphs- one which would show a location on a map (based on the longitude and latitude fount in each of database’s documents) and one other graph of our choosing. I chose to implement a simple pi-chart which would show the attributes of all the records returned from the user’s search results.

For our final reflection on our achievements in this course, we have been asked to answer the following questions:

•	How do you write programs that are maintainable, readable, and adaptable?”

For the CRUD module, which the final project used to communicate with the database, I wrote very simple and efficient functions and provided comprehensive documentation. This module enabled me to communicate with the database in a straightforward and standardized way.

In an earlier version of the final assignment, I tried to make the Dash front-end somewhat database agnostic using the pandas python library by loading the data into a local dataframe and parsing the user’s commands into the appropriate operations on the local dataframe. This strategy would have provided a lot of adaptability by allowing the project to be used on a wide variety of database types (or even a CSV file), but instructions in later weeks indicated that we were expected to work more directly with the database server.

The final project is more integrated with the database, but there are still some elements which could be reused. The filtering widgets (tick boxes, dropdown menus, and sliders) could be repurposed with relative ease. The two graphs could also be re-used, provided that the new project implements the appropriate data source.

•	How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

The most useful technique I used in this course was breaking down tasks into progressively smaller tasks, working on one small piece at a time, and ensuring that these pieces retained modularity throughout the course. Whenever a new assignment featured a subtly different set of functionalities, I was often able to modify a few pieces instead of needing to re-write large sections of the code.

•	What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

One type of work I would enjoy doing, as a computer scientist, would be developing, fixing, or updating code to make it more efficient. While I am still a student, my understanding is that a lot of work goes into maintaining and modifying existing code rather than developing something completely new. If a company is encountering a scaling issue with their SQL database, and is looking to find a new database solution, the skills I learned in this course would help me assist in the migration and to fit the new database into existing front-ends. If a company has a database which is working fine, and has been perfectly operational since the 1990s, but is looking to replace an old GUI with a fresh new look, then the skills I learned in this course would help me implement that redesign.
