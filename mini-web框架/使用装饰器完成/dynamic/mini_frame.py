import re
URL_FUNC_DICT = dict()
func_list = list()
def route(url):
    def set_func(func):
        #URL_FUNC_DICT["/index.py"] =index
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func
@route("/index.py")
def index():
    with open(r"D:/demo/index.html") as f:
        content = f.read()
    my_stock_info = "哈哈哈哈"
    content = re.sub(r"\{%content%\}",my_stock_info,content)
    return content
@route("/login.py")
def login():
    return "这是login"

'''
URL_FUNC_DICT = {
    "/index.py": index,
    "/login.py": login
}
'''
def application(env, start_response):
    start_response('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
    file_name = env["PATH_INFO"]
    '''if file_name == "/index.py":
        return index()
    elif file_name =="/login.py":
        return  login()
    else:
        return "hellow word,我"
    '''
    try:

        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "请求错误 ： %s"%str(ret)
