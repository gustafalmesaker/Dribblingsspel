from ultralytics import YOLO

model = YOLO('models\\final_model_20_epochs.pt')
#model.export(format='onnx')
model.export(format='openvino')

