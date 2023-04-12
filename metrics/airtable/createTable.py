import requests
import json

# Replace "YOUR_API_KEY" with your actual Airtable API key
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Replace "YOUR_BASE_ID" with the ID of the base where you want to create a new table
url = "https://api.airtable.com/v0/meta/bases/{YOUR_BASE_ID}/tables"

# Set up the payload for the new table
data = {
    "description": "Metrics from Orbit.love",
    "name": "Metrics",
    "fields": [
        {
            "description": "Start date of the metrics period",
            "name": "start_date",
            "type": "date",
            "options": {
                "dateFormat": {
                    "name": "iso"
                }
            }
        },
        {
            "description": "End date of the metrics period",
            "name": "end_date",
            "type": "date",
            "options": {
                "dateFormat": {
                    "name": "iso"
                }
            }        
        },
        {
            "description": "Active members in the community",
            "name": "members_active",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members in the community",
            "name": "members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Returning members in the community",
            "name": "members_returning",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "GitHub stars",
            "name": "github_stars",
            "type": "number",
            "options": {
                "precision": 0
            }
        },
        {
            "description": "Members stared us",
            "name": "github_stars_members",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members stared us",
            "name": "github_stars_members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "PR opened",
            "name": "pr_opened",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Members opened PR",
            "name": "pr_opened_members",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members opened PR",
            "name": "pr_opened_members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Issues opened",
            "name": "issues_opened",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Members opened issues",
            "name": "issues_opened_members",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members opened issues",
            "name": "issues_opened_members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Issue comments",
            "name": "issue_comment",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Members commented issues",
            "name": "issue_comment_members",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members commented issues",
            "name": "issue_comment_members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Discussion topics on GitHub",
            "name": "discussion_created",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Members created discussion topics on GitHub",
            "name": "discussion_created_members",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members created discussion topics on GitHub",
            "name": "discussion_created_members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Discussion response on GitHub",
            "name": "discussion_response",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Members replied discussion on GitHub",
            "name": "discussion_response_members",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members replied discussion on GitHub",
            "name": "discussion_response_members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Twitter followers",
            "name": "twitter_follower",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Twitter tweets",
            "name": "twitter_tweet",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Comments on LinkedIn",
            "name": "linkedin_comment",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Members commented us on LinkedIn",
            "name": "linkedin_comment_members",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members commented us on LinkedIn",
            "name": "linkedin_comment_members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members joined Discord",
            "name": "discord_joined",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Messages in Discord",
            "name": "discord_message",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Members sent Discord messages",
            "name": "discord_message_members",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members sent Discord messages",
            "name": "discord_message_members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members joined Slack",
            "name": "slack_joined",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Messages in Slack",
            "name": "slack_message",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Members sent Slack messages",
            "name": "slack_message_members",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members sent Slack messages",
            "name": "slack_message_members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Topics created on Discourse",
            "name": "discourse_topic",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Members created topics on Discourse",
            "name": "discourse_topic_members",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members created topics on Discourse",
            "name": "discourse_topic_members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Replies posted on Discourse",
            "name": "discourse_post",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "Members posted replies on Discourse",
            "name": "discourse_post_members",
            "type": "number",
            "options": {
                "precision": 0
            }        
        },
        {
            "description": "New members posted replies on Discourse",
            "name": "discourse_post_members_new",
            "type": "number",
            "options": {
                "precision": 0
            }        
        }
    ]
}

# Make a POST request to create the new table
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response to confirm that the table was created
print(response.json())
