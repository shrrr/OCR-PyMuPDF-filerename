# OCR-PyMuPDF-filerename
* PDF2PNG.py：完成PDF到PNG的转换，利用PyMuPDF库实现
* OCR.py：利用百度OCR-api实现PNG图片的文字识别，转为export.txt文件并保存
* FileRename.py：利用正则匹配，提取txt文件中的关键信息，并利用其重命名原PDF文件

```
运行：
   1、先运行PDF2PNG，将文件夹中的PDF转化为同文件夹中的PNG文件
   2、再将所有PNG放在原文件夹内新建的picture文件夹中，而后运行OCR，识别图片
   3、识别结果将保存在原文件夹的export.txt中
   4、接下来，运行FileRename，读取txt文件，正则匹配，提取关键信息，完成文件更名
   
注意：
   1、在原PDF文件夹中运行，以保证PDF2PNG和OCR文件中路径正确
   2、OCR中需要修改填入baidu OCR-api的用户名和key
   3、在运行FileRename中的正则匹配时，注意名字匹配的汉字长度设置、OCR-api识别后在txt中莫名的换行导致的语言等级匹配问题等
   4、注意可能会出现的更名后文件名字相同导致的rename失败问题
```
