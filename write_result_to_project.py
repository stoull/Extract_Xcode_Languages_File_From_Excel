import sys
import os, fnmatch
from enum import Enum

class Language(Enum):
	chinese_simplifed = "zh-Hans"
	english_en = "en"
	italian_it = "it"
	polish_pl = "pl"
	putch_nl = "nl"
	german_de = "de"
	hungarian_hu = "hu-HU"
	portuguese_pt = "pt-PT"
	chinese_hongkong = "zh-Hant-HK"
	chinese_traditional = "zh-Hant"
	spanish_es = "es"
	korean_ko = "ko"
	french_fr = "fr"
	Base = "Base"

	# 根据语言类型获取对应的结果文件的文件名
	def getResultFileName(self, language):
		fileName="chinese_simplifed"
		localizedName="中文简体"
		if language == Language.chinese_simplifed:
			fileName="chinese_simplifed"
			localizedName="中文简体"
		elif language == Language.english_en:
			fileName="english_en"
			localizedName="英文"
		elif language == Language.italian_it:
			fileName="italian_it"
			localizedName="意大利文"
		elif language == Language.polish_pl:
			fileName="polish_pl"
			localizedName="波兰语"
		elif language == Language.putch_nl:
			fileName="putch_nl"
			localizedName="荷兰语"
		elif language == Language.german_de:
			fileName="german_de"
			localizedName="德语"
		elif language == Language.hungarian_hu:
			fileName="hungarian_hu"
			localizedName="匈牙利语"
		elif language == Language.portuguese_pt:
			fileName="portuguese_pt"
			localizedName="葡萄牙语"
		elif language == Language.chinese_hongkong:
			fileName="chinese_hongkong"
			localizedName="中文香港繁体"
		elif language == Language.chinese_traditional:
			fileName="chinese_traditional"
			localizedName="中文繁体"
		elif language == Language.spanish_es:
			fileName="spanish_es"
			localizedName="中文西班牙语"
		elif language == Language.korean_ko:
			fileName="korean_ko"
			localizedName="中文韩语"
		elif language == Language.french_fr:
			fileName="french_fr"
			localizedName="中文法语"
		elif language == Language.Base:
			fileName="base"
			localizedName="base"
		else:
			fileName="chinese_simplifed"
			localizedName="中文简体"
		return fileName

#如果没有传入正确的文件夹地址则返回false, 否则返回对应的目录参数 /Users/hut/Documents/shinePhone_ios_new_test
def getProjectDirPathFromSysArgv():
	inputArgv = sys.argv[1:]

	hasValidArgv=False
	validPath="."
	firstArgv = inputArgv[0]
	if os.path.isdir(firstArgv):
		hasValidArgv=True
		validPath = firstArgv
	else:
		try:
			projectPathIndex = inputArgv.index("-path")+1
			filePath = inputArgv[projectPathIndex]
			if os.path.isdir(filePath):
				hasValidArgv=True
				validPath = filePath
		except Exception as e:
			pass
	if hasValidArgv==True:
		return validPath
	else:
		return False

# 查找一个文件所在的目录位置
def findFilesDirectory(targetPath,targetFileName):
	isFound = False
	targetDir=""
	for root, dirs, files, in os.walk(targetPath):
		for name in files:
			if fnmatch.fnmatch(name, targetFileName):
				# print(f"Main Project Dir {root}/{name}")
				isFound = True
				targetDir = root
			if isFound==True:
				break
		if isFound==True:
			break
	if isFound == True:
		return targetDir
	else:
		return False

# 查找一个目录所在的目录位置
def findDirsDirectory(targetPath,targetDirName):
	isFound = False
	targetDir=""
	for root, dirs, files, in os.walk(targetPath):
		for name in dirs:
			if fnmatch.fnmatch(name, targetDirName):
				# print(f"Main Project Dir {root}/{name}")
				isFound = True
				targetDir = root
			if isFound==True:
				break
		if isFound==True:
			break
	if isFound == True:
		return targetDir
	else:
		return False

def writeResultFileTo(projectPath):
	errorMessages=[]
	exceptionFilePath = f"./wirte_to_project_log.txt"
	open(exceptionFilePath, 'w').close()

	languageDir = findDirsDirectory(targetPath=projectPath, targetDirName="Base.lproj")
	allLanguageFilePaths = []
	if languageDir == False:
		message = f"在{projectPath}目录下搜索不到Xcode项目的语言文件！"
		print(message)
		errorMessages.append(message)
		# 存储错误信息
		with open(exceptionFilePath, mode='wt', encoding='utf-8') as the_file:
			the_file.write('\n'.join(errorMessages))
		exit(0)
	else:
		print(f"最终搜寻到的语言存储目录：{languageDir}")
		for file in os.listdir(languageDir):
			if file.endswith(".lproj"):
				lanFilePath = f"{languageDir}/{file}/Localizable.strings"
				if os.path.isfile(lanFilePath):
					allLanguageFilePaths.append(lanFilePath)

	for lanPath in allLanguageFilePaths:
		# /nl.lproj/Localizable.strings
		lanDirName = os.path.basename(os.path.dirname(lanPath))
		lanDirName = lanDirName.replace(".lproj", "")
		try:
			xLanguage = Language(lanDirName)
			resultLanFileName = xLanguage.getResultFileName(language=xLanguage)
			resultLanFilePath = f"./Result/{resultLanFileName}.strings"
		except Exception as e:
			message = f"未能找到{lanDirName}对应的结果文件！"
			print(message)
			errorMessages.append(message)
			continue

		if os.path.isfile(resultLanFilePath):
			#清空之前的翻译文件信息
			open(lanPath, 'w').close()
			#写入新的文件信息
			with open(resultLanFilePath, mode='r', encoding='utf-8') as result_file:
				with open(lanPath, mode='a', encoding='utf-8') as project_file:
					for newline in result_file:
						project_file.write(newline)
			message = f"写入{resultLanFilePath}到{lanPath}成功！"
			errorMessages.append(message)
		else:
			message = f"{lanDirName}写入错误！对应的结果文件：{resultLanFilePath} 不存在或错误！"
			print(message)
			errorMessages.append(message)
	# 存储错误信息
	with open(exceptionFilePath, mode='wt', encoding='utf-8') as the_file:
		the_file.write('\n'.join(errorMessages))
		

if __name__ == '__main__':
	projectPath = getProjectDirPathFromSysArgv()
	if projectPath == False:
		print(f"请指定工程目录参数！")
		exit(2)
	else:
		print(f"获取到合法的目录参数: {projectPath}")

	mainProjectDir = findFilesDirectory(targetPath=projectPath, targetFileName="AppDelegate.*")

	if mainProjectDir != False:
		projectPath = mainProjectDir

	print(f"最终搜寻的目录：{projectPath}")

	writeResultFileTo(projectPath=projectPath)

	




