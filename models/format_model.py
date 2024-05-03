from ultralytics import YOLO

model = YOLO('final_model.pt')
#model.export(format='onnx')
model.export(format='openvino')

