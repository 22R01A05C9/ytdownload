from flask import Flask,render_template,request,url_for
import requests
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download', methods=["POST"])
def download():
    video=request.form['url']
    url="https://x2mate.com/api/ajaxSearch"
    data={"q": video,
    "vt": "home"}
    response=requests.post(url,data=data)
    a=response.text
    d=[]
    token=""
    timeexpires=""
    title=""
    vid=""
    c=a.replace('\n',"")
    e=c.replace('"',"")
    b=e.split(',')
    for i in b:
        d.append(i.split(':'))
    for j in d:
        if(j[0]=="token"):
            token=j[-1]
        elif(j[0]=="title"):
            title=j[-1]
        elif(j[0]=="timeExpires"):
            timeexpires=j[-1]
        elif(j[0]=="{vid"):
            vid=j[-1]
    if(token==""):
        return render_template('home.html',info="Video Not Found")
    url1="https://dt244.kokiuyar.xyz/api/json/convert"
    data1={"v_id": vid,
    "ftype": "mp4",
    "fquality": "720p",
    "fname":title,
    "token": token,
    "timeExpire": timeexpires,
    }
    header1={
    "Sec-Ch-Ua-Mobile":
    "?0",
    "Sec-Ch-Ua-Platform":
    "Windows",
    "Sec-Fetch-Dest":
    "empty",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Site":
    "cross-site",
    "Sec-Gpc":
    "1",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    response2=requests.post(url1,data=data1,headers=header1)
    data1=response2.text
    data=data1.replace('"',"")
    a=data.split(',')
    d=[]
    link1=""
    link2=""
    for i in a:
        d.append(i.split(':'))
    for j in d:
        if(j[0]=="result"):
            link2=j[-1]
    link1=link2.replace("}","")
    link="https:"+link1
    return render_template('home.html',title=title,link=link)

if __name__=='__main__':
    app.run()