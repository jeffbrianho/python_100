age = int(input('What is your current age? '))
print(f'You are {age} years old')
# ten_year = 10
# twenty_year = 20
# thirty_year = 30
# forty_year = 40

# print(f'In {ten_year} years you will be {ten_year + age}')
# print(f'In {twenty_year} years you will be {twenty_year + age}')
# print(f'In {thirty_year} years you will be {thirty_year + age}')
# print(f'In {forty_year} years you will be {forty_year + age}')

years = range(10, 50, 10) # using a range with step value I used a manufactured list of [10, 20, 30, 40];
for year in years:
    print(f'In {year} years you will be {year + age}')

