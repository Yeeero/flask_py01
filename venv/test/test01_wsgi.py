# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : test01_wsgi.by
# @Software : PyCharm

'''
    利用python实现wsgi静态服务资源
'''

from wsgiref.simple_server import make_server

def app(env,make_response):
    # 处理核心数据
    for k,v in env.items():
        print(k, ':', v)
    # 处理相应头
    make_response('200 OK!',[('Content-Type', 'text/html;charset=utf-8')])
    return ['<h3>Hi, WSGI!</h3>'.encode('utf-8')]   # 相应数据
    

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8000
    # 生成web应用服务进程
    httpd = make_server(host, port, app)
    print('-----running http://{}:{}'.format(host, port))
    # 启动服务，开启监听服务器里链接
    httpd.serve_forever()
    print('------end----->', httpd)
