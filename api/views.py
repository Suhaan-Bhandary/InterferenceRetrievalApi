import json
from api.functions import create_class, delete_class
from rest_framework.views import Response, APIView, status


class OwlClassView(APIView):
    def get(self, request, format=None):
        # TODO: Will return information about the given node
        return Response({'message': 'Work in progress...'}, status=status.HTTP_200_OK)

    # This method used to create a class
    def post(self, request, format=None):
        try:
            classes = create_class()
            return Response({'message': 'Created node successfully', 'classes': json.dumps(classes)}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'message': 'Unexpected error', 'error': error}, status=status.HTTP_400_BAD_REQUEST)

    # This method is used to delete a class
    def delete(self, request, format=None):
        try:
            new_classes = delete_class()
            return Response({'message': 'Created node successfully', 'classes': json.dumps(new_classes)}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'message': 'Unexpected error', 'error': error}, status=status.HTTP_400_BAD_REQUEST)
