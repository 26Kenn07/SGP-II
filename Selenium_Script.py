from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

User = input("Enter your id: ")
Password = input("Enter your password: ")
PATH = "/Users/kirtan/Downloads/chromedriver_mac_arm64/chromedriver"
service = Service(PATH)

driver = webdriver.Chrome(service=service)
driver.get("https://charusat.edu.in:912/eGovernance/")

wait = WebDriverWait(driver, 10)



search = wait.until(EC.presence_of_element_located((By.NAME, "txtUserName")))
search.send_keys(User)
search = wait.until(EC.presence_of_element_located((By.NAME, "txtPassword")))
search.send_keys(Password)
search.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

Name = wait.until(EC.presence_of_element_located((By.ID, "lnkUsername1")))
print(Name.text)

c = driver.find_element(by="id", value="grdGrossAtt_ctl01_lnkRequestViewTT")
actions = ActionChains(driver)
actions.click(c)
actions.perform()



d = driver.find_element(by="id", value="footAnnouncement")
actions = ActionChains(driver)
actions.click(d)
actions.perform()
Overall = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='lblHeadAnnouncement']")))
print(Overall.text)

print("-------------------------------------------------")

Course1 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='grdGrossAtt_ctl02_lblSubjct']")))
print("Course = ",Course1.text)

Class1 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='grdGrossAtt_ctl02_lblClass']")))
print("Class Type = ",Class1.text)

Total1 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[3]")))
print("Total = ",Total1.text)

Percentage1 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[4]")))
print("Percentage = ",Percentage1.text)


print("-------------------------------------------------")

Course2 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='grdGrossAtt_ctl03_lblSubjct']")))
print("Course = ",Course2.text)

Class2 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='grdGrossAtt_ctl03_lblClass']")))
print("Class Type = ",Class2.text)

Total2 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[3]")))
print("Total = ",Total2.text)

Percentage2 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[4]")))
print("Percentage = ",Percentage2.text)

print("-------------------------------------------------")

Course3 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='grdGrossAtt_ctl04_lblSubjct']")))
print("Course = ",Course3.text)

Class3 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='grdGrossAtt_ctl04_lblClass']")))
print("Class Type = ",Class3.text)

Total3 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[3]")))
print("Total = ",Total3.text)

Percentage3 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[4]")))
print("Percentage = ",Percentage3.text)

print("-------------------------------------------------")

Course4 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='grdGrossAtt_ctl05_lblSubjct']")))
print("Course = ",Course4.text)

Class4 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='grdGrossAtt_ctl05_lblClass']")))
print("Class Type = ",Class4.text)

Total4 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[5]/td[3]")))
print("Total = ",Total4.text)

Percentage4 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[5]/td[4]")))
print("Percentage = ",Percentage4.text)

print("-------------------------------------------------")

Course5 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='grdGrossAtt_ctl06_lblSubjct']")))
print("Course = ",Course5.text)

Class5 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='grdGrossAtt_ctl06_lblClass']")))
print("Class Type = ",Class5.text)

Total5 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[6]/td[3]")))
print("Total = ",Total5.text)

Percentage5 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[6]/td[4]")))
print("Percentage = ",Percentage5.text)

print("-------------------------------------------------")

Course6 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='gvGrossAttPop_ctl07_lblSubjct']")))
print("Course = ",Course6.text)

Class6 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='gvGrossAttPop_ctl07_lblClass']")))
print("Class Type = ",Class6.text)

Total6 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[7]/td[3]")))
print("Total = ",Total6.text)

Percentage6 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[7]/td[4]")))
print("Percentage = ",Percentage6.text)

print("-------------------------------------------------")

Course7 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='gvGrossAttPop_ctl08_lblSubjct']")))
print("Course = ",Course7.text)

Class7 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='gvGrossAttPop_ctl08_lblClass']")))
print("Class Type = ",Class7.text)

Total7 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[8]/td[3]")))
print("Total = ",Total7.text)

Percentage7 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[8]/td[4]")))
print("Percentage = ",Percentage7.text)

print("-------------------------------------------------")

Course8 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='gvGrossAttPop_ctl09_lblSubjct']")))
print("Course = ",Course8.text)

Class8 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='gvGrossAttPop_ctl09_lblClass']")))
print("Class Type = ",Class8.text)

Total8 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[9]/td[3]")))
print("Total = ",Total8.text)

Percentage8 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[9]/td[4]")))
print("Percentage = ",Percentage8.text)

print("-------------------------------------------------")

Course9 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='gvGrossAttPop_ctl10_lblSubjct']")))
print("Course = ",Course9.text)

Class9 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='gvGrossAttPop_ctl10_lblClass']")))
print("Class Type = ",Class9.text)

Total9 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[10]/td[3]")))
print("Total = ",Total9.text)

Percentage9 = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[10]/td[4]")))
print("Percentage = ",Percentage9.text)

print("-------------------------------------------------")


UserName = str(Name.text)

str_Course1 = str(Course1.text)
str_Class1 = str(Class1.text)
str_Total1 = str(Total1.text)

str_Course2 = str(Course2.text)
str_Class2 = str(Class2.text)
str_Total2 = str(Total2.text)

str_Course3 = str(Course3.text)
str_Class3 = str(Class3.text)
str_Total3 = str(Total3.text)

str_Course4 = str(Course4.text)
str_Class4 = str(Class4.text)
str_Total4 = str(Total4.text)

str_Course5 = str(Course5.text)
str_Class5 = str(Class5.text)
str_Total5 = str(Total5.text)

str_Course6 = str(Course6.text)
str_Class6 = str(Class6.text)
str_Total6 = str(Total6.text)

str_Course7 = str(Course7.text)
str_Class7 = str(Class7.text)
str_Total7 = str(Total7.text)

str_Course8 = str(Course8.text)
str_Class8 = str(Class8.text)
str_Total8 = str(Total8.text)

str_Course9 = str(Course9.text)
str_Class9 = str(Class9.text)
str_Total9 = str(Total9.text)

driver.quit()

client = MongoClient("mongodb+srv://Kirtan:Kirtan1234@attendance.reoe654.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('Students')
records = db.Student_Attendance

new_student ={
    "User Name": UserName,
    "Course1":str_Course1,
    "Type1":str_Class1,
    "Tota1":str_Total1,
    "Course2":str_Course2,
    "Type2":str_Class2,
    "Total2":str_Total2,
    "Course3":str_Course3,
    "Type3":str_Class3,
    "Total3":str_Total3,
    "Course4":str_Course4,
    "Type4":str_Class4,
    "Tota4":str_Total4,
    "Course5":str_Course5,
    "Type5":str_Class5,
    "Tota5":str_Total5,
    "Course6":str_Course6,
    "Type6":str_Class6,
    "Tota6":str_Total6,
    "Course7":str_Course7,
    "Type7":str_Class7,
    "Tota7":str_Total7,
    "Course8":str_Course8,
    "Type8":str_Class8,
    "Tota8":str_Total8,
    "Course9":str_Course9,
    "Type9":str_Class9,
    "Tota9":str_Total9

}

records.insert_one(new_student)
