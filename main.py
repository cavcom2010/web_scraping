from bs4 import BeautifulSoup

with open('index.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')


# print(soup.h1)
#
# print(soup.head)
# print(soup.p)


x = soup.find_all('h2')

print(x)

my_var = soup.title
print(str(my_var))

# if str(my_var).__contains__('website'):
#     print("yes")

if 'website' in str(my_var):
    print('yes')





