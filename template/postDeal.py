# import os
import zip

inputName = 'template'
filename = inputName + '.docx'
unzipdir = f'./{inputName}/'
outputname = f'{inputName}-posted.docx'

zip.unzip(filename, unzipdir, True)

zip.zip(unzipdir, outputname, True)
# print(unzipdir)
