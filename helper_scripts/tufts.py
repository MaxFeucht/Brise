#%%


import os
from PIL import Image
import cv2
import shutil
import pandas as pd

#%%

#Extract and rename data from all 
folders = [dir for dir in os.listdir("data/") if "TD_IR" in dir]
for folder in folders:
    target_path = "data/" + folder
    sets = [dir for dir in os.listdir(target_path) if not "other" in dir]
    for set in sets:
        path = "data/" + folder + "/" + set
        individuals = [file for file in os.listdir(path)]
        for ind in individuals: 
            try: 
                images = os.listdir(path + "/" + ind)
                for img in images:
                    file_path = path + "/" + ind + "/" + img
                    img_num = str(img).rsplit("_")[-1]
                    new_filename = folder + "_"  + str(ind) + "_" + str(img_num) + ".jpg"
                    shutil.move(file_path, target_path + "/" + new_filename)
            except: 
                pass


#%%

bounding_boxes = pd.read_csv("data/bounding_boxes.csv.csv")
bounding_boxes.rename({col: col.lower() for col in bounding_boxes.columns}, axis = 1, inplace = True)
bounding_boxes["img_num"] = bounding_boxes.file.apply(lambda x: pd.Series(str(x).rsplit("_")[-1].replace(".jpg","")))
bounding_boxes['filename'] = bounding_boxes.set.apply(lambda x: pd.Series(str(x)[:7])).squeeze(axis = 1) + "_" + bounding_boxes["participant"].astype(str) + "_" + bounding_boxes["img_num"].astype(str) + ".jpg"
bounding_boxes.to_csv("bounding_boxes_update.csv", index = False)

#%%

pics = [pic for pic in os.listdir() if".jpg" in pic]

idx = 0
for pic in pics:
    if "TD_IR_E" in pic:
        shutil.move(pic, "data/TD_IR_E" + str(idx) + ".jpg")
    elif "TD_IR_A" in pic:
        shutil.move(pic, "data/TD_IR_A" + str(idx) + ".jpg")
   

# %%
