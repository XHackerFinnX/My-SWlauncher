from win32com.client import Dispatch
from win_tkinter import win_tk_download_mods
import wget
import time
import zipfile
import shutil
import os
import winshell
import requests

#Создание ярлыка----------------------------------------
def tags_stonelauncher():
    if os.path.exists("./stonelauncher.exe"):
        if os.path.exists(r"C:\.stoneworld\stonelauncher.exe"):
            return False
        else:
            shutil.move("./stonelauncher.exe", r"C:\.stoneworld")
            desktop = winshell.desktop()
            path = os.path.join(desktop, "stonelauncher.lnk")
            target = r"C:\.stoneworld\stonelauncher.exe"
            wDir = r"C:\.stoneworld"
            icon = r"C:\.stoneworld\stonelauncher.exe"

            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = wDir
            shortcut.IconLocation = icon
            shortcut.save()
            return True
#-------------------------------------------------------
def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)
    return

def build(root, data):
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            createFolder(path)
            build(path, d[1])

def downolad_wget(url_file, name_file):
    wget.download(url=url_file, out=name_file)
    time.sleep(1)
    shutil.move(f"./{name_file}", r"C:\.stoneworld\SWMinecraft")
    return
    
def zip_unzip(url ,name_file):
    unzip = url
    file_zip = zipfile.ZipFile(f"C:\.stoneworld\SWMinecraft\{name_file}", 'r')
    for f in file_zip.namelist():
        full = os.path.join(unzip, f)
        d = os.path.dirname(full)
        if d:
            if not os.path.exists(d):
                os.makedirs(d)
        if os.path.basename(f):
            out = open(full, mode="wb")
            out.write(file_zip.read(f))
            out.close()
    file_zip.close()
    return

def download(version):
    
    if version == "Forge 1.7.10":
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\forge1.7.10.zip"):
            downolad_wget("https://stoneworldlauncher.netlify.app/forge_1_7_10.zip", "forge1.7.10.zip")
            zip_unzip(r"C:\.stoneworld\SWMinecraft","forge1.7.10.zip")

        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods"):
            path = r"C:\.stoneworld\SWMinecraft"
            minecraft_dir = "mods"
            fullpath = os.path.join(path, minecraft_dir)
            createFolder(fullpath)

            if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_1.zip"):
                downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_1.zip", "mods_tm_1.zip")
                zip_unzip(r"C:\.stoneworld\SWMinecraft\mods", "mods_tm_1.zip")
                
            if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_2.zip"):
                downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_2.zip", "mods_tm_2.zip")
                zip_unzip(r"C:\.stoneworld\SWMinecraft\mods", "mods_tm_2.zip")
                
            if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_3.zip"):
                downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_3.zip", "mods_tm_3.zip")
                zip_unzip(r"C:\.stoneworld\SWMinecraft\mods", "mods_tm_3.zip")
                
            if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_4.zip"):
                downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_4.zip", "mods_tm_4.zip")
                zip_unzip(r"C:\.stoneworld\SWMinecraft\mods", "mods_tm_4.zip")
                
            if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_5.zip"):
                downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_5.zip", "mods_tm_5.zip")
                zip_unzip(r"C:\.stoneworld\SWMinecraft\mods", "mods_tm_5.zip")
                
    if version == "Forge 1.12.2":
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\forge1.12.2.zip"):
            win_tk_download_mods()
            downolad_wget("https://stoneworldlauncher.netlify.app/forge_1_12_2lvj.zip", "forge1.12.2.zip")
            zip_unzip(r"C:\.stoneworld\SWMinecraft","forge1.12.2.zip")
            
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\forge1.12.2org.zip"):
            downolad_wget("https://stoneworldlauncher.netlify.app/forge_1_12_2org.zip", "forge1.12.2org.zip")
            zip_unzip(r"C:\.stoneworld\SWMinecraft\libraries","forge1.12.2org.zip")
            
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods"):
            path = r"C:\.stoneworld\SWMinecraft"
            minecraft_dir = "mods"
            fullpath = os.path.join(path, minecraft_dir)
            createFolder(fullpath)
            
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods\1.12.2"):
            path = r"C:\.stoneworld\SWMinecraft\mods"
            minecraft_dir = "1.12.2"
            fullpath = os.path.join(path, minecraft_dir)
            createFolder(fullpath)
            
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_12_1.zip"):
            downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_12_1.zip", "mods_tm_12_1.zip")
            zip_unzip(r"C:\.stoneworld\SWMinecraft\mods", "mods_tm_12_1.zip")
        
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_12_2.zip"):
            downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_12_2.zip", "mods_tm_12_2.zip")
            zip_unzip(r"C:\.stoneworld\SWMinecraft\mods\1.12.2", "mods_tm_12_2.zip")
            
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_12_3.zip"):
            downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_12_3.zip", "mods_tm_12_3.zip")
            zip_unzip(r"C:\.stoneworld\SWMinecraft\mods\1.12.2", "mods_tm_12_3.zip")
            
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_12_4.zip"):
            downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_12_4.zip", "mods_tm_12_4.zip")
            zip_unzip(r"C:\.stoneworld\SWMinecraft\mods\1.12.2", "mods_tm_12_4.zip")
            
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_12_5.zip"):
            downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_12_5.zip", "mods_tm_12_5.zip")
            zip_unzip(r"C:\.stoneworld\SWMinecraft\mods\1.12.2", "mods_tm_12_5.zip")
            
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_12_6.zip"):
            downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_12_6.zip", "mods_tm_12_6.zip")
            zip_unzip(r"C:\.stoneworld\SWMinecraft\mods\1.12.2", "mods_tm_12_6.zip")
            
        if not os.path.exists(r"C:\.stoneworld\SWMinecraft\mods_tm_12_7.zip"):
            downolad_wget("https://stoneworldlauncher.netlify.app/mods_tm_12_7.zip", "mods_tm_12_7.zip")
            zip_unzip(r"C:\.stoneworld\SWMinecraft\mods\1.12.2", "mods_tm_12_7.zip")
   
    return

def download_dir():
    path = r"C:\Users\.."
    projectname = ".stoneworld"

    fullPath = os.path.join(path, projectname)
    createFolder(fullPath)
    #-------------------------------------------
    path = r"C:\.stoneworld"
    minecraft_dir = "SWMinecraft"

    fullpath = os.path.join(path, minecraft_dir)
    createFolder(fullpath)
    #-------------------------------------------
    folders = \
        [['login', []],
        ['icon_s', []]]
    path = r"C:\.stoneworld"
    projectname = "datalogandver"
    fullPath = os.path.join(path, projectname)
    createFolder(fullPath)
    build(fullPath, folders)

    #-------------------------------------------
    link_fon = "https://stoneworldlauncher.netlify.app/fooonjpg.jpg"
    link_icon = "https://stoneworldlauncher.netlify.app/icon_stone.jpg"

    response_fon = requests.get(link_fon)
    response_icon = requests.get(link_icon)

    path = r"C:\.stoneworld"
    minecraft_dir = "pictures"

    fullpath = os.path.join(path, minecraft_dir)
    createFolder(fullpath)
    
    with open(file= r"C:\.stoneworld\datalogandver\login\version_data.txt", mode= "a+") as file_version:
        file_version.close()
    
    with open(file=r"C:\.stoneworld\datalogandver\login\login_data.txt", mode= "a+") as file_login:
        file_login.close()

    with open(file=r"C:\.stoneworld\pictures\fon.jpg", mode="wb") as file_fon:
        file_fon.write(response_fon.content)
        file_fon.close()

    with open(file=r"C:\.stoneworld\pictures\icon.jpg", mode="wb") as file_icon:
        file_icon.write(response_icon.content)
        file_icon.close()
        
    return

def download_resourcepacks(version):
    path = r"C:\.stoneworld\SWMinecraft"
    minecraft_dir = "resourcepacks"
    fullpath = os.path.join(path, minecraft_dir)
    createFolder(fullpath)
    
    #Текстур пак скачивается на ["1.9", "1.9.2", "1.10", "1.10.2", "1.11", "1.11.2", "1.12", "1.12.2"]
        
    #if self.version_id in ["1.9", "1.9.2", "1.10", "1.10.2", "1.11", "1.11.2", "1.12", "1.12.2"]:
    #    minecraft_directory_texture = r"C:\.stoneworld\SWMinecraft\resourcepacks\SWFaithful.zip"
    #    if not os.path.exists(minecraft_directory_texture):
    #        downolad_wget("https://stoneworldlauncher.netlify.app/SWFaithful.zip", "SWFaithful.zip")
    #        zip_unzip(r"C:\.stoneworld\SWMinecraft\resourcepacks", "SWFaithful.zip")
        
                        
    #Текстур пак скачивается на ["1.7.10"]
    
    #if self.version_id in ["Forge 1.7.10", "1.7.10"]:
    #    minecraft_directory_texture_1_7_10 = r"C:\.stoneworld\SWMinecraft\resourcepacks\SWtexture.zip"
    #    if not os.path.exists(minecraft_directory_texture_1_7_10): 
    #        downolad_wget("https://stoneworldlauncher.netlify.app/Real%20Nature%20Resource%20Pack.zip", "SWtexture.zip")
    #        zip_unzip(r"C:\.stoneworld\SWMinecraft\resourcepacks", "SWtexture.zip")
    #
    #if self.version_id in ["Forge 1.7.10"]:
    #    minecraft_directory_cloud = r"C:\.stoneworld\SWMinecraft\resourcepacks\SWcloud.zip"
    #    if not os.path.exists(minecraft_directory_cloud): 
    #        downolad_wget("https://stoneworldlauncher.netlify.app/Clouds-Pack.zip", "SWcloud.zip")
    #        zip_unzip(r"C:\.stoneworld\SWMinecraft\resourcepacks", "SWcloud.zip")
    return

def record_login_version(version_id, username):
    with open(file=r"C:\.stoneworld\datalogandver\login\version_data.txt", mode= "w") as file_version:
        file_version.write(version_id)
        file_version.close()
    with open(file=r"C:\.stoneworld\datalogandver\login\login_data.txt", mode= "w") as file_login:
        file_login.write(username)
        file_login.close()
        
    return
        
        
def download_java_8():
    if not os.path.exists(r"C:\Program Files\Java\jdk-1.8"):
        return True
    return False


def add_server_ip():
    if not os.path.exists(r"C:\.stoneworld\SWMinecraft\server_ip.zip"):
        downolad_wget("https://stoneworldlauncher.netlify.app/server_ip.zip", "server_ip.zip")
        zip_unzip(r"C:\.stoneworld\SWMinecraft", "server_ip.zip")
    
    return