# yt-deleted-playlist-remaker
Remakes (YOUTUBE) deleted Youtube playlists only using the HTML source file. Also usable if you have a bulk of YT URLs
Code is poorly written but it works to my knowledge.


No YouTUbe API or dependencies needed expect one extension, [Multiselect](https://chromewebstore.google.com/detail/multiselect-for-youtube/gpgbiinpmelaihndlegbgfkmnpofgfei).
# Pre

When YouTube deletes a playlist you made, they will send you an email saying that your playlist is terminated and will send you a link to appeal the decision, but like 9/10 times they will deny it anyways and now you lost your playlist.


However, when you appeal, they show you a [preview](https://imgur.com/a6oxXDr) of all the videos you had in the playlist, ALL OF IT. Those videos can be extracted from the HTML in the form of href's and then be added via an extension called [Multiselect For Youtube](https://chromewebstore.google.com/detail/multiselect-for-youtube/gpgbiinpmelaihndlegbgfkmnpofgfei)
There are ways to do it with the Youtube API but this way it is free and less complicated. 
.

# HOW TO USE
When on the [appeal page](https://imgur.com/a6oxXDr)  check if you have `&v=appeal` in the URL, if not, change the `v` value to `appeal`. Other way is to go the [studio](https://studio.youtube.com/channel/) and clicking on the warning, then changing the value in the URL from `&v=summary` to `&v=appeal`. 

Save the HTML by right-clicking and clicking on Save As... (or Ctrl - S) and save it to a folder or anything else doesnt really mattter. 

Now drag in yt_playlist_creator.py into the folder where the HTML is located and open the script. If you have other files in your folder you can skip over it by entering N.

When the right text or HTML file is found you can type Y and press Enter and the script will automatically extract the URLs from the file and put it in a text file (fin.txt) or automatically open it in on the webbrowser (recommended to close all other tabs)

When you have all the tabs loaded you can add them to a playlist via the extension. Recommended to start from the back to the front, so it is still in chronological order of date added.

# Important
YouTube has removed the ability to add videos from a generated playlist to another user made playlist, the ONLY way I found to still put them in a playlist is by using [Multiselect](https://chromewebstore.google.com/detail/multiselect-for-youtube/gpgbiinpmelaihndlegbgfkmnpofgfei) 

You can use Multiselect by clicking on the blue icon in the upper right when in YouTube, then clicking the double checkmark on the bottom, then clicking the 3 dots to Save To Playlist.

