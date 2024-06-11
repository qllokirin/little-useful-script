import requests
def plus_plus(title,msg):
    # TODO
    token=""
    response = requests.get(url=f"http://www.pushplus.plus/send?token={token}&title={title}&content={msg}&template=html")
    if response.status_code == 200:
        print("成功发送(或许)")
        print("消息流水号:",response.json()["data"])