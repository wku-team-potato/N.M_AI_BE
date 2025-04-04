# N.M_AI_BE
- YOLOv8 기반 객체 탐지 모델 API를 제공하는 백엔드 서버
- Django Rest Framework를 사용하여 API 서버 구축

## 시스템 구성도
![시스템 구성도](./assets/images/system_architecture.png)

## 프로젝트 구조
```
N.M_AI_BE
├── foodDetection
│   ├── model
│   │   └── _food_detection.pt
│   ├── service.py
│   ├── urls.py
│   └── views.py
```

## 기술 스택
### 백엔드
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/Ultralytics-FF6600?style=for-the-badge&logo=ultralytics&logoColor=white"/>
</p>

### 기타
<p>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white"/>
  <img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white"/>
</p>

## 문서
[API 문서](./assets/docs/AI_BE_API_DOCS.pdf)