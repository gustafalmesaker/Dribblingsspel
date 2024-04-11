from ultralytics import YOLO

model = YOLO("yolov8n.yaml") #build the model
#model = YOLO("yolov8n.pt") #build the model

results = model.train(data="configs\config.yaml", epochs=1) # train the model