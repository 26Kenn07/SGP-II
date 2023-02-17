from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = "/Users/kirtan/Downloads/chromedriver_mac_arm64/chromedriver"
service = Service(PATH)

driver = webdriver.Chrome(service=service)
driver.get("https://charusat.edu.in:912/eGovernance/")

wait = WebDriverWait(driver, 10)

search = wait.until(EC.presence_of_element_located((By.NAME, "txtUserName")))
search.send_keys("21CE070")
search = wait.until(EC.presence_of_element_located((By.NAME, "txtPassword")))
search.send_keys("260703")
search.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

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
driver.quit()
