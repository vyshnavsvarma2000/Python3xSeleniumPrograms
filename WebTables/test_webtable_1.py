from selenium import webdriver
from selenium.webdriver.common.by import By



def test_webtables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")

    #Row
    row_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
    row = len(row_elements)
    print(row)
    #Col
    col_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)

    for i in range(2, row+1):
        for j in range(1, col+1):
            dynamic_path = f"//table[@id='customers']/tbody/tr[{i}]/td[{j}]"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if "Helen Bennett" in data:
                company_path = f"{dynamic_path}/preceding-sibling::td"
                company_text = driver.find_element(By.XPATH, company_path).text
                print(f"Helen Bennet works in {company_text}")


    # Find Helen Bennett's country

    driver.get("https://awesomeqa.com/webtable1.html")
    # Get the table
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    row_table = table.find_elements(By.TAG_NAME, "tr")

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for e in cols:
            if "UAE" in e.text:
                print("Yes")





