from django.db import models
from ea_account_no.models import UserAccount
from django.utils import timezone
import hashlib
from datetime import timedelta
from django.core.validators import integer_validator


class UserToken(models.Model):
    username = models.CharField(max_length=25, null=True)
    account_no = models.CharField(max_length=25, null=True, validators=[integer_validator])
    token = models.CharField(max_length=40, null=True)
    access_datetime = models.DateTimeField()

    def __str__(self):
        # メールアドレスとアクセス日時、トークンが見えるようにする
        if self.account_no is not None and self.access_datetime is not None and self.token is not None:
            dt = timezone.localtime(self.access_datetime).strftime("%Y/%m/%d %H:%M:%S")
            return str(self.account_no) + '(' + dt + ') - ' + self.token

    @staticmethod
    def get(token_str: str):
        # 引数のトークン文字列が存在するかチェック
        if UserToken.objects.filter(token=token_str).exists():
            return UserToken.objects.get(token=token_str)
        else:
            # 存在しない場合はNoneを返却
            return None

    def check_valid_token(self):
        # このトークンが有効かどうかをチェック
        delta = timedelta(minutes=30)  # 有効時間は30分
        if delta < timezone.now() - self.access_datetime:
            # 最終アクセス時間から30分以上経過している場合はFalseを返却
            return False
        update = UserAccount.objects.get(account_no=self.account_no)
        update.update_access_datetime()
        return True

    def update_access_datetime(self):
        # 最終アクセス日時を現在日時で更新
        self.access_datetime = timezone.now()
        try:
            self.save()
        except():
            print("アクセス日時のアップデートに失敗しました")

    def create(self: UserAccount):
        # ユーザの既存のトークンを取得
        if UserToken.objects.filter(account_no=self.account_no).exists():
            # トークンが既に存在している場合は削除する
            UserToken.objects.filter(account_no=self.account_no).delete()

        # トークン生成（メールアドレス + パスワード + システム日付のハッシュ値とする）
        dt = timezone.now()
        original_str = str(self.account_no) + dt.strftime('%Y%m%d%H%M%S%f')
        hash_str = hashlib.sha1(original_str.encode('utf-8')).hexdigest()  # utf-8でエンコードしないとエラーになる
        # トークンをデータベースに追加
        token = UserToken.objects.create(
            account_no=str(self.account_no),
            token=hash_str,
            access_datetime=dt)

        try:
            user_account_update = UserAccount.objects.get(account_no=self.account_no)
            user_account_update.update_access_datetime()
        except():
            print("トークンを発行したユーザーの最終アクセス日時をアップデートできませんでした。")

        return token
