from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)  # __name__ 为Flask应用对象名称（可以随意命名）


# 声明web服务的请求资源（指定资源访问的路由）@app.route('/path', method=['GET','POST','PUT','DELETE','PATCH'])
@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return '''
        <h3>用户登录月面</h3>
            <form action="/hello" method="post">
                <input name="name" placeholder="please input your name"></br> 
                <input name="pwd" placeholder="please input your password"></br> 
                <button>提交</button>
            </from>
        '''
    else:
        # 获取b表单参数
        name = request.form.get('name')
        password = request.form.get('pwd')

        if name.strip() == 'Alice' and password.strip() == '123':
            return '''
                <h2>登录成功</h2>
            '''
        else:
            return """
                <h2 style='color:orange'>登录失败</h2></br>
                <a href="/hello">重试</a>
            """


@app.route('/bank', methods=['GET', 'POST'])
def addBank():
    data = {'title': '绑定银行卡', 'error_message': '卡号和银行卡信息不能为空'}
    # 渲染模板并返回给客户端
    return render_template('index.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)
