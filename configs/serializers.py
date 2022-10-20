from rest_framework import serializers

class AttributeSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    value = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ConfigSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    attributes = AttributeSerializer(many=True)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
