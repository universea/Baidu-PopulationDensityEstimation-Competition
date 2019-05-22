import json 
import csv

csv_labels = open("csv_labels.csv","w")

with open('train.json','r') as flist:
    jsons = json.load(flist)
    print(len(jsons['annotations']))
    for i in range(len(jsons['annotations'])):
        img_path = jsons['annotations'][i]['name']
        img_path = img_path.replace('stage1/train/', '')
        annotations = jsons['annotations'][i]['annotation']
        #标注类型 bbox或者dot
        type = jsons['annotations'][i]['type']
        if type == "bbox":
            for annotation in annotations:
                w = annotation['w']
                h = annotation['h']
                ymin = annotation['y']
                xmin = annotation['x']
                label = "1"
                csv_labels.write(img_path+","+str(xmin)+","+str(ymin)+","+str(w)+","+str(h)+","+label+"\n")
        else:
            for annotation in annotations:
                w = 10
                h = 10
                ymin = annotation['y']
                xmin = annotation['x']
                label = "1"
                csv_labels.write(img_path+","+str(xmin)+","+str(ymin)+","+str(w)+","+str(h)+","+label+"\n")
        print(i)
csv_labels.close()
print('success')