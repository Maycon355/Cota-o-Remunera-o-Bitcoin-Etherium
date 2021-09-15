import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import os
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument("--headless")

url = "https://whattomine.com/coins?aq_380=0&aq_fury=0&aq_470=0&aq_480=3&aq_570=0&aq_580=1&a_580=true&aq_vega56=0&aq_vega64=0&aq_5600xt=0&aq_5700=0&aq_5700xt=0&aq_vii=0&aq_67xt=0&aq_68=0&aq_68xt=0&aq_1050Ti=0&aq_10606=1&a_10606=true&aq_1070=0&aq_1070Ti=0&aq_1080=0&aq_1080Ti=0&aq_1660=0&aq_1660Ti=0&aq_166s=0&aq_2060=0&aq_2070=0&aq_2080=0&aq_2080Ti=0&aq_3060=0&aq_3060Ti=0&aq_3070=0&aq_3080=0&aq_3090=0&eth=true&factor%5Beth_hr%5D=53.00&factor%5Beth_p%5D=220.00&e4g=true&factor%5Be4g_hr%5D=53.00&factor%5Be4g_p%5D=220.00&zh=true&factor%5Bzh_hr%5D=53.50&factor%5Bzh_p%5D=200.00&cnh=true&factor%5Bcnh_hr%5D=1550.00&factor%5Bcnh_p%5D=185.00&cng=true&factor%5Bcng_hr%5D=1560.00&factor%5Bcng_p%5D=210.00&cnr=true&factor%5Bcnr_hr%5D=1220.00&factor%5Bcnr_p%5D=210.00&cnf=true&factor%5Bcnf_hr%5D=2650.00&factor%5Bcnf_p%5D=185.00&eqa=true&factor%5Beqa_hr%5D=230.00&factor%5Beqa_p%5D=200.00&cc=true&factor%5Bcc_hr%5D=6.00&factor%5Bcc_p%5D=210.00&cr29=true&factor%5Bcr29_hr%5D=6.20&factor%5Bcr29_p%5D=210.00&ct31=true&factor%5Bct31_hr%5D=0.60&factor%5Bct31_p%5D=110.00&ct32=true&factor%5Bct32_hr%5D=0.31&factor%5Bct32_p%5D=200.00&eqb=true&factor%5Beqb_hr%5D=26.20&factor%5Beqb_p%5D=220.00&rmx=true&factor%5Brmx_hr%5D=820.00&factor%5Brmx_p%5D=170.00&ns=true&factor%5Bns_hr%5D=1500.00&factor%5Bns_p%5D=240.00&al=true&factor%5Bal_hr%5D=101.00&factor%5Bal_p%5D=210.00&ops=true&factor%5Bops_hr%5D=9.70&factor%5Bops_p%5D=200.00&eqz=true&factor%5Beqz_hr%5D=32.50&factor%5Beqz_p%5D=210.00&zlh=true&factor%5Bzlh_hr%5D=29.50&factor%5Bzlh_p%5D=200.00&kpw=true&factor%5Bkpw_hr%5D=22.00&factor%5Bkpw_p%5D=260.00&ppw=true&factor%5Bppw_hr%5D=18.40&factor%5Bppw_p%5D=230.00&x25x=true&factor%5Bx25x_hr%5D=3.23&factor%5Bx25x_p%5D=170.00&mtp=true&factor%5Bmtp_hr%5D=1.90&factor%5Bmtp_p%5D=210.00&vh=true&factor%5Bvh_hr%5D=0.78&factor%5Bvh_p%5D=190.00&factor%5Bcost%5D=&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=&commit=Calcular"
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

sleep(1)
bitcoin = driver.find_element_by_xpath('/html/body/nav/div[1]/span[1]/span[1]/a').text
cotacao = driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[1]/td[8]/strong').text
eth = driver.find_element_by_xpath('/html/body/nav/div[1]/span[1]/span[3]').text


print('\nREMUNERAÇÃO HOJE: ', cotacao,'\n\nVALOR ETHERIUM AGORA: ',eth,'\nBITCOIN AGORA: ',bitcoin)
sleep(15)

driver.quit()

