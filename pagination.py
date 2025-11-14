from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.cnarios.com/challenges/product-listing-pagination")
#wait until the product cards are loaded
# wait for 4 seconds
webdriver_wait = WebDriverWait(driver, 10)
webdriver_wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='MuiCardContent-root flex flex-col space-y-3 css-15q2cw4']")))

number_of_pages = len(driver.find_elements(By.CSS_SELECTOR,'nav ul li')) - 2
print("Number of pages:", number_of_pages)
products = []
for page in range(1, number_of_pages + 1):
    print('Navigating to page ', page)
    webdriver_wait = WebDriverWait(driver, 5)
    # store every ptoduct name,price and rating in list of dictionaries
    
    product_elements = driver.find_elements(By.XPATH, "//div[@class='MuiCardContent-root flex flex-col space-y-3 css-15q2cw4']")
    for product in product_elements:
        # name is /h6
        name = product.find_element(By.XPATH, "h6").text
        # price is next h6
        price = product.find_element(By.XPATH, "h6[2]").text
        remove_dollar = price.replace("$", "")
        price = float(remove_dollar)
        #raitng is aria-label in /span
        rating_string = product.find_element(By.XPATH, "span").get_attribute("aria-label") # eg 3 Stars
        rating = rating_string.split(" ")[0]  # get only the number part
        #print(name, price, int(rating))
        products.append({"name": name, "price": price, "rating": int(rating), "page": page})
        print(f"Product found: {name}, Price: {price}, Rating: {rating}, Page: {page}")
    if page != number_of_pages:
        # click on the page number
        buttons = driver.find_elements(By.CSS_SELECTOR, "button[class*='MuiButtonBase-root MuiButton-root MuiButton-outlined']")
        if not buttons:
            print("No pagination buttons found.")
            break
        for button in buttons:
            if button.text == 'Next':
                button.click()
                break

driver.close()
#print all products sorted by price ascending
products_sorted = sorted(products, key=lambda x: x['price'])
for product in products_sorted:
    print(f"Product: {product['name']}, Price: {product['price']}, Rating: {product['rating']}, Page: {product['page']}")

#also print on txt file
with open("Practice/products_pagination.txt", "w") as f:
    for product in products_sorted:
        f.write(f"Product: {product['name']}, Price: {product['price']}, Rating: {product['rating']}, Page: {product['page']}\n")

#put on ecxel file in Practice folder
import pandas as pd

df = pd.DataFrame(products_sorted)
df.to_excel("Practice/products_pagination.xlsx", index=False)
