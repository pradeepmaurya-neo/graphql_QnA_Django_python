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

    # all_quizzes = DjangoListField(QuizzesType)
    # all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())
    all_question = graphene.Field(QuestionType, id = graphene.Int())
    all_answers = graphene.List(AnswersType, id = graphene.Int())

    # def resolve_all_quizzes(root, info, id):
    #     return Quizzes.objects.get(pk=id)


    def resolve_all_question(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(questions=id)


schema = graphene.Schema(query=Query)
