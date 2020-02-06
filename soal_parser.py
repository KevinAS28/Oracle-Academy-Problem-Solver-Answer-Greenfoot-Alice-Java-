# soal = b"""1. 	All objects in Alice have three dimensional coordinates on which axes? 	Mark for Review 
# (1) Points
					
# 			(Choose all correct answers) 	
					
			
# 	x
	
			
# 	y
	
			
# 	z
	
			
# 	w
	
			
# 	All of the above
	
					
# 		2. 	Alice objects move relative to the orientation of the person viewing the animation. True or false? 	Mark for Review 
# (1) Points
					
			
# 	True
	
			
# 	False
	
					
# 		3. 	In Alice, what are the forms of a scenario? 	Mark for Review 
# (1) Points
					
# 			(Choose all correct answers) 	
					
			
# 	A section of code to write.
	
			
# 	A system to start.
	
			
# 	A person to help.
	
			
# 	A problem to solve.
	
			
# 	A task to perform.
	
					
# 		4. 	From your Alice lessons, which of the following are types of storyboards? 	Mark for Review 
# (1) Points
					
# 			(Choose all correct answers) 	
					
			
# 	Fictional
	
			
# 	Factual
	
			
# 	Actual
	
			
# 	Visual
	
			
# 	Textual
	
					
# 		5. 	In Alice, if a procedure is declared for a clownFish class, which classes can use the procedure? 	Mark for Review 
# (1) Points
					
			
# 	The pajamaFish class, clownFish class, and Swimmer class
	
			
# 	The clownFish class and Swimmer class
	
			
# 	Any class with "Fish" in the class name
	
			
# 	ClownFish class"""




import subprocess
import re
import os
from bs4 import BeautifulSoup

source = "source"

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

soal = getClipboardData()


#print(soal)
splitter = b"""\n\n\t\t\t\t\t\n\t\t"""
soal = soal.split(splitter)



# pattern = r"( \t\t\t\n\t\t)*[0-9]{1,2}\.\ \t(.*)( \tMark for Review )"
pattern = r"""([0-9]{1,2}\.)(\s)*(.*)(\w*)"""
from_oracle = []
for i in soal:
    i = str(re.search(pattern.encode("utf-8"), i).groups()[2].decode("utf-8").lower()).rstrip("""	 mark for review""")
    from_oracle.append(i)
    #print(i)


# setClipboardData(extracted.encode("utf-8"))

all_answer = []
all_ans = []
soal_real = ""
jwb_real = []
soal_before = False
options = 0
no = 0
all_soal = [] # prevent the same question in database
for root, dirs, files in os.walk(source):
    for file in files:
        if file.endswith(".html") and ("@" not in file):
            file = os.path.join(os.getcwd(), root, file)
            with open(file, "r") as file_read:
                content = file_read.read()
                content_lower = BeautifulSoup(content, 'html.parser').get_text().lower()
                for ext in from_oracle:
                    # print(content_lower)
                    if (ext in content_lower):
                        #print("Found question {} in {}".format(ext, file))
                        try:
                            html_soup = BeautifulSoup(content, 'html.parser')
                            content = html_soup.find_all('div', attrs={'itemprop': 'description'})[0]
                        except TypeError as error:
                            continue
                        except IndexError as error:
                            continue
                            # print("ERROR: ", str(error))
                            #print(file)
                        
                        #splitter = """        """
                        splitter = r'[\s]{3,}|\xa0{2,}'
                        
                        content = re.split(splitter, content.get_text())
                        soal_pattern = r"""([1-9]{1,2}\.[\ ])*(.*)"""
                        remove_pattern0 = """(\s*)Mark for Review"""
                        remove_pattern1 = """(\s*)(\(\d\))(\s*)Points"""
                        remove_pattern2 = """([\d]{1,2})\.(\s*)"""
                        for i in content:
                            i = re.sub(remove_pattern0, "", i)
                            i = re.sub(remove_pattern1, "", i)                            
                            regex_result = re.search(soal_pattern, i)
                            condition0 = ext in i.lower() #and (re.search('^')ext.split()[0] i.lower().split()[0])
                            if  ((condition0) or (regex_result and ( (re.split(splitter, i.lower())[0]==re.split(splitter, ext)[0]) and  (re.split(splitter, i.lower())[-1]==re.split(splitter, ext)[-1])))):
                                i = re.sub(r'[\xa0|\s|\n]*', '', re.sub(r'[\xa0|\s|\n]*', '', re.sub(remove_pattern2, "", i), count=1)[::-1], count=1)[::-1]
                                if (i in all_soal) or (len(i)<=5) or (re.match(r'^(\s|\n)*$', i)):
                                    pass
                                else:
                                    all_ans.append(jwb_real)
                                    soal_before = True                
                                    no+=1
                                    jwb_real = [no]
                                    options = 0                                

                                    all_soal.append(i)
                                    print("|"+i+"|", "and", "|"+ext+"|", end="\n\n\n")
                                
                            
                            if (("[Correct]" in i) or ("[Incorrect]" in i) or ("(Choose all correct answers)" in i) or (re.match(r'^(\s)*$', i))):
                                continue
                            print("OPTION:"+i)
                            if ("(*)" in i):
                                
                                # jwb_real.append(i.replace('\xa0', '').strip(' ').rstrip(' '))
                                jwb_real.append(options)
                            options+=1
                                                            
                        



                        

exit()

jawaban = "source/2017/12/kunci-jawaban-all-quiz-oracle-academy.html"


with open(jawaban, "r") as read:
    content = read.read()
    html_soup = BeautifulSoup(content, 'html.parser')
    content = html_soup.find_all('div', attrs={'itemprop': 'description'})[0]
    splitter = """        """
    
    content = content.get_text().split(splitter)
    
    soal_pattern = r"""[0-9]{1,2}\.(\s)*(.*)(\w*)"""
    soal = """15.     From your Alice lessons, the IF control structure can process one true and one false response. True or false?     Mark for Review <br/>(1) Points<br/>                   <br/>           <br/>    True (*)<br/>   <br/>           <br/>    False<br/>
<br/>
<br/>"""
    # print(content)
    # result = re.search(soal_pattern, soal).groups()
    
    all_ans = []
    soal_real = ""
    jwb_real = []
    soal_before = False
    options = 0
    no = 0
    for i in content:
        if (re.match(r'^(\s|\n)*$', i)):
            continue
        result = re.search(soal_pattern, i)
        if (result or ("Mark for Review" in i)):
            
            if (("Mark for Review" in i)):
                soal_real = i
            else:
                soal_real = result.groups()[1]
            if (soal_real==""):
                continue                        
                
            # if (soal_before):
            #     jwb_real
            if (len(jwb_real)==1):
                pass
            else:
                print("JWB: ", jwb_real, end="\n\n\n")
                all_ans.append(jwb_real)
                soal_before = True                
                no+=1
                jwb_real = [no]
                options = 0
                print(f"{no}. SOAL: ", soal_real)
                continue

        if (("[Correct]" in i) or ("[Incorrect]" in i) or ("(Choose all correct answers)" in i) or (re.match(r'^(\s)*$', i))):
            continue
        print("OPTION:"+i)
        if ("(*)" in i):
            
            # jwb_real.append(i.replace('\xa0', '').strip(' ').rstrip(' '))
            jwb_real.append(options)
        options+=1
all_ans.append(jwb_real)

# print("JWB: ", jwb_real, end="\n\n\n")

print(all_ans)
setClipboardData(str(all_ans).encode("utf-8"))
