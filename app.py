from flask import Flask,render_template,request,url_for,session
import requests
import json,websocket,time
app=Flask(__name__)
app.secret_key="link"
def getdatamp4(url):
    data={}
    data1={
    "q": url,
    "vt": "home"
    }
    headers1={
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"same-origin",
        "Sec-Gpc":"1",
        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
        "X-Requested-With":"XMLHttpRequest"
    }
    response1=requests.post(url="https://x2mate.com/api/ajaxSearch",data=data1,headers=headers1)
    op1=json.loads(response1.text)
    data['title']=str(op1['title'])
    data['mp4']={}
    for i in op1['links']['mp4']:
        try:
            data['mp4'][op1['links']['mp4'][i]['q']]=op1['links']['mp4'][i]['size']
        except:
            break
    return data

def getdatamp3(url):
    data={}
    data['status']=1
    data1={
        "q": url,
        "vt": "mp3"
    }
    headers1={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "X-Access-Token":"ZJtmlGRrkWxhY2bK2qeh122VlG2om6OakqmQodB3n9WnoJdfk5dsX5RhlpNkUIyPnI+iy2eXZ26Ra2liYpSf",
        "X-Auth-Token":"m6iW2sqX3V+c1JJkl5lrx2hnyJqSYmedyWqYk2vIlH2cf2uwi4LYo7V/hre/krFyh6vaqJSonMewYdhwm15qk5Y=",
        "X-Requested-Domain":"9xbuddy.in",
        "X-Requested-With":"xmlhttprequest"
    }
    response1=requests.post(url="https://x2mate.com/api/ajaxSearch",data=data1,headers=headers1)
    op1=json.loads(response1.text)
    try:
        data['title']=str(op1['title'])
    except KeyError:
        data['status']=0
        return data
    else:
        data['mp3']={}
        for i in range(1,7):
            try:
                data['mp3'][op1['links']['mp3'][str(i)]['q']]=op1['links']['mp3'][str(i)]['size']
            except:
                break
        return data

def getlinkmp4(url,type):
    data={}
    data1={
    "q": url,
    "vt": "home"
    }
    response1=requests.post(url="https://x2mate.com/api/ajaxSearch",data=data1)
    op1=json.loads(response1.text)
    data['vid']=str(op1['vid'])
    data['title']=str(op1['title'])
    data['token']=str(op1['token'])
    data['timeexpire']=str(op1['timeExpires'])
    data2={"v_id": data['vid'],
    "ftype": "mp4",
    "fquality": type,
    "fname":data['title'],
    "token": data['token'],
    "timeExpire": data['timeexpire'],
    "client":"x2mate.com"
    }
    headers2={
        "Sec-Ch-Ua-Mobile":"?0",
        "Sec-Ch-Ua-Platform":"Windows",
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"cross-site", 
        "Sec-Gpc":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "X-Requested-Key":"de0cfuirtgf67a"
    }
    response2=requests.post(data=data2,headers=headers2,url="https://backend.svcenter.xyz/api/convert-by-45fc4be8916916ba3b8d61dd6e0d6994")
    op2=json.loads(response2.text)
    cserver=op2['c_server']
    t1=cserver.split('/')
    sublink=t1[-1]
    data3={"v_id": data['vid'],
    "ftype": "mp4",
    "fquality": type,
    "fname":data['title'],
    "token": data['token'],
    "timeExpire": data['timeexpire'],
    }
    header3={
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform":"Windows",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"cross-site",
    "Sec-Gpc":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    response3=requests.post(url=f"{cserver}/api/json/convert",data=data3,headers=header3)
    op3=json.loads(response3.text)
    if op3['result']=='Converting':
        
        jobid=op3['jobId']
        url4=f"wss://{sublink}/sub/{jobid}?fname=x2mate.com"
        ws = websocket.WebSocket() 
        ws.connect(url4)
        while(True):
            message=ws.recv()
            op4=json.loads(message)
            if (op4['action']=='success'):
                link=op4['url']
                break
    else:
        link=op3['result']
    return link     
    
def getlinkmp3(url,type):
    data={}
    data1={
        "q": url,
        "vt": "mp3"
    }
    headers1={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "X-Access-Token":"ZJtmlGRrkWxhY2bK2qeh122VlG2om6OakqmQodB3n9WnoJdfk5dsX5RhlpNkUIyPnI+iy2eXZ26Ra2liYpSf",
        "X-Auth-Token":"m6iW2sqX3V+c1JJkl5lrx2hnyJqSYmedyWqYk2vIlH2cf2uwi4LYo7V/hre/krFyh6vaqJSonMewYdhwm15qk5Y=",
        "X-Requested-Domain":"9xbuddy.in",
        "X-Requested-With":"xmlhttprequest"
    }
    response1=requests.post(url="https://x2mate.com/api/ajaxSearch",data=data1,headers=headers1)
    op1=json.loads(response1.text)
    data['vid']=str(op1['vid'])
    data['title']=str(op1['title'])
    data['token']=str(op1['token'])
    data['timeexpire']=str(op1['timeExpires'])
    data2={
    "v_id": data['vid'],
    "ftype":"mp3",
    "fquality": type,
    "token": data['token'],
    "timeExpire": data['timeexpire'],
    "client": "x2mate.com"
    }
    headers2={
        "Sec-Ch-Ua-Mobile":"?0",
        "Sec-Ch-Ua-Platform":"Windows",
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"cross-site", 
        "Sec-Gpc":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "X-Requested-Key":"de0cfuirtgf67a"
    }
    response2=requests.post(url="https://backend.svcenter.xyz/api/convert-by-45fc4be8916916ba3b8d61dd6e0d6994",data=data2,headers=headers2)
    op2=json.loads(response2.text)
    link=op2['d_url']
    return link
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=["POST"])
def search():
    url=request.form['link']
    session['link']=url
    datamp3=getdatamp3(url)
    if (datamp3['status']==0):
        return render_template('home.html',info="Video Not Found")
    time.sleep(1)
    datamp4=getdatamp4(url)
    print(datamp4['title'])
    session['title']=datamp4['title']
    return render_template('home.html',title=datamp4['title'],mp3=datamp3['mp3'],mp4=datamp4['mp4'],link=url)
    
@app.route('/download',methods=['POST'])
def download():
    try:
        url=session['link']
    except KeyError:
        return render_template('home.html',info="Some Error Occured,Please Try Again.")
    else:
        session.pop('link',None)
        type1=request.form['opti']
        l=type1.split(',')
        if (l[0]=='mp3'):
            endlink=getlinkmp3(url,type=l[-1])
        elif (l[0]=='mp4'):
            endlink=getlinkmp4(url,type=l[-1])
        title=session['title']
        session.pop('title',None)
        return render_template('home.html',title=title,endlink=endlink)
if __name__=='__main__':
    app.run(debug=True,host='192.168.0.108')