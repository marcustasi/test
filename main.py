"""
需求:
1.存儲資料在文件中
2.系統功能需要包含新增、刪除、修改、查詢、顯示所有、保存與退出
角色:
1.會員-->數據資料
2.管理系統-->進行管理的機制
一般一個角色會是一個文件以方便維護
項目的主程序入口通常會被命名為main.py

程序文件如下:
主程序:main.py
會員資料:member.py
管理系統:managersystem.py
"""

from manager_system import *
if __name__ == '__main__':
    mm = managersystem()
    mm.run()

