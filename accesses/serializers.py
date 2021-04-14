from rest_framework import serializers

from accesses.models import DoorUseLog
from accounts.models import Generation, User

from door_access_control_system import settings


class GenerationSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model        = Generation
        fields       = ['name', 'total_cost']
        extra_kwargs = {
            'access_password': {'write_only': True}
        }

    def get_total_cost(self, object):
        count = object.dooruselog_set.count()
        return settings.UNIT_COST*count


class DoorUseLogSerializer(serializers.ModelSerializer):
    generation_name = serializers.SerializerMethodField()

    class Meta:
        model  = DoorUseLog
        fields = ['generation_name', 'create_at']

    def get_generation_name(self, object):
        name = object.generation.name
        return name