import sys
import os
import time
import glob
import webbrowser

#   this thing is bad and very janky but it works. dont forget the Multiselect extension to add them to a playlist
#   because youtube removed the ability to add videos to a playlist if the playlist is Untitled List
#
#   Multiselect:
#   https://chromewebstore.google.com/detail/multiselect-for-youtube/gpgbiinpmelaihndlegbgfkmnpofgfei

 
def main():


    filem = "null"
    t=0
    cwd = sys.argv[0].replace("yt_playlist_creator.py", "")
    
    for filename in glob.glob(cwd+"/*", recursive=True):
        if "urls.txt" in filename.lower():
            continue
        elif "fin.txt" in filename.lower():
            continue
        elif ".py" in filename.lower():
            continue

        temp = input("Is this the correct file? : "+filename+" Y/N: ") 
        if "y" in temp.lower():
            filem = filename
            break
       
    if filem == "null":
        print("No text file or HTML file found, make sure it is in this folder.")
        input() 
        
    file = open(filem,"r", encoding='utf-8')
    urls = open(cwd+"/urls.txt","w")
    
    for line in file.readlines():
        if 'href="https://www.youtube.com/watch?' in line.lower():
            not1 = line.split("href=")
            not2 = not1[1].split(">")
            not3 = not2[0].replace('"', "")
            t += 1
            urls.write(not3+"\n")
        else:
            continue  
    urls.close()       
    file.close()
    print("=============================================")
    ghh = print("DONE "+ str(t)+" URLS found, Continuing.. ")
    time.sleep(2)
    main2()


def main2():

    cwd = sys.argv[0].replace("yt_playlist_creator.py", "")
    file = open(cwd+'/urls.txt',"r")
    urls = open(cwd+'/fin.txt', "w")
    
    i = 0
    v = 0
    t = 0
    ft = 0
    for line in file.readlines():
        t += 1
        ft = t
    file.close()
    print(t)
    
    file = open(cwd+'/urls.txt',"r")
    stringline = "https://www.youtube.com/watch_videos?video_ids="
    
    for line in file.readlines():
        line = line.replace("https://www.youtube.com/watch?v=", "")
        stringline = stringline + line + ","
        stringline= stringline.replace("\n", "")
        i += 1
        if (ft % 49) > t:
            
            if t == 1:
                urls.write(stringline)
                urls.write("\n")
                print(stringline)
                stringline = "https://www.youtube.com/watch_videos?video_ids="
                v += 1
        elif i > 49:
            urls.write(stringline)
            urls.write("\n")
            print(stringline)
            stringline = "https://www.youtube.com/watch_videos?video_ids="
            
            print(" ================= new line ================= ")
            i = 0
            v += 1
        t -= 1
        
    urls.close()
    urls = open(cwd+'/fin.txt', "r")
    input("DONE: "+ str(ft)+" URLS, "+str(v)+" Playlists, Press enter to automatically open the URLS or exit with Ctrl+C to open them manually, they are found in fin.txt")
    print(" ================================== ")
    for line in urls.readlines():
        time.sleep(1)
        webbrowser.open(line, new=1)
        
        

            
    file.close()
    urls.close()
    print("=============================================")

if __name__ == '__main__':
    main()
    
