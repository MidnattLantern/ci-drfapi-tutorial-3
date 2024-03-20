from rest_framework import serializers
from .models import Child


class ChildSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_parent = serializers.SerializerMethodField()
    display_natal_sex = serializers.SerializerMethodField()
    display_choosen_sex = serializers.SerializerMethodField()

    def get_is_parent(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_display_natal_sex(self, obj):
        return obj.get_natal_sex_display()
    
    def get_display_choosen_sex(self, obj):
        return obj.get_choosen_sex_display()


    class Meta:
        """
        Meta class for ChildSerializer
        """
        model = Child
        fields = [
            'id',
            'owner',
            'register_date',
            'register_update_date',
            'name',
            'age',
            'is_parent',

            'natal_sex',
            'display_natal_sex',
            'choosen_sex',
            'display_choosen_sex',
        ]

