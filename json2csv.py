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
                ymin = annotation['y']
                xmin = annotation['x']
                w = annotation['w']
                h = annotation['h']
                xmax = xmin + w
                ymax = ymin + h
                label = "body"
                csv_labels.write(img_path+","+str(xmin)+","+str(ymin)+","+str(xmax)+","+str(ymax)+","+label+"\n")
        else:
            pass
            for annotation in annotations:
                w = 2
                h = 2
                ymin = annotation['y']
                xmin = annotation['x']
                xmax = xmin + w
                ymax = ymin + h
                label = "head"
                csv_labels.write(img_path+","+str(xmin)+","+str(ymin)+","+str(xmax)+","+str(ymax)+","+label+"\n")
        print(i)
csv_labels.close()
print('success')