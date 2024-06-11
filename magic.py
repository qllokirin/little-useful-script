import requests
import time
if_qiangke = True
if_dis_time = True
# 111111 a课程  222222 是b课程
# lessonAssocs = [111111,222222]
lessonAssocs = []
studentAssoc = 
courseSelectTurnAssoc = 
# 上面几个值直接填数字 下面填字符串
Authorization = ''
Cookie = ''

def cal_time():
    global start_time
    global end_time
    end_time = time.time()
    run_time = (end_time - start_time) * 1000 
    print(f"代码运行时间: {run_time:.2f} 毫秒")
    start_time = time.time()
start_time = time.time()
end_time = time.time()
header2 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'Authorization': Authorization,
    'Connection': 'keep-alive',
    'Cookie': Cookie,
    'Host': 'jwxt.nwpu.edu.cn',
    'Referer': 'https://jwxt.nwpu.edu.cn/course-selection/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

header4 = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
        "Authorization": Authorization,
        "Connection": "keep-alive",
        "Content-Length": "138",
        "Content-Type": "application/json",
        "Cookie": Cookie,
        "Host": "jwxt.nwpu.edu.cn",
        "Origin": "https://jwxt.nwpu.edu.cn",
        "Referer": "https://jwxt.nwpu.edu.cn/course-selection/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "contentType": "application/json",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

session = requests.session()
response = session.get(
    # TODO
    url="",
    headers=header2
)
print(response.status_code)
print(response.text)
cal_time()
print('初始化完成')
while if_qiangke:
    print('-----------')
    for lessonAssoc in lessonAssocs:
        request_payload = {
            "studentAssoc": studentAssoc,
            "courseSelectTurnAssoc": courseSelectTurnAssoc,
            "requestMiddleDtos": [
                {"lessonAssoc": lessonAssoc, "virtualCost": 0}
            ],
            "coursePackAssoc": None
        }
        response = session.post(
            url= "https://jwxt.nwpu.edu.cn/course-selection-api/api/v1/student/course-select/add-request",
            headers=header4,
            json=request_payload
        )
        print(response.status_code)
        print(response.text)
        if if_dis_time:
            cal_time()
    # break

