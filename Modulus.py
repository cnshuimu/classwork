# Q1
time = float(input())
hour = time // 60
minute = time % 60
print(f"{time} equal to {hour} hours {minute} minutes")

# Q2
total_minute = float(input())
minutes = total_minute % 60
hours = total_minute // 60
print(f"{total_minute} equal to {round(hours, 2)} hour {round(minutes, 2)} minutes")

# Q3
frame_count = int(input())
judge = frame_count % 60
if judge == 0:
    print("shoot the lazer")
else:
    print("wait for a momment")

# Q4
total_cents = float(input())
dollar = total_cents // 100
cent = total_cents % 100
print(dollar, "dollars", cent, "cents" )

# Q5
cents = int(input())
toonie = cents // 200
loonie = cents % 200 // 100
quarter = cents % 100 // 25
dime = cents % 25 // 10
nickle = cents % 10 // 5
penny = cents % 5 // 1
print(f"""{cents} cents is:
{toonie} - toonie
{loonie} - loonie
{quarter} - quarter
{dime} - dime
{nickle} - nickle
{penny} - penny""")

# Q6
id = int(input("student number:"))
group = id % 5
number = str(group)
if group == 0:
    print("You are in group #" + number)
elif group == 1:
    print("You are in group #" + number)
elif group == 2:
    print("You are in group #" + number)
elif group == 3:
    print("You are in group #" + number)
elif group == 4:
    print("You are in group #" + number)
# Q6
def group_number():
    id = int(input("student number:"))
    group = id % 5
    print("You are in group #" + str(group))
group_number()

# calculate total digits
num = input()
index = 0
sum = 0
while index <= len(str(num))-1:
    a = list(str(num)[index])
    index += 1
    for i in a:
        sum += int(i)
print(sum)
