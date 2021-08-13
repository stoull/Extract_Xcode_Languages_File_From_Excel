# 从excel文件中提取多语言的翻译文件


## 从excel文件中提取多语言的翻译（*.strings）文件

使用方法：

1. 将工程开发语言（Base或者其它需要翻译的完整文件）的.strings文件里的内容存储到当前目录下，文件写为：`Base.strings`。
2. 将其它部门翻译好全语言文档xlsx文件存于当下目录，文件名为`source_translate.xlsx`。
3. 检查`create_translate_file_from_xlsx.py`文件中的枚举`class Language(Enum)` 使其中的语言与xlsx中的列对应（即A为第1列, B=2,.....）
4. 运行`create_translate_file_from_xlsx.py`，在当前目录会得到`Result`目录，为翻译目标文件。
5. 可以试着运行命令

	>`$ python3 create_translate_file_from_xlsx.py`

观察一下具体的行为

### create_translate_file_from_xlsx.py
`create_translate_file_from_xlsx.py`脚本文件会根据当前目录下的`Base.lproj`文件中的键值对，在当当前目录下的`source_20210716_translate.xlsx`文件中查找对应的翻译内容，并生成对应语言的`.strings `文件，存放于当前目录下`Result`目录中。
> 查找方法为
> 用需要查找的key-value对，先匹配xlsx文件中苹果key值和key-value对中的key进行对比，如果没有再匹配 中文（校对）与key-value对中的value行,如果没有就表示未查找到。

对应的错误及未翻译内容记录于当前目录下 `log.txt`文件中

生成的语言有如下：
>
```
chinese_simplifed
english_en
italian_it
polish_pl
putch_nl
german_de
hungarian_hu
portuguese_pt
chinese_hongkong
chinese_traditional
spanish_es
korean_ko
french_fr
```

## 将多语言文件（*.strings）替换写入到工程的对应多语言文件中
使用方法：

1. 确定当前目录下的`Result`目录下的多语言文件是你最终确定的文件，因为它将会覆盖写入到你的工程中。
2. 确定你工程的目录，或者让目录尽量靠近工程中存储多语言文件的目录。不过不靠近也没有关系。
3. 确认完全无误后运行：`python write_result_to_project.py -path your_project_path`

### write_result_to_project.py
使用`write_result_to_project.py`脚本文件时，传入对应工程的文件路径，
如：`python write_result_to_project.py -path your_project_path` 或者
`python write_result_to_project.py your_project_path `

`write_result_to_project.py` 会先在你传入的 `your_project_path`下寻找`AppDelegate.*`文件，以确定项目的主项目目录（为`AppDelegate.*`文件所在的目录），然后主项目目录里查找`Base.lproj`文件目录，以确定本地化文件所在的位置。（以第一个搜寻到的`Base.lproj`文件目录）
如果在`your_project_path `中搜寻不到`AppDelegate.*`文件，即当`your_project_path`为主目录，以第一个搜寻到的`Base.lproj`文件目录为本地化文件所在的位置。

`write_result_to_project.py`脚本文件会根据当前目录下的`Result`文件中.strings文件替换写入到对应工程中的本地化文件（`*.strings`文件）

对应的错误及未翻译内容记录于当前目录下 `result_check_log.txt`文件中