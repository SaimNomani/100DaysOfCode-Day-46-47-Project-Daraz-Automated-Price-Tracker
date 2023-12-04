from selenium import webdriver
from selenium.webdriver.common.by import By
from data import my_email, my_passowrd, recievers_email
from smtplib import SMTP

# making the browser to remain open
# configuring driver options
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# creating a chrome driver to drive through website
driver=webdriver.Chrome(chrome_options)

# website to drive through
page_url="https://www.daraz.pk/products/like-new-phones-used-apple-iphone-x-silver-256-gb-pta-approved-i435087172-s2088535157.html?spm=a2a0e.searchlist.sku.1.5f0ca1ad4mYwlc&search=1"
driver.get(page_url)


price=driver.find_element(By.XPATH, value='//*[@id="module_product_price_1"]/div/div/span')
product_title=driver.find_element(By.XPATH, value='//*[@id="module_product_title_1"]/div/div/span')
buy_link=driver.find_element(By.XPATH, value='//*[@id="module_add_to_cart"]/div/button[1]/span/span')

print(product_title.text)


price_text=float(price.text.split(" ")[1].replace(',',''))
print(price_text)
print(type(price_text))

message=f"{product_title.text} is now Rs.{price_text}\nBuy now: {page_url}"

target_price=110000.00

if price_text<=target_price:
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_passowrd)
        connection.sendmail(from_addr=my_email, to_addrs=recievers_email, msg=f"subject:price alert\n\n{message}")

# to close the tab as program end
# driver.close()

# to close the entire browser as progrm end
driver.quit()