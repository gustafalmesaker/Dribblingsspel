from ultralytics import YOLO

model = YOLO('models\model_v1.1.pt')
model.export(format='onnx')