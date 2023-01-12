import requests
import re
import os
import json

MCVsMFs = "http://launchermeta.mojang.com/mc/game/version_manifest.json"

def main():

    global MCVsMFs

    print("Excuting , Waiting...")
    if os.path.exists("latest.json") == False:
        fx = open("latest.json" , "x")
        fx.close()

    UrlDetail = requests.get(url=MCVsMFs)
    UClean = json.loads(UrlDetail.text)
    ReadU1 = UClean["latest"]
    ReadU2 = ReadU1["release"]
    ReadUV1 = UClean["versions"]

    LocalDetail = open("latest.json" , "r")

    try:
        LClean = json.loads(LocalDetail.read())
        ReadL1 = LClean["latest"]
        ReadL2 = ReadL1["release"]
        if ReadU2 != ReadL2:
            LocalDetail.close()
            wilf = open("latest.json" , "w")
            wilf.write(str(UClean))
            wilf.close()
    except:
        LocalDetail.close()
        wilf = open("latest.json" , "w")
        wilf.write(str(UrlDetail.text))
        wilf.close()
    
    print("OK!Please Input the Version NUM")
    userIc = input(">")
    print("Finding...")
    occGroup = []
    idtime = -1
    for x in ReadUV1:
        idtime += 1
        Read1 = x["id"]
        Read2 = x["type"]
        findstr = re.findall(userIc , Read1)
        if len(findstr) == 0:
            pass
        else:
            occGroup.append("id=" + Read1 + " , type=" + Read2 + " , Num=" + str(idtime))
    for x in occGroup:
        print(x)
    print("Which One?(Num)")
    userIc = input(">")
    print("OK,Wait...")
    ReadD1 = ReadUV1[int(userIc)]
    Readjson = ReadD1["url"]

    VjsonD = requests.get(url=Readjson)
    LoadVJD = json.loads(VjsonD.text)
    LoadDl1 = LoadVJD["downloads"]
    LoadDl2 = LoadDl1["server"]
    LoadDl3 = LoadDl2["url"]
    LoadDl4 = LoadVJD["id"]
    mdcmd = r"{0}"
    a2cmd = r"aria2c -d {0}  -o server.jar {1}"
    os.mkdir(mdcmd.format(LoadDl4))
    os.system(a2cmd.format(LoadDl4 , LoadDl3))

    

if __name__ == "__main__":
    main()