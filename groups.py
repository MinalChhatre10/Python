import re
pattern = r"bread(eggs)*bread"
if re.match(pattern , "breadeggsbread"):
    print("match found")