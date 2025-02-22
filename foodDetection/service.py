import os
from ultralytics import YOLO

class DetectionService:
    _model = None

    @staticmethod
    def get_model():
        """
        YOLO 모델을 Lazy Loading 방식으로 동기로 로드
        """
        if DetectionService._model is None:
            # 모델 경로 설정
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            model_path = os.path.join(base_dir, 'foodDetection/model/food_detection.pt')
            
            # YOLO 모델 로드
            DetectionService._model = YOLO(model_path)
        return DetectionService._model

    @staticmethod
    def detect(image_file):
        """
        이미지를 받아 YOLO 모델로 추론 결과를 반환 (동기 처리)
        """
        try:
            # 모델 가져오기
            model = DetectionService.get_model()

            # 이미지 추론
            results = model.predict(image_file)
            return DetectionService.parse_yolo_results(results)
        except Exception as e:
            raise RuntimeError(f"Detection error: {str(e)}")

    @staticmethod
    def parse_yolo_results(results):
        """
        YOLO 모델 추론 결과를 파싱
        """
        parsed_results = []
        for result in results:
            for box in result.boxes:
                parsed_results.append({
                    "label": result.names[int(box.cls[0])],  # 클래스 이름
                    "confidence": float(box.conf[0])         # 예측 신뢰도
                })
        return parsed_results
