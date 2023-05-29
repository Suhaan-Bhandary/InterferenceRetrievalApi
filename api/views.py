import json
from api.functions import create_class, delete_class, update_class, get_data_summary, get_user_query_output
from rest_framework.views import Response, APIView, status
import os
import sys


class OwlClassView(APIView):
    def get(self, request, format=None):
        get_data_summary()
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)

    # This method used to create a class
    def post(self, request, format=None):
        try:
            if 'data_file' not in request.FILES:
                return Response({'message': 'Please Provide a data_file', status: status.HTTP_400_BAD_REQUEST})

            # Get the file from the post request
            file_obj = request.FILES['data_file']

            # Check if the file is of correct extension
            file_name = str(file_obj)
            if not file_name.endswith('.xlsx'):
                return Response({'message': 'Please upload a File with .xlsx extension'})

            # Create class using the file object
            classes = create_class(file_obj)
            print(classes)

            return Response({'message': 'Created node successfully'}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Unexpected error'}, status=status.HTTP_400_BAD_REQUEST)

    # This method is used to delete a class
    def delete(self, request, format=None):
        try:

            new_classes = delete_class(request.data['class_name'])

            return Response({'message': 'Deleted node successfully'}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Unexpected error'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        try:

            # if 'class_name' not in request.data or 'sub_class_name' not in request.data:
            #     return Response(
            #         {'message': 'Please provide class_name and sub_class_name in request body'},
            #         status=status.HTTP_400_BAD_REQUEST
            #     )

            # Get the data from the body of the request
            print(request.data)
            class_name = request.data['class_name']

            sub_class_name = request.data['sub_class_name']
            relationship = request.data['relationship']

            domain = request.data['domain']
            range = request.data['range']
            print("relationship" + relationship)

            # Update the owl
            classes = update_class(
                class_name, sub_class_name, relationship, domain, range)

            return Response({'message': 'Updated Node Successfully'}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'message': 'Unexpected error'}, status=status.HTTP_400_BAD_REQUEST)


class UserQueryClass(APIView):
    def post(self, request, format=None):
        try:
            user_text = request.data['user_text']
            data = get_user_query_output(user_text)
            print(data)
            return Response({'message': 'Successfully', "data": data}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Unexpected error'}, status=status.HTTP_400_BAD_REQUEST)
