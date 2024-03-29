# paladinsLive

## Description:
Application to view Live Paladins Match Statistics (meant for Siege and rank) on both teams.

## Demo:
Default screen when opening the app:

<img src="demo_img/MainScreen_default.png" alt="MainScreen_default" width="700"/>

Screen after entering players' IGN:

<img src="demo_img/MainScreen_player.png" alt="MainScreen_player" width="700"/>

LiveMatch statistic screen:

<img src="demo_img/LiveGame_stats.png" alt="LiveGame_stats" width="700"/>

LiveMatch prediction (for casual siege and rank only):

<img src="demo_img/LiveGame_prediction.png" alt="LiveGame_prediction" width="700"/>

## Developer ID and Authentication Key:
Hi-Rez allows us users to access their database by giving us a Developer ID's and a Authentication Keys, but with that we have limited requests we can make before we can no longer use the database for a certain time period.

In the API Document (https://docs.google.com/document/d/1OFS-3ocSx-1Rvg4afAnEHlT3917MAK_6eJTR6rzr-BM/edit#) it states:  
  
"Here are the default initial limitations for API Developers:

concurrent_sessions:  50  
sessions_per_day: 500  
session_time_limit:  15 minutes  
request_day_limit:  7500"  

Therefore if you use the app a lot, it is a good idea to get a personal dev_id and auth_key instead of using the one built in the app because if more people use it then the default Developer ID and Authentiaction Key will not work consistently throughout the day.

The app will automatically save your Dev ID and your Auth Key as default, so you only need to enter it once.

To get your own personal Dev ID and Auth Key, you can submit a request using this link:
https://fs12.formsite.com/HiRez/form48/secure_index.html

If you enter incorrect dev_id and auth_key then every player name will be invalid and the app won't be able to access Paladins Database. If you want to reset to the apps default dev_id and auth_key, there should be a reset button at the bottom of the main screen.

If the default id and auth key is not working and your personal one isn't working as well, then there could be maintenance on Hi-Rez's end.
http://status.hirezstudios.com/


## How to use:

### Live Match:
Type in a player's username and make sure to hit enter for the program to check if the name is valid (usernames are not case sensitive). Then press the
"Continue" button. If the player is currently in a match then hit the "Live
Match" button for the program to attempt to view both teams player stats of the current match.

### Shortcuts:
Right now there are two keyboard shortcuts that can be used to make the navigation of the program more friendly. There is the "Esc" button that will go back instead
of manually hitting the back button. As well as the "R" button that will refresh the Live Match statistics. This is useful if the player is in
a new match or to check if there might be a bot in the match.

### KeyWord:
There is a stat in the live match called "df" which stands for "dominance factor". This is a value calculated by paladins by summing up this equation of every match: 2xkills - 3xdeaths + assists. If a players dominance factor is low or in the negatives it means they usually have a bad kda and do not perform well. If it is high, usually they are good.

## Error:
If the app crashes (unlike "not responding"), then a txt file will be created on the users desktop with information on the error. Copy paste that error to the issues tab on my github so I can take a look and try to debug it.
