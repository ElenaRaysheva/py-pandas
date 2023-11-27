import pandas as pd

data = pd.read_html('https://www.x-rates.com/table/?from=USD&amount=1')

print(data)

# Output:
# [               US Dollar    1.00 USD  inv. 1.00 USD
# 0                   Euro    0.914483       1.093514
# 1          British Pound    0.792840       1.261289
# 2           Indian Rupee   83.362328       0.011996
# ...
# 51     Venezuelan Bolivar  3.544945e+06       0.000000]
