# **[little-useful-script](https://github.com/qllokirin/little-useful-script)**

没什么用的脚本

### 1微信推送.py

[pushplus](https://www.pushplus.plus/)一个请求就能把消息推送到微信，非常好用

### 2邮箱检测.py

之前一直困扰于学校邮箱检有新邮件不推送，后来发现有授权码绑定到QQ邮箱app上但是偶尔也不会推送，用学校邮箱的app版也偶尔不推送，故写此脚本

### 3跑步打卡.py

大体逻辑是把体育app装进模拟器里，然后这个脚本可以帮你自动设置位置，实现自动打卡，不过目前发现最困难的一步是登陆，过于玄学，可能一次就登陆成功，也可能一直登陆不上，也就不详细展开了

### 4鼠标键盘组合指令.py

如`4commands.csv`那样写好指令即可按顺序执行

### 5tmux.sh

用tmux把终端划分为四个小窗，最有用的一集

tmux设置鼠标开启

```
echo "set-option -g mouse on" >> ~/.tmux.conf
tmux source-file ~/.tmux.conf
```
