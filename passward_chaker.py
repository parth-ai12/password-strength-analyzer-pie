import re
from colorama import Fore, Style
import matplotlib.pyplot as plt

print(Fore.CYAN + "🔍 Password Strength Checker")
print(Style.RESET_ALL)

password = input("Enter your password: ")

score = 0

# Checks
if len(password) >= 8:
    score += 1

if re.search("[A-Z]", password):
    score += 1

if re.search("[0-9]", password):
    score += 1

if re.search("[!@#$%^&*]", password):
    score += 1

# Show score
print(Fore.YELLOW + f"Strength Score: {score}/4")
print(Style.RESET_ALL)

# Result
if score <= 1:
    print(Fore.RED + "Strength: Weak ❌")
elif score <= 3:
    print(Fore.MAGENTA + "Strength: Medium ⚠️")
else:
    print(Fore.GREEN + "Strength: Strong ✅")

print(Style.RESET_ALL)

# 📊 Pie Chart Data
labels = ['Passed', 'Failed']
values = [score, 4 - score]

# Create chart
plt.pie(values, labels=labels, autopct='%1.0f%%')
plt.title("Password Strength Analysis")

# ✅ Save image
plt.savefig("password_strength_chart.png")

# Show chart
plt.show()

print("📁 Chart saved as password_strength_chart.png")