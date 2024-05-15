from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from assessment.serializers import questionvalueserializers
from assessment.services import assessment_core, assessment_core_services


class AnswerQuestionApi(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def put(self, request, assessment_id):
        result = assessment_core.question_answering(request, assessment_id)
        return Response(result["body"], result["status_code"])


class LoadQuestionnaireAnswerApi(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: ""})
    def get(self, request, assessment_id, questionnaire_id):
        assessments_details = assessment_core_services.load_assessment_details_with_id(request, assessment_id)
        if not assessments_details["Success"]:
            return Response(assessments_details["body"], assessments_details["status_code"])
        result = assessment_core.get_questionnaire_answer(request, assessments_details["body"], questionnaire_id)
        return Response(result["body"], result["status_code"])
