import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Use your MongoDB URI if needed
db = client['projectdb']  # Create or connect to the projectdb
projects_collection = db['projects']  # Create or connect to the 'projects' collection

# Menu bar for navigation
menu = st.sidebar.selectbox("Menu", ["Add Project", "View Projects"])

if menu == "Add Project":
    # Section for adding new projects
    st.title("Project Entry Form")

    # Form to input name and projects
    name = st.text_input("Enter your name")
    project = st.text_input("Enter your project")

    if st.button("Add Project"):
        if name and project:
            # Insert the data into MongoDB
            projects_collection.insert_one({"name": name, "project": project})
            st.success(f"Project '{project}' added for {name}!")
        else:
            st.error("Please enter both your name and project.")

elif menu == "View Projects":
    # Section for viewing projects
    st.title("Project List")

    # Form to search for projects by name
    name_to_search = st.text_input("Enter the name to view their projects")

    if st.button("Show Projects"):
        if name_to_search:
            # Find all projects done by the user
            user_projects = list(projects_collection.find({"name": name_to_search}))

            if user_projects:
                st.write(f"Projects done by {name_to_search}:")
                for i, proj in enumerate(user_projects, 1):
                    st.write(f"{i}. {proj['project']}")
            else:
                st.error(f"No projects found for {name_to_search}.")
        else:
            st.error("Please enter a name.")
