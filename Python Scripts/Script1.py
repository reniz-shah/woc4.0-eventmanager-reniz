# Web Automation to create new page in FaceBook
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

def getDetails(txt):
    print("Enter your "+txt+" : ")
    string = str(input())
    return string


driver.get('https://www.facebook.com/signup')
time.sleep(2)
# Name
driver.find_element_by_name('firstname').send_keys(getDetails('First Name'))
driver.find_element_by_name('lastname').send_keys(getDetails('Last Name'))
# Mobile or E-mail
moe = getDetails('Mobile or E-mail')
if '@' in moe:
    driver.find_element_by_name('reg_email__').send_keys(moe)
    driver.find_element_by_name('reg_email_confirmation__').send_keys(moe)
else:
    driver.find_element_by_name('reg_email__').send_keys(moe)
# Password
driver.find_element_by_name('reg_passwd__').send_keys(getDetails('Password'))
# Birth Date 
dob = str(getDetails('Date of Birth (DD-Mon-YYYY) Format')).split('-')
driver.find_element_by_name('birthday_day').send_keys(dob[0])
driver.find_element_by_name('birthday_month').send_keys(dob[1])
driver.find_element_by_name('birthday_year').send_keys(dob[2])
# Gender
gender_choice = getDetails("1. Male \n2. Female \n3. Other \nSelect your Choice : ")
if gender_choice == '1':
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input').click()
elif gender_choice == '2':
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input').click()
elif gender_choice == '3':
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[3]/input').click()
else:
    print('Invalid Choice')
# Submit
driver.find_element_by_name('websubmit').click()
