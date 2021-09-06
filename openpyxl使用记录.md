## openpyxl使用记录



**openpyxl文档：**
[openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files](https://openpyxl.readthedocs.io/en/stable/)

**office xml 规范: **
[Office Open XML file formats](http://www.ecma-international.org/publications/standards/Ecma-376.htm)



### 使用记录：

`from openpyxl import load_workbook`

1. 打开一个xlsx文件
	> `wb = load_workbook('source.xlsx')`
	
	
2. 遍历xlsx文件中的sheet

	```
	for sheet in wb:
		stitle = sheet.title
		print(f"{stitle}")
	```
3. 遍历sheet中的行列

```
for row in asheet.iter_rows(min_row=1, max_row=3663, min_col=5, max_col=5, values_only=True):
		rowValue = row[0]
```

4. 大
5. 大
6. 在

## 自动化测试  selenium

https://selenium-python.readthedocs.io