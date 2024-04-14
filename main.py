from ultralytics import YOLO

#model = YOLO("yolov8n.yaml") #build the model
model = YOLO("yolov8n.pt") #load pretrained model

results = model.train(data="configs\config.yaml", epochs=1) # train the model

#model.save("models/model_v0.pt")
