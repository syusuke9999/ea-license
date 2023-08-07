from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import UserToken
from ea_account_no.models import UserAccount
import json


@csrf_exempt
class Login(APIView):
    @staticmethod
    def post(request):
        # リクエストボディのJSONを読み込み、メールアドレス、パスワードを取得
        try:
            data = json.loads(request.body)
            account_no = data['account_no']
        except():
            # JSONの読み込みに失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)
        # アカウント番号からユーザを取得
        if not UserAccount.objects.filter(account_no=account_no).exists():
            # 存在しない場合は403を返却
            return JsonResponse({'message': 'There is no such account no'}, status=403)
        user = UserAccount.objects.get(account_no=account_no)
        # ログインOKの場合は、トークンを生成
        token = UserToken.create(user)
        # トークンを取得した日付を更新
        try:
            user.update_access_datetime()
        except():
            print("日付の更新に失敗しました")
        # トークンを返却
        return JsonResponse({'token': token.token})


class AuthAPI(APIView):
    # authentication_classes = (EaAuthentication,)
    # permission_classes = (IsAuthenticated,)
    @staticmethod
    def post(request):
        return JsonResponse(
            {'response': 'OK'}
        )
