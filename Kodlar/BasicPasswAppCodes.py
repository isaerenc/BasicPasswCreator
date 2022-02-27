__author__ = "isaerenc"

import random

lower = "abcdefghijklmnzoprstuvywxq"
upper = "ABCDEFGHIJKLMNZOPRSTUVYWXQ"
numbers = "1234567890"
symbols = "@-_!=."

string = lower + upper + numbers + symbols
length = 12
password = "".join(random.sample(string, length))

print("Rastgele olusturulmuz  sifreniz: " + password)