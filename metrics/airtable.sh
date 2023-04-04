curl -X POST "https://api.airtable.com/v0/meta/bases/{baseId}/tables" \
-H "Authorization: Bearer YOUR_TOKEN" \
-H "Content-Type: application/json" \
--data '{
    "description": "Metrics from Orbit.love",
    "fields": [
      {
        "description": "Name of the apartment",
        "name": "Name",
        "type": "singleLineText"
      },
      {
        "name": "Address",
        "type": "singleLineText"
      },
      {
        "name": "Visited",
        "options": {
          "color": "greenBright",
          "icon": "check"
        },
        "type": "checkbox"
      }
    ],
    "name": "Apartments"
  }'