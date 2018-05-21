import  time,os,sys

#获取到当前时间
def getTime():
    return (time.strftime('%Y''_''%m''_''%d''_''%H''_''%M''_''%S',time.localtime(time.time())))


#截图
def shotPic(driver):
    path1 = os.path.dirname(os.getcwd()) + '/' + 'errorPIC'
    isexists = os.path.exists(path1)
    if isexists is False:
        print('文件夹不存在,正在新增')
        os.makedirs(path1)
    path = os.path.dirname(os.getcwd()) + '/' + 'errorPIC' + '/' + getTime()
    driver.save_screenshot(path + '.png')
