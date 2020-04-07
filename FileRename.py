# 正则匹配，从txt中提取得到需要的新旧文件路径，使用os.rename()完成文件重命名
import re
import os
path=r"C:\Users\76778\Desktop\040720595651\export.txt"
txt=open(path,"rb")
strs=txt.read()
strs=strs.decode("ANSI")
# print(strs.decode("ANSI"))

# strs ='识别图片：	040720595651_1.png文本内容：明装有电子科技大学信息与通信工程学院黄子轩,学号2016020906成绩单号191251002006630该生于2019年6月参加全国大学英语六级考试,准考证号510024191210927,考试成绩为456分。特此证明电子科技大学教务处2020-3-22专用章impus: No, 4, Section 2, North Jianshe Road, 610054 I Qingshuihe Campus: No 2006, Xiyuan Ave, West Hi-Techne,6117311 Chengdu Sichuan, PR chinaTe&FaN:+86-28-61830026++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++识别图片：	040720595651_10.png文本内容：证兹有电子科技大学信息与通信工程学院李磊,学号20160200910022,身份证号51068319980912031X。该生于2017年6月参加全国大学英语六级考试,准考证号51002417122223考试成绩为538分。特此证明。料电子科技大学教务处2020322候No, 4, Section 2. North Jianshe Road, 610054I Qingshuihe Campus No. 2006, Xiyuan Ave West Hi-Techchuan, P.R. China'
pattern = '信息与通信工程学院[\u4E00-\u9FA5].{1,6},'
pattern_num = re.compile(pattern)
search_num = pattern_num.findall(strs)
name = [search_num[j][9:-1] for j in range(len(search_num))]
print(name)
print(len(name))

pattern1 ='_.{0,3}.png'
pattern_num1 = re.compile(pattern1)
search_num1 = pattern_num1.findall(strs)
filename = [search_num1[j][1:-4] for j in range(len(search_num1))]
print(filename)
print(len(filename))

pattern2='大学英语[\u4E00-\u9FA5]级'
pattern_num2 = re.compile(pattern2)
search_num2 = pattern_num2.findall(strs)
level = [search_num2[j][4:-1] for j in range(len(search_num2))]
print(level)
print(len(level))
flag=0
for i in filename:
    oldname="040720595651_"+i+".pdf"
    newname=name[flag]+"+"+level[flag]+"级"+".pdf"
    os.rename(oldname,newname)
    flag=flag+1
