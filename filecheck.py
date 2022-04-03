#!/usr/bin/env python
import os
import zipfile
import subprocess
import time
from bs4 import BeautifulSoup
import csv
import glob
import re
import gc

# if you are not install "BeautifulSoup", do command "pip install beautifulsoup4".

def get_html_filename():
    zip_files = glob.glob("./HTML/*")
    for file in zip_files:
        with zipfile.ZipFile(file) as zfile:
            zfile.extractall('./HTML/')
    return zip_files

def get_pdf_filename():
    pdf_files = glob.glob("./PDF/*")
    return pdf_files

def get_name(zip_files):
    file_names = []
    for zip in zip_files:
        html_folder = zip.replace('.zip','')
        html = html_folder + '/index.html'
        # html = glob.glob(zip_path)
        source = BeautifulSoup(open(html), 'html.parser')

        # source.string.replace_with('Navigable String')
        # source_content = source.string.extract()
        # print(source_content)
        # str_source = str(source.string)
        # print(str_source)
        
        elem1 = source.html.title
        # str(elem1)
        elem1_content = str(elem1.string)
        # print(elem1_content)

        # print(elem1)
        # elem1str = elem1.renderContents()
        # print(elem1str)
        # elem1str = elem1str.__str__()
        # print(elem1str)
        elem2 = source.html.p
        elem2str = str(elem2.string)

        # find_all: 戻り値はList
        # titles = source.find('title').unwrap()
        # id = source.find(class_='id').unwrap()

        # タグを外したHTMLを出力
        # print(elem3.get_text())

            # ここでエラー
            # idy.removeprefix(Tstr)
            # idy.sub('\d+', '', Tstr)
            # idy.remove(Tstr,'')
            # idy.replace('</p>', '')
        name =  elem1_content + elem2str
        print(name)
        file_names.append(name)

    return file_names

def change_filename(file_names, change_names):
    # judge = 'zip' in file_names
    i = 0
    print('file_name: {}'.format(file_names))
    print('change_name: {}'.format(change_names))
    for cname in file_names:
        judge = 'pdf' in cname
        if judge == True:
            print('pdfname: {}'.format(change_names[i]))
        else:
            change_names[i] = change_names[i] + '.zip'
            print('zipname: {}'.format(change_names[i]))

        changename = change_names[i]
        print('c_name: {}'.format(cname))
        os.rename(cname,changename)
        i = i + 1
    del file_names
    del change_names
    gc.collect()

    return 0

def display_pdf(pdf_files):
    acr_path = 'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'
    for idx,file in enumerate(pdf_files):
        pdf_pro = subprocess.Popen([acr_path,pdf_files], shell=False)
        time.sleep(2)
        pdf_pro.kill()
        time.sleep(1)

    return 0

if __name__ == '__main__':
    # Zipファイル名を取得
    zip_files = get_html_filename()
    print(zip_files)

    # pdfファイル名を取得
    pdf_files = get_pdf_filename()

    # 変更するファイル名を取得
    file_names = get_name(zip_files)
    print(file_names)
    pdf_names = file_names
    print('pdf_name: {}'.format(pdf_names))
    zip_names = file_names

    # ファイル名を変更
    change_filename(zip_files, zip_names)
    
    print('pdf_name: {}'.format(pdf_names))
    change_filename(pdf_files, pdf_names)

    # PDFを表示
    display_pdf(pdf_files)