# xx服务

## 启动说明
    1、进入虚拟环境：
    conda create -n py38 python=3.8
    conda activate py38

    2、安装依赖包
    pip install -r requirements.txt

    3、启动

    在config/model_config.py 设置端口号！

    gunicorn启动，service 文件夹下的 app_test.py 里的名为 my_test_app 的flask应用
    `-c 配置文件` 或者 `--config 配置文件`  配置文件是gunicorn_config_test.py
    建议gunicorn_config_test.py这样的命名，带上任务名方便查找进程：

            gunicorn -c ./config/gunicorn_config_test.py service.app_test:my_test_app

    查看gunicorn进程：
            pstree -ap|grep gunicorn   pstree -ap|grep gunicorn_config_test.py
            ps -ef|grep gunicorn   
            ps -ef|grep python

    同时log/gunicorn.pid会显示gunicorn进程号


## 接口返回说明

请求类型：post
端口号：  6666 （随便写的，仅用于本地测试）
功能：chatpdf
    

请求参数说明：

    token_id:
    content:
    num（选填）:

输入示例

    {
        "token_id":"test001",
        "query":"文章主题",
        "content":"2023年5月2饱和预警。\n\n"
    }

输出

    {
        "data": 
        {
            "result": "风范。"
        },
        "message": "success",
        "status": 200
    }
        


## 调用方式
    curl -H "Accept: application/json" -H "Content-type: application/json" -X POST  -d '{"token_id":"user1",content": "...","query","..."}' http://43.130.32.111:5089/chatpdf