import streamlit as st

# Custom imports 
from multiapp import MultiPage
#import the our pages
from apps import home, user_overview, user_engagement, user_experience, user_satisfaction, ml_model

# Create an instance of the app 
app = MultiPage()

# Add all your applications (pages) here
app.add_page("HOME", home.app)
app.add_page("USER OVERVIEW", user_overview.app)
app.add_page("USER ENGAGEMENT ANALYSIS", user_engagement.app)
app.add_page("USER EXPERIENCE ANALYSIS", user_experience.app)
app.add_page("USER SATISFACTION ANALYSIS", user_satisfaction.app)
app.add_page("MACHINE LEARNING MODEL", ml_model.app)

# The main app
app.run()