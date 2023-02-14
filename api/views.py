import json
from api.functions import create_class, delete_class, update_class
from rest_framework.views import Response, APIView, status


class OwlClassView(APIView):
    def get(self, request, format=None):
        # TODO: Will return information about the given node
        return Response({'message': 'Work in progress...'}, status=status.HTTP_200_OK)

    # This method used to create a class
    def post(self, request, format=None):
        try:
            classes = create_class()
            print(classes)
            return Response({'message': 'Created node successfully'}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Unexpected error'}, status=status.HTTP_400_BAD_REQUEST)

    # This method is used to delete a class
    def delete(self, request, format=None):
        try:
            new_classes = delete_class()
            print(new_classes)
            return Response({'message': 'Created node successfully'}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Unexpected error'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        try:
            classes = update_class()
            print(classes)
            return Response({'message': 'Updated Node Successfully'}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Unexpected error'}, status=status.HTTP_400_BAD_REQUEST)
