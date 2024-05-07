from ultralytics import YOLO

#model = YOLO("yolov8n.yaml") #build the model
model = YOLO("models\\final_model.pt") #load pretrained model

results = model.train(data="models\configs\config.yaml", epochs=20) # train the model

model.save("final_model_20_epochs.pt")
