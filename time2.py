# Eleonora 
# 15 OCtober

str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?") 
time = int(str_time)
wai_time = int(str_wait_time)

time_when_alarm_go_off = time + wai_time # typo in wai_time "wait"
print(time_when_alarm_go_off)
