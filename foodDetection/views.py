# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser
# from rest_framework.response import Response
# from rest_framework import status
from asgiref.sync import sync_to_async
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from PIL import Image
from foodDetection.service import DetectionService
# from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

# @method_decorator(csrf_exempt, name='dispatch')
# class AsyncDetectionView(View):
#     def parse_request(self, request):
#         """
#         Helper method to parse the request for uploaded image.
#         """
#         image_file = request.FILES.get('image')
#         if not image_file:
#             raise ValueError("No image uploaded")
#         return image_file

#     @swagger_auto_schema(
#         operation_description="이미지를 업로드하면 YOLO 모델을 사용하여 음식 탐지 결과를 반환합니다.",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'image': openapi.Schema(
#                     type=openapi.TYPE_FILE,
#                     description='탐지할 이미지 파일'
#                 ),
#             },
#             required=['image']
#         ),
#         responses={
#             200: openapi.Schema(
#                 type=openapi.TYPE_OBJECT,
#                 properties={
#                     'result': openapi.Schema(
#                         type=openapi.TYPE_ARRAY,
#                         items=openapi.Schema(
#                             type=openapi.TYPE_OBJECT,
#                             properties={
#                                 'label': openapi.Schema(
#                                     type=openapi.TYPE_STRING,
#                                     description="탐지된 객체의 클래스 라벨"
#                                 ),
#                                 'confidence': openapi.Schema(
#                                     type=openapi.TYPE_NUMBER,
#                                     format='float',
#                                     description="탐지 신뢰도 (0.0 ~ 1.0)"
#                                 ),
#                             },
#                         ),
#                         description="탐지된 객체 리스트",
#                     ),
#                 }
#             ),
#             400: openapi.Schema(
#                 type=openapi.TYPE_OBJECT,
#                 properties={
#                     'error': openapi.Schema(type=openapi.TYPE_STRING)
#                 }
#             ),
#         }
#     )
#     async def post(self, request, *args, **kwargs):
#         try:
#             image_file = self.parse_request(request)
#             detection_results = await sync_to_async(DetectionService.detect)(Image.open(image_file))
#             return JsonResponse({'result': detection_results}, status=200)
#         except ValueError as ve:
#             return JsonResponse({'error': str(ve)}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': f'Detection error: {str(e)}'}, status=500)

# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser
# from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
# from asgiref.sync import sync_to_async
# from PIL import Image


# class AsyncDetectionView(APIView):
#     parser_classes = [MultiPartParser]  # 파일 업로드 지원

#     @swagger_auto_schema(
#         operation_description="이미지를 업로드하면 YOLO 모델을 사용하여 음식 탐지 결과를 반환합니다.",
#         manual_parameters=[
#             openapi.Parameter(
#                 'image',
#                 openapi.IN_FORM,
#                 description="탐지할 이미지 파일",
#                 type=openapi.TYPE_FILE,
#                 required=True,
#             ),
#         ],
#         responses={
#             200: openapi.Schema(
#                 type=openapi.TYPE_OBJECT,
#                 properties={
#                     'result': openapi.Schema(
#                         type=openapi.TYPE_ARRAY,
#                         items=openapi.Schema(
#                             type=openapi.TYPE_OBJECT,
#                             properties={
#                                 'label': openapi.Schema(
#                                     type=openapi.TYPE_STRING,
#                                     description="탐지된 객체의 클래스 라벨"
#                                 ),
#                                 'confidence': openapi.Schema(
#                                     type=openapi.TYPE_NUMBER,
#                                     format='float',
#                                     description="탐지 신뢰도 (0.0 ~ 1.0)"
#                                 ),
#                             },
#                         ),
#                         description="탐지된 객체 리스트",
#                     ),
#                 }
#             ),
#             400: openapi.Schema(
#                 type=openapi.TYPE_OBJECT,
#                 properties={
#                     'error': openapi.Schema(type=openapi.TYPE_STRING)
#                 }
#             ),
#         }
#     )
#     async def post(self, request, *args, **kwargs):
#         try:
#             image_file = request.FILES.get('image')
#             if not image_file:
#                 return Response({'error': 'No image uploaded'}, status=HTTP_400_BAD_REQUEST)

#             # YOLO 탐지 서비스 호출
#             detection_results = await sync_to_async(DetectionService.detect)(Image.open(image_file))
#             return Response({'result': detection_results}, status=200)
#         except ValueError as ve:
#             return Response({'error': str(ve)}, status=HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': f'Detection error: {str(e)}'}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class SyncDetectionView(APIView):
    parser_classes = [MultiPartParser]  # 파일 업로드 지원

    @swagger_auto_schema(
        operation_description="이미지를 업로드하면 YOLO 모델을 사용하여 음식 탐지 결과를 반환합니다.",
        manual_parameters=[
            openapi.Parameter(
                'image',
                openapi.IN_FORM,
                description="탐지할 이미지 파일",
                type=openapi.TYPE_FILE,
                required=True,
            ),
        ],
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'result': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'label': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description="탐지된 객체의 클래스 라벨"
                                ),
                                'confidence': openapi.Schema(
                                    type=openapi.TYPE_NUMBER,
                                    format='float',
                                    description="탐지 신뢰도 (0.0 ~ 1.0)"
                                ),
                            },
                        ),
                        description="탐지된 객체 리스트",
                    ),
                }
            ),
            400: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING)
                }
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        try:
            image_file = request.FILES.get('image')
            if not image_file:
                return Response({'error': 'No image uploaded'}, status=HTTP_400_BAD_REQUEST)

            # YOLO 탐지 서비스 호출 (동기적으로 처리)
            detection_results = DetectionService.detect(Image.open(image_file))
            return Response({'result': detection_results}, status=200)
        except ValueError as ve:
            return Response({'error': str(ve)}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Detection error: {str(e)}'}, status=HTTP_500_INTERNAL_SERVER_ERROR)
