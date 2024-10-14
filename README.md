# Project manager using Python and MongoDB
This is a Project Tracker web application built using Streamlit and MongoDB. The application allows users to keep track of their projects by adding details and viewing a list of all completed projects.
The data is stored in a MongoDB database, making it easy to manage and retrieve project information.

# Technologies Used
Streamlit: A simple framework for building web applications in Python.

MongoDB: A NoSQL database used to store project details.

Pymongo: A Python library to interact with MongoDB.

Python: The programming language used to implement the project.

# Installation
1. Clone the repository:
git clone https://github.com/your-username/project-tracker.git

Navigate to the project directory : 

cd project-tracker

2. Install the required dependencies:

pip install streamlit pymongo

Ensure MongoDB is running on your local machine, or connect to MongoDB Atlas if you are using a cloud database.

3. Run the Streamlit app:

streamlit run project_tracker.py
Open your browser and navigate to:

http://localhost:8501
# Usage
----------------------------------------
# 1. Adding Projects
Go to the "Add Projects" section via the sidebar menu.

Fill in the following details:

Project Name: Name of the project.
Project Description: A brief description of the project.
Status: Status of the project (e.g., "Completed", "Ongoing").
Click Submit to add the project to the MongoDB database.

# 2. Viewing Projects

Go to the "View Projects" section via the sidebar menu.
The list of all the projects you have added will be displayed.
You can see the Project Name, Description, and Status of each project.
