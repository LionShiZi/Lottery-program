import random as rd
import time
print('Made in LionShiZi')
hello = '''
1.输入1进行抽奖（每次1位同学），持续2秒（自动将已中奖的同学移除参与抽奖的同学列表）
2.输入2输出中奖者（将为1个列表呈现）
3.输入3查看当前参与抽奖的同学（将为1个列表呈现）
4.输入4退出该抽奖程序
注：此程序为死循环，每次抽奖完了无需按4，最后一次再按4.
'''

ChouJiang_List = ['熊二','熊大','毛毛','光头强']  #在此处填入参与抽奖之人员，格式：'xxx','xxx','xxx'
ZhongJiang_List = []
while True:
    ZhongJiang = ""
    ZhongJiangXB = 1000
    print(hello, end='\n')
    num1 = input("请输入1，2，3，4中的1个功能:")
    if num1 == '1':
        if ChouJiang_List == []:
            print('Error!此列表为空!')
        else :
            ZhongJiangXB = rd.randint(0, len(ChouJiang_List)-1)
            ZhongJiang = ChouJiang_List[ZhongJiangXB]
            ZhongJiang_List.append(ZhongJiang)
            time.sleep(2)
            print(ZhongJiang, end='\n') #起始与终止都包含
            ChouJiang_List.pop(ZhongJiangXB)
            print('指令执行完毕，中奖的幸运儿是不是你呢？')
            ZhongJiangXB = 1000
            ZhongJiang = ''
    elif num1 == '2':
        print(ZhongJiang_List)
        print('共有' + str(len(ZhongJiang_List)) + "人")
    elif num1 == '3':
        print(ChouJiang_List, end=' ')
        print('共有'+ str(len(ChouJiang_List)) +"人")
    elif num1 == '4':
        print('Bye~~~')
        break
    else:
        print('输入无效！请重新输入！')
