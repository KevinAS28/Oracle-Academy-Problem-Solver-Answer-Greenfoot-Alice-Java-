import subprocess
import re
import os
from bs4 import BeautifulSoup

def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def setClipboardData(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()
    os.system('notify-send -u critical done')

soal = getClipboardData()
splitter = b"""\n\n\t\t\t\t\t\n\t\t"""
soal = soal.split(splitter)



# pattern = r"( \t\t\t\n\t\t)*[0-9]{1,2}\.\ \t(.*)( \tMark for Review )"
pattern = r"""([0-9]{1,2}\.)(\s)*(.*)(\w*)"""
from_oracle = []
for i in soal:
    i = re.sub(r'[\s]*mark for review[\s]*', '', str(re.search(pattern.encode("utf-8"), i).groups()[2].decode("utf-8").lower()))
    
    from_oracle.append(i)
    #print(i)

all_ans = []
soal_real = ""
jwb_real = []
soal_before = False
options = 0
all_soal = [] # prevent the same question in database

source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
# print(from_oracle)
# print("EXTACTED: ")
# for ext in from_oracle:
#     print("|"+ext+"|")
# exit()
for root, dirs, files in os.walk(source):
   for file in files:
       if file.endswith(".html") and ("@" not in file):
            file = os.path.join(os.getcwd(), root, file)
# if True:
#     if True:
#         if True:            
#             file = ('/media/data/programming/python_saya/oracle_scrapping/source/2017/12/kunci-jawaban-all-quiz-oracle-academy_26.html')
            with open(file, "r") as file_read:
                content = file_read.read()
                content_parsed = BeautifulSoup(content, 'html.parser').get_text(separator='\t\t\t')
                content_lower = content_parsed.lower()
                no_ext = 0
                for ext in from_oracle:
                    no_ext+=1
                            
                    if (ext in content_lower):                            
                        content = re.split(r'\t\t\t', content_parsed.replace(chr(160), ''))
                        content_index = 0
                        soal_found = False
                        for i in content:
                            if (re.search(r'^[\n|\s]*$', i)):
                                continue
                            content_index+=1                     
                            if (ext in i.lower()):
                                if (ext in all_soal):
                                    # print("LANJUT\n\n\n\n\n\n")
                                    continue                                                   
                                print(f'Question {i} in {file}')
                                # print('Founded question:', i)
                                if ("Mark for Review" in i):
                                    i = re.search(r'(.*)([\s]*Mark for Review[\s]*)', i).groups()[0]
                                
                                first_answer = re.search(r'(.*\?)\ (.*)', i)
                                if (first_answer):
                                    fw = first_answer.groups()
                                    i = fw[0]
                                    content[content_index-1] = i
                                    content.insert(content_index, fw[1])   
                                all_ans.append(jwb_real)
                                jwb_real = [no_ext-1]
                                soal_found = True
                                all_soal.append(ext)
                                continue

                            if (soal_found):
                                soal0 = "Mark for Review" in i
                                soal1 = re.search(r'([\s]*)(\d{1,2})\.(\s*)(.*)', i)                                                        
                                if (soal0 or soal1):
                                    soal_found = False
                                    options = 0
                                    continue
                                else:
                                    print("OPTION: ", i)
                                    if ("(*)" in i):
                                        jwb_real.append(i)
                                    options+=1
                        # print(content)
                        # exit()
                                                            


all_ans.append(jwb_real)
del all_ans[0]
#all_ans = sort(all_ans)
print(all_ans)
setClipboardData(str(all_ans).encode('utf-8'))