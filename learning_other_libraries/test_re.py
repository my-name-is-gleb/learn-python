import re

log = "Входящий запрос от 192.168.1.15, перенаправлено на 10.0.0.5, статус: успех"

pattern = r"\d+\.\d+\.\d+\.\d+"

result = re.findall(pattern, log)
print(result)

config = "Device: Vacuum_Cleaner_X1; Token: ABC-123-XYZ; Status: Online"

pattern_2 = r"Token: ([\w-]+)"

result_2 = re.findall(pattern_2, config)
print(result_2)