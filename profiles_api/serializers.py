from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    #here you cretrieve any field you define
    name = serializers.CharField(max_length=10)