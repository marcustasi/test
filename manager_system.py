"""
需求:
1.存放資料的位置:(member.data)
載入文件數據
修改數據後保存
2.儲存資料的形式:列表
3.系統應包含功能:
新增
刪除
修改
查詢
顯示全部
保存
退出
"""

class managersystem(object):
    def __init__(self):
        #儲存資料用的列表
        self.member_list = []
    """
    管理系統框架
    step 1
    定義系統入口函示
        載入資料
        顯示功能列表
        用戶輸入功能序號
        依照序號執行不同功能
    """        
    def run(self):
        self.load_member() #載入資料

        while True:
            self.show_menu() #顯示功能列表
            menu_num = int(input('請輸入功能序號:')) 
            #依照序號執行不同功能
            if menu_num == 1:#新增
                self.add_member()
            elif menu_num == 2:#刪除
                self.del_member()
            elif menu_num == 3:#修改
                self.modify_member()
            elif menu_num == 4:#查詢
                self.search_member()
            elif menu_num == 5:#顯示所有
                self.show_member()
            elif menu_num == 6:#保存
                self.save_member()
            elif menu_num == 7:#退出系統即是終止此循環
                break 
            else:
                print("請重新選擇功能")
#系統功能函示
#顯示功能菜單
@staticmethod
def show_menu():
    print("請選擇下列功能:")
    print('1.新增會員')
    print('刪除會員')
    print('修改會員')
    print('查詢會員')
    print('顯示所有會員')
    print('保存會員資料')
    print('退出系統')
#新增
def add_member(self):
    print('新增會員')
#刪除
def del_member(self):
    print('刪除會員')
#修改
def modify_member(self):
    print('修改會員')
#查詢
def search_member(self):
    print('查詢會員')
#顯示所有
def show_member(self):
    print('顯示所有會員')
#保存
def save_member(self):
    print('保存會員')
#載入
def load_member(self):
    print('載入會員')