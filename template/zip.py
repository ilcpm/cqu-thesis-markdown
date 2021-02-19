# 解压压缩docx文件
import os
import sys
import zipfile
import shutil


def unzip(inputfile: str, unzipdir: str, overwrite: bool = False):
    # 如果存在与压缩包同名文件夹 提示信息并跳过
    if os.path.exists(unzipdir):
        if overwrite == True:
            shutil.rmtree(unzipdir)
        else:
            return False, 'DirExisted'
    file = zipfile.ZipFile(inputfile, 'r')
    # 创建文件夹，并解压
    os.mkdir(unzipdir)
    file.extractall(unzipdir)
    file.close()
    return True, unzipdir
    # print(f'{inputfile} unzip fail')


def zip(folder, outputfile: str, overwrite: bool = False):
    # 如果存在与压缩包同名文件 提示信息并跳过
    if os.path.exists(outputfile):
        if overwrite == True:
            os.remove(outputfile)
        else:
            return False, 'FileExisted'
    file = zipfile.ZipFile(outputfile, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_name, file_names in os.walk(folder):
        # 要是不replace，就从根目录开始复制
        file_path = dir_path.replace(folder, '')
        # 实现当前文件夹以及包含的所有文件
        # file_path = file_path and file_path + os.sep or ''
        for file_name in file_names:
            file.write(os.path.join(dir_path, file_name),
                       os.path.join(file_path, file_name))
    file.close()
    return True, outputfile


if __name__ == "__main__":
    if not True:
        if os.path.exists('./unzip/'):
            shutil.rmtree('./unzip/')
        filename = 'example.docx'
        outputpath = './unzip/'
        unzip(filename, outputpath)
    else:
        if os.path.exists('./zip.docx'):
            os.remove('./zip.docx')
        folder = './unzip/'
        outputfilename = 'zip.docx'
        zip(folder, outputfilename)
