import os

ROAST = "It's 6 a.m. on a Saturday and the alarm is screaming like I owe it rent. I set you for weekdays, you traitor \u2014 the weekend is sacred."

os.makedirs("/output", exist_ok=True)
fd = os.open("/output/entry.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
os.write(fd, ROAST.encode("utf-8"))
os.close(fd)
