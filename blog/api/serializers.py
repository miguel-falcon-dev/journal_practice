from rest_framework import serializers
import blog.models as b_mdls

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = b_mdls.Entry
        fields = ["creation_date", "updated_date", "feeling", "description", "photo", "time_stamp"]