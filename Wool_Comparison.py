from selenium import webdriver
import csv
import pandas as pd

class Wool():
    def page_load(self):
        #fetching page deatils
        path=r"C:\Users\iTTaste\Desktop\old one\PycharmProjects\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.implicitly_wait(10)
        self.url="https://www.wollplatz.de/"
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.find_element_by_id('AcceptReload').click()

    def create_csv_file(self):
        #created CSV file with desired header
      rowHeaders = ["Brand", "Name", "Price", "Needle Size", "Composition"]
      self.file_csv = open('Wool_output.csv', 'w', newline='', encoding='utf-8')
      self.mycsv = csv.DictWriter(self.file_csv, fieldnames=rowHeaders)
      self.mycsv.writeheader()

    def data_scrap(self,brand,name):
        #fetch all products elements
        try:
         self.page = page = 'https://www.wollplatz.de/wolle/' + brand + '/' + name
         self.driver.get(page)
         self.driver.maximize_window()
         print(name)
         price = self.driver.find_element_by_class_name("product-price").text
         print("price:" + price)

         needle_size = self.driver.find_element_by_xpath("//div[@id='pdetailTableSpecs']/table/tbody/tr[5]/td[2]").text
         print("needle_size:" +needle_size )
         composition = self.driver.find_element_by_xpath("//div[@id='pdetailTableSpecs']/table/tbody/tr[4]/td[2]").text

         print("composition:" + composition)
        except:
            print("Not available")
            price="Not available"
            needle_size="Not available"
            composition="Not available"
        self.mycsv.writerow(
            {"Brand":brand,"Name":name,"Price":price,"Needle Size":needle_size,"Composition":composition})

    def tearDown(self):

    # driver.quit function is used to close chromedriver
      self.driver.quit()
    #close Csv file which I generated above
      self.file_csv.close()


Wool = Wool()
Wool.page_load()
Wool.create_csv_file()
company = {"dmc": "dmc-natura-xl",
                "drops": ["drops-baby-merino-mix", "drops-safron"],
                "hahn": "hahn-alpacca-speciale",
                "stylecraft": "stylecraft-special-double-knit"}
for keys, values in company.items():
    if (isinstance(values, list)):
        for value in values:
            Wool.data_scrap(keys,value)
    else:

        Wool.data_scrap(keys,values)


Wool.tearDown()

#read csv and display it into browser as html table
a=pd.read_csv("Woll_output.csv",encoding='UTF-8')

a.to_html("output1.html")

#print table on console
print(a.to_html)






