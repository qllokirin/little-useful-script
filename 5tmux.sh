#!/bin/bash
## tmux new -s <window-name> 创建一个会话
## -d是在后台创建（重要 没有这个参数会有bug）
tmux kill-session -t start
tmux new -d -s start

## 分割成四块
tmux split-window -h -t start
tmux split-window -v -t start.0
tmux split-window -v -t start.2

## 填入指令 0是左上 1是坐下 2是右上 3是右下
tmux send -t start.0 " " 
tmux send -t start.1 " " 
tmux send -t start.2 " " 
tmux send -t start.3 " " 
## 显示刚刚创建的会话
tmux a -t start