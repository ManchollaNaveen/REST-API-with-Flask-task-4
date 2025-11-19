🍼 What is Flask? (Beginner Explanation)

Flask is a tool (a Python framework) that helps you create:

Websites APIs Backend servers

i.e 👉 A Python program that can talk to a browser or another application.

🧠 Why do we need Flask?

Without Flask, Python cannot:

Talk to a browser

Handle URLs

Receive data

Send data back

Flask gives Python these abilities.

A REST API is a way for two applications to talk to each other using the internet.

It is like a waiter in a restaurant:

You (client) tell the waiter what you want

The waiter (API) takes your request

The kitchen (server) prepares the data

The waiter brings the result back to you

That "waiter" → is the REST API

A REST API allows apps to communicate by sending requests and receiving data in a standard, simple way (usually JSON).

Flask → to create endpoints

HTTP methods → GET, POST, PUT, DELETE

Postman → to send requests and test

User Management REST API (Flask)
A simple REST API built with Python + Flask that manages user data in memory.
This project demonstrates core API fundamentals: REST concepts

HTTP methods (GET, POST, PUT, DELETE)
Basic API design with Flask
Testing APIs using Postman
🧰 Tech Stack
Python
Flask
Postman (for testing)
📚 Key Concepts Covered REST: Representational State Transfer – designing APIs using resources and standard HTTP methods. 
HTTP Methods: 
GET → read data 
POST → create data 
PUT → update data 
DELETE → remove data 
Flask: @app.route() → defines routes/endpoints 
request.get_json() → read JSON 
jsonify() → return JSON responses In-memory storage: Using a Python dictionary instead of a real database (for learning purposes).
