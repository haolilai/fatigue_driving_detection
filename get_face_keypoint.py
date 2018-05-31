import urllib.request
import urllib.parse
import json
import  sys
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=T0TsNwRb4ur5MXKYuG0GGDPP&client_secret=GnFMGhBecEE0jtKdzE2d1PpRobYWWZGZ'

headers = {
  #  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Content-Type':'application/json; charset=UTF-8'
}

values = {
    'image': 'zh',
    'to': 'en',
    'query': '死肥猪',
    'transtype': 'translang',
    'simple_means_flag': '3'
}
data = urllib.parse.urlencode(values).encode('utf-8')
#创建一个request,放入我们的地址、数据、头
request = urllib.request.Request(url, None, headers)
#访问
ret=urllib.request.urlopen(request).read()
access_token=json.loads(ret)['access_token']
print(access_token)
#print(json.loads(ret))
#exit()
# encoding:utf-8
'''
人脸检测与属性分析
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
headers = {
  #  'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Content-Type':'application/json; charset=UTF-8'
}

def imgdata(file1path):
    import base64
    f=open(r'%s' % file1path,'rb')
    pic1=base64.b64encode(f.read())
    f.close()

    return str(pic1,'utf-8')
    #将图片信息格式化为可提交信息，这里需要注意str参数设置
    #params = {"images":str(pic1,'utf-8') + ',' + str(pic2,'utf-8')}
    #return params

par=imgdata("D:\image_0001.png")

values = {
    'image': par,
    'image_type': 'BASE64',
    'face_field': 'faceshape,facetype,landmark',
    'transtype': 'translang',
    'simple_means_flag': '3'
}

#params = "{\"image\":\"027d8308a2ec665acb1bdf63e513bcb9\",\"image_type\":\"FACE_TOKEN\",\"face_field\":\"faceshape,facetype\"}"
#access_token = '[调用鉴权接口获取的token]'
data = urllib.parse.urlencode(values).encode('utf-8')
request_url = request_url + "?access_token=" + access_token
request = urllib.request.Request(request_url, data, headers)
ret=urllib.request.urlopen(request).read()
#response = urllib.request.urlopen(request)
print(json.loads(ret))

