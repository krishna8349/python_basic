print("Twinkle, Twinkle, Little star, \n\tHow I wonder what you are!\n\t\t Up above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, Twinkle, Little star, \n\tHow I wonder What you are!")


print("--------------------------------")
# for checking python version
import sys

print("python varsion")
print(sys.version)
print("version info")
print(sys.version_info)

print("--------------------------")

# for current time
import datetime

now = datetime.datetime.now()
print("Current time")
print(now.strftime("%Y-%m-%d %H:%M:%S"))