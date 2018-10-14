from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Group, Element


class ElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Element
        fields = ("name", "description", "icon", "created", "group")


class GroupSerializer(serializers.ModelSerializer):
    children = RecursiveField(required=False, allow_null=True, many=True)
    elements = ElementSerializer(many=True, source="element_child")

    class Meta:
        model = Group
        fields = ("id", "name", "description", "icon", 'children_groups_count', 'children_elements_count', "elements",
                  "children", )

    def validate(self, attrs):
        name = attrs.get('name', None)
        children = attrs.get('children', None)

        if not name and not children:
            raise serializers.ValidationError('Enter subgroup for validation')
        return attrs

    def create(self, validated_data):
        elements_data = validated_data.pop('elements')
        group = Group.objects.create(**validated_data)
        for element_data in elements_data:
            Element.objects.create(group=group, **element_data)
        return group

