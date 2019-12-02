from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Use Http methods functions(get,post,patch,put,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control of your application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
