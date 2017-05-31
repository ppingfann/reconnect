# 校园网自动重连脚本
1. 使用python语言编写
2. 用了pip来安装requests库
3. 使用firefox的httpfox插件来抓取数据包
4. 使用pyinstaller生成exe可执行文件
5. 程序运行时会自动提交表单到目标url，且每隔10s会自动检测是否掉线，若掉线则会自动再次提交表单到目标url。
