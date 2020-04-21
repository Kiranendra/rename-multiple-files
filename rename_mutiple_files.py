from os import listdir, rename

source_path = "G:\\Pictures\\MCA Family(PP)\\Farewell_Cropped_Images\\Selected\\"
files = [f for f in listdir(source_path)]
i = 0

for file in files:
    try:
        i += 1
        rename(source_path + file, source_path + str(i) + ".jpg")
    except Exception as e:
        print("ERROR : ==> " + str(e))
        

print("Operation Successfully")
