from unicodedata import category
import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from qnapp.models import Category, Question, Quizzes, Answer


class Categorytype(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id', 'title', 'category',)


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title', 'quiz')


class AnswersType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('questions', 'answer_text')




class Query(graphene.ObjectType):

    quizz = graphene.String()

    def resolve_quizz(root, info):
        return f"This is First Questions"



schema = graphene.Schema(query=Query)
