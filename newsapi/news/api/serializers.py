from rest_framework import serializers
from news.models import Article, Journalist
from datetime import datetime
from django.utils.timesince import timesince


class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()
    # author = JournalistSerializer(read_only=True)
    class Meta:
        model = Article
        fields = "__all__"

    def get_time_since_publication(self,object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date,now)
        return time_delta

class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="article-detail")
    # articles = ArticleSerializer(many=True,read_only=True)
    class Meta:
        model = Journalist
        fields = "__all__"

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     def create(self,validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self,instance,validated_data):
#         instance.author = validated_data.get('author',instance.author)
#         instance.save()
#         return instance;
#
#     def validate(self,data):
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title and description cannot be same..!!")
#         return data
#
#     def validate_title(self,value):
#         if len(value)<10:
#             raise serializers.ValidationError("Title must be atleast 10 characters..!!")
#         return value