
import os

def main():
    name=raw_input("Enter the file name \n")   
    cmd='~/git/python-youtube-download/ffmpeg -ac 2 -ab 192k -vn -i "' + name + '.mp4" "' + name +'.mp3"'    
    os.system(cmd);

        
if __name__ == "__main__":
    main()
    