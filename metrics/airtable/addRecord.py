import requests, json, datetime
from datetime import date

# Replace "YOUR_API_KEY" with your actual Orbit API key
orbitHeaders = {
    "accept": "application/json",
    "authorization": "Bearer YOUR_API_KEY"
}

# Replace "YOUR_BASE_ID" with the ID of the base where you want to create a new table
airtableURL = "https://api.airtable.com/v0/YOUR_BASE_ID/Metrics"
# Replace "YOUR_API_KEY" with your actual Airtable API key
airtableHeaders = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Extract number of months data from Orbit
months = 51
i = 1
rows = []

t_day = date.today()
end_date = t_day - datetime.timedelta(days=(t_day.day))

while i <= months:
    start_date = end_date - datetime.timedelta(days=(end_date.day-1))

    # Get data from Orbit love. Replace YOUR_WORKSPACE with the name of workspace you created in Orbit.love
    orbitURL = "https://app.orbit.love/api/v1/YOUR_WORKSPACE/reports?start_date="+start_date.strftime('%Y-%m-%d')+"&end_date="+end_date.strftime('%Y-%m-%d')
    orbitData = json.loads(requests.get(orbitURL, headers=orbitHeaders).text)
    print(orbitData['data']['attributes']['timeframe']['start_date'],": retrieved.")

    rows.append(
        {
            "fields": {
                "start_date": orbitData['data']['attributes']['timeframe']['start_date'],
                "end_date": orbitData['data']['attributes']['timeframe']['end_date'],
                "members_active": orbitData['data']['attributes']['members']['active_count'],
                "members_new": orbitData['data']['attributes']['members']['new_count'],
                "members_returning": orbitData['data']['attributes']['members']['returning_count'],
                "github_stars": orbitData['data']['attributes']['activities']['star:created']['count'],
                "github_stars_members": orbitData['data']['attributes']['activities']['star:created']['members']['active_count'],
                "github_stars_members_new": orbitData['data']['attributes']['activities']['star:created']['members']['new_count'],
                "pr_opened": orbitData['data']['attributes']['activities']['pull_requests:opened']['count'],
                "pr_opened_members": orbitData['data']['attributes']['activities']['pull_requests:opened']['members']['active_count'],
                "pr_opened_members_new": orbitData['data']['attributes']['activities']['pull_requests:opened']['members']['new_count'],
                "issues_opened": orbitData['data']['attributes']['activities']['issues:opened']['count'],
                "issues_opened_members": orbitData['data']['attributes']['activities']['issues:opened']['members']['active_count'],
                "issues_opened_members_new": orbitData['data']['attributes']['activities']['issues:opened']['members']['new_count'],
                "issue_comment": orbitData['data']['attributes']['activities']['issue_comment:created']['count'],
                "issue_comment_members": orbitData['data']['attributes']['activities']['issue_comment:created']['members']['active_count'],
                "issue_comment_members_new": orbitData['data']['attributes']['activities']['issue_comment:created']['members']['new_count'],
                "discussion_created": orbitData['data']['attributes']['activities']['discussions:discussion_created']['count'],
                "discussion_created_members": orbitData['data']['attributes']['activities']['discussions:discussion_created']['members']['active_count'],
                "discussion_created_members_new": orbitData['data']['attributes']['activities']['discussions:discussion_created']['members']['new_count'],
                "discussion_response": orbitData['data']['attributes']['activities']['discussions:comment']['count']+orbitData['data']['attributes']['activities']['discussions:reply']['count'],
                "discussion_response_members": max(orbitData['data']['attributes']['activities']['discussions:comment']['members']['active_count'],orbitData['data']['attributes']['activities']['discussions:reply']['members']['active_count']),
                "discussion_response_members_new": max(orbitData['data']['attributes']['activities']['discussions:comment']['members']['new_count'],orbitData['data']['attributes']['activities']['discussions:reply']['members']['new_count']),
                "twitter_follower": orbitData['data']['attributes']['activities']['twitter:followed']['count'],
                "twitter_tweet": orbitData['data']['attributes']['activities']['tweet:sent']['count'],
                "linkedin_comment": orbitData['data']['attributes']['activities']['linkedin:comment']['count'],
                "linkedin_comment_members": orbitData['data']['attributes']['activities']['linkedin:comment']['members']['active_count'],
                "linkedin_comment_members_new": orbitData['data']['attributes']['activities']['linkedin:comment']['members']['new_count'],
                "discord_joined": orbitData['data']['attributes']['activities']['discord:server:joined']['count'],
                "discord_message": orbitData['data']['attributes']['activities']['discord:message:replied']['count']+orbitData['data']['attributes']['activities']['discord:message:sent']['count'],
                "discord_message_members": max(orbitData['data']['attributes']['activities']['discord:message:replied']['members']['active_count'],orbitData['data']['attributes']['activities']['discord:message:sent']['members']['active_count']),
                "discord_message_members_new": max(orbitData['data']['attributes']['activities']['discord:message:replied']['members']['new_count'],orbitData['data']['attributes']['activities']['discord:message:sent']['members']['new_count']),
                "slack_joined": orbitData['data']['attributes']['activities']['slack:channel:joined']['count'],
                "slack_message": orbitData['data']['attributes']['activities']['slack:message:sent']['count']+orbitData['data']['attributes']['activities']['slack:thread:replied']['count'],
                "slack_message_members": max(orbitData['data']['attributes']['activities']['slack:message:sent']['members']['active_count'],orbitData['data']['attributes']['activities']['slack:thread:replied']['members']['active_count']),
                "slack_message_members_new": max(orbitData['data']['attributes']['activities']['slack:message:sent']['members']['new_count'],orbitData['data']['attributes']['activities']['slack:thread:replied']['members']['new_count']),
                "discourse_topic": orbitData['data']['attributes']['activities']['discourse:topic:created']['count'],
                "discourse_topic_members": orbitData['data']['attributes']['activities']['discourse:topic:created']['members']['active_count'],
                "discourse_topic_members_new": orbitData['data']['attributes']['activities']['discourse:topic:created']['members']['new_count'],
                "discourse_post": orbitData['data']['attributes']['activities']['discourse:post:created']['count'],
                "discourse_post_members": orbitData['data']['attributes']['activities']['discourse:post:created']['members']['active_count'],
                "discourse_post_members_new": orbitData['data']['attributes']['activities']['discourse:post:created']['members']['new_count']
            }
        }
    )

    # Airtable only accepts 10 rows in each POST request
    if i % 10 == 0:
        # Make a POST request to create records
        response = requests.post(airtableURL, headers=airtableHeaders, data=json.dumps({"records":rows}))
        print(response.json())
        rows = []

    end_date = start_date - datetime.timedelta(days=1)
    i = i + 1

# Make a POST request to create records
response = requests.post(airtableURL, headers=airtableHeaders, data=json.dumps({"records":rows}))
print(response.json())
rows=[]
