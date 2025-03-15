import pandas as pd

data = {
    'title': ['Intel Core i5', 'AMD Ryzen 5', 'Intel Core i7', 'AMD Ryzen 7', 'Intel Core i9'],
    'url': ['https://www.intel.com/content/www/us/en/products/sku/123456/intel-core-i5-11600k.html', 
            'https://www.dns-shop.ru/product/d4bde9994d11ed20/processor-amd-ryzen-5-7500f-oem/', 
            'https://www.intel.com/content/www/us/en/products/sku/123456/intel-core-i7-11700k.html', 
            'https://www.dns-shop.ru/product/4eae94861ec4ed20/processor-amd-ryzen-7-3700x-oem/', 
            'https://www.intel.com/content/www/us/en/products/sku/123456/intel-core-i9-11900k.html'],
    'xpath': ['/html/body/div[1]/div[2]/div[3]/span', '/html/body/div[1]/div[2]/div[3]/span', '/html/body/div[1]/div[2]/div[3]/span', '/html/body/div[1]/div[2]/div[3]/span', '/html/body/div[1]/div[2]/div[3]/span']
}

df = pd.DataFrame(data)

df.to_excel('example.xlsx', index=False)
#этот код реализован для демострации примерного excel файла по ТЗ