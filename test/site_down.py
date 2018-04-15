# urllib 的使用
#在python3.3后urllib2已经不能再用，只能用urllib.request来代替

from urllib import request
import http.cookiejar

#写入文件，方便查看
def write_txt(path, txt):
    f = open(path, 'w')
    f.write(str(txt))
    f.close()

url = 'http://www.baidu.com'
path = 'D:/Python/MySampleCrawler/test/'

#第一种方式
response = request.urlopen(url)
print(response.getcode())
cont = response.read()
write_txt(path + 'output_1', cont)

#第二种方式
req = request.Request(url)
req.data = None # 没有 add_data 这个函数了,可以使用 req.data = '' 添加，具体值参考http的get和post方法
req.add_header('user-agent', 'Mozilla/5.0')
response_2 = request.urlopen(req)
print(response_2.getcode())
cont_2 = response_2.read()
write_txt(path + 'output_2', cont_2)

#第三种方式
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response_3 = request.urlopen(url)
print(response_3.getcode())
cont_3 = response_3.read()
write_txt(path + 'output_31', cont_3)
write_txt(path + 'output_32', cj)

