import logging

from django.http import HttpResponse

from polls.models import Question


def index(request):
    logger = logging.getLogger(__name__)

    # リクエストヘッダーのキーを確認するため、headersとMETAを見る
    # なお、request-id が埋め込まれたログが出力される
    logger.debug(list(request.headers.keys()))
    logger.debug(list(request.META.keys()))

    # x-request-id ヘッダの中身を確認
    logger.debug(request.META.get('HTTP_X_REQUEST_ID'))

    # ログへSQLの内容を出力するために、list()を使ってSQLを即時実行する
    list(Question.objects.all())

    return HttpResponse("Hello, world!!")


def exception(request):
    logger = logging.getLogger(__name__)

    try:
        raise Exception('my exception')
    except Exception as e:
        logger.debug(e)
        raise e
