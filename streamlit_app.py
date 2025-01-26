import os
import praw
from dotenv import load_dotenv
import streamlit as st

st.title("Subreddit Image Finder")
st.write(
    "Enter the subreddit name and get it's most trending image."
)

CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["CLIENT_SECRET"]
REDDIT_USERNAME = st.secrets["REDDIT_USERNAME"]
REDDIT_PASSWORD = st.secrets["REDDIT_PASSWORD"]
USER_AGENT = st.secrets["USER_AGENT"]

# Use credentials
import praw
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD
)

# Function to find the first trending post with an image
def find_top_image(subreddit_name):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        
        # Fetch top posts, checking for valid image URLs
        for post in subreddit.hot(limit=50):  # Iterate through top 50 posts
            if post.url.endswith((".jpg", ".png", ".jpeg", ".gif")):
                return post.title, post.url

        return None, None  # If no images found

    except Exception as e:
        return None, f"Error: {e}"


# User input for subreddit
subreddit_name = st.text_input("Enter subreddit name:")

if st.button("Submit"):
    with st.spinner("Fetching trending image..."):
        title, image_url = find_top_image(subreddit_name)

        if image_url:
            st.image(image_url, caption=title)
        else:
            st.warning("No trending image found in this subreddit. Try another one.")