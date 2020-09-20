from selenium import webdriver
from time import sleep
from os import system

class colors: 
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'
#selenium configs
print("Enter full path of chrome driver : ")
PATH = './chromedriver'
driver = webdriver.Chrome(PATH)

#go to homepage
driver.get("http://in.finance.yahoo.com")
driver.implicitly_wait(60)
# go to loginpage
print("Enter yahoo emailID and Password : ")
input_str = "sourabh.mandal1997@yahoo.com !19Mandal97!" #input()
yahooID, passWord = map(str, input_str.split())
login_button = driver.find_element_by_xpath('//*[@id="uh-signedin"]')
login_button.click()
# enter username
driver.implicitly_wait(60)
username = driver.find_element_by_xpath('//*[@id="login-username"]')
username.send_keys(yahooID)
next_button = driver.find_element_by_xpath('//*[@id="login-signin"]')
next_button.click()
# enter password
driver.implicitly_wait(60)
password = driver.find_element_by_xpath('//*[@id="login-passwd"]')
password.send_keys(passWord)
signin_button = driver.find_element_by_xpath('//*[@id="login-signin"]')
signin_button.click()
driver.implicitly_wait(60)


#go to my portfolio
portfolio_button = driver.find_element_by_xpath('//*[@id="Nav-0-DesktopNav"]/div/div[3]/div/nav/ul/li[1]/a')
portfolio_button.click()
driver.implicitly_wait(60)

#go to specific portfolio
port_tab = driver.find_element_by_xpath('//*[@id="Col1-0-Portfolios-Proxy"]/main/table/tbody/tr[3]/td[1]/div[2]/a')
port_tab.click()
driver.implicitly_wait(60)


# fetch data
try:
    while(True):
        sleep(0.1)
        table = driver.find_elements_by_tag_name('tr')
        data_list = []

        count = 1
        for i in range(1,len(table)):
            symbol = driver.find_element_by_xpath('.//*[@id="pf-detail-table"]/div[1]/table/tbody/tr[' + str(i) + ']/td[1]/a').text     #symbol
            last_price = driver.find_element_by_xpath('.//*[@id="pf-detail-table"]/div[1]/table/tbody/tr['+ str(i) + ']/td[2]/span').text    #last Price
            change = driver.find_element_by_xpath('.//*[@id="pf-detail-table"]/div[1]/table/tbody/tr['+ str(i) + ']/td[3]/span').text    #Change
            change_percent = driver.find_element_by_xpath('.//*[@id="pf-detail-table"]/div[1]/table/tbody/tr['+ str(i) + ']/td[4]/span').text    #change %
            currency = driver.find_element_by_xpath('.//*[@id="pf-detail-table"]/div[1]/table/tbody/tr['+ str(i) + ']/td[5]').text         #currency
            volume = driver.find_element_by_xpath('.//*[@id="pf-detail-table"]/div[1]/table/tbody/tr['+ str(i) + ']/td[7]/span').text     #volume
            shares = driver.find_element_by_xpath('.//*[@id="pf-detail-table"]/div[1]/table/tbody/tr['+ str(i) + ']/td[8]').text         #shares
            average_volume = driver.find_element_by_xpath('.//*[@id="pf-detail-table"]/div[1]/table/tbody/tr['+ str(i) + ']/td[9]').text          #average volume
            
            pol = " " + colors.bg.red + " LOSS " + colors.fg.yellow + '\033[0m' + " " if change[0]=='-' else " " + colors.bg.green + "PROFIT" + colors.fg.blue + '\033[0m' + " "
            data_element = {
                'symbol' : symbol,
                'last_price' : last_price,
                'change' : change,
                'change_percent' : change_percent,
                'currency' : currency,
                'volume' : volume,
                'shares' : shares,
                'average_volume' : average_volume,
                'Profit_Loss' : pol,
            }
            count+=1
            data_list.append(data_element)

        system('clear')
        print('{0:15s}{1:18s}{2:14s}{3:22s}{4:16s}{5:15s}{6:14s}{7:22s}{8:15}'.format('symbol','last_price','change','change_percent','currency','volume','shares','average_volume', 'Profit/Loss'))

        for i in range(0, len(data_list)):
            print('{0:15s}{1:18s}{2:14s}{3:22s}{4:16s}{5:15s}{6:14s}{7:22s}{8:15}'.format(data_list[i]['symbol'],data_list[i]['last_price'],data_list[i]['change'],data_list[i]['change_percent'],data_list[i]['currency'],data_list[i]['volume'],data_list[i]['shares'],data_list[i]['average_volume'],data_list[i]['Profit_Loss']))

except:
    driver.close()