# paladinsLive

## Description:
Application to view Live Paladins Match Statistics on both teams.

## How to use:
Type in a player's username and make sure to hit enter for the program to check if the name is valid. Then press the
"Continue" button. For now, the friends list feature is not functioning but if the player is currently in a match then hit the "Live
Match" button for the program to attempt to view both teams player stats of the current match.

### Shortcuts:
Right now there are two keyboard shortcuts that can be used to make the navigation of the program more friendly. There is the "Esc" button that will go back instead
of manually hitting the back button. As well as the "R" button that will refresh the Live Match statistics. This is useful if the player is in
a new match or if there might be a bot in the match.

### KeyWord:
There is a stat in the live match called "df" which stands for "dominance factor". This is a value calculated by paladins by summing up this equation of every match: 2xkills - 3xdeaths + assists. If a players dominance factor is low or in the negatives it means they usually have a bad kda and do not perform well. If it is high, usually they are good.

## Developer ID and Authentication Key:
Hi-Rez allows us users to access their database by giving us a Developer ID's and a Authentication Keys, but with that we have limited requests we can make before we can no longer use the database for a certain time period.

In the API Document it states:
"Here are the default initial limitations for API Developers:

concurrent_sessions:  50 &nbsp
sessions_per_day: 500 &nbsp
session_time_limit:  15 minutes &nbsp
request_day_limit:  7500" &nbsp

Therefore if you use the app a lot, it is a good idea to get a personal dev_id and auth_key instead of using the one built in the app because if more people use it then the default Developer ID and Authentiaction Key will not work consistently throughout the day.

To get your own personal Dev ID and Auth Key, you can submit a request using this link:
https://fs12.formsite.com/HiRez/form48/secure_index.html
