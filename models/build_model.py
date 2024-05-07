from ultralytics import YOLO

#model = YOLO("yolov8n.yaml") #build the model
model = YOLO("models\final_model.pt") #load pretrained model

results = model.train(data="configs\config_only_ball.yaml", epochs=10) # train the model

results.save("final_ball_model.pt")
