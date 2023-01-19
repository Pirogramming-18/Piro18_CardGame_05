from random import choice

class Card(models.Model):
	card_num = models.IntegerField()

	def __str__(self):
		return str(self.card_num)

class Attack(models.Model):
	attack_user = models.ForeignKey(User, on_delete=models.CASCADE)
	num = models.ForeignKey(Card, on_delete=models.CASCADE)
  attacked_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Defense(models.Model):
	defense_user = models.ForeignKey(Attack, on_delete=models.CASCADE)
	num = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True)

MODE_CHOICES = {('큰 수', '큰 수'), ('작은 수', '작은 수')}
STATUS_CHOICES = {'진행 중', '진행 중'), ('끝', '끝')}
class CardGame(models.Model):
	mode = models.CharField(max_length=30, choices = MODE_CHOICES) # 큰 수가 이기는 게임 혹은 작은 수가 이기는 게임
	status = models.CharField(max_length=30, choices = STATUS_CHOICES) # 게임 상태값
	attack = models.OnetoOneField(Attack, on_delete=models.CASCADE)
	defense = models.OnetoOneField(Defense, on_delete=models.CASCADE)
	win_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class User(models.Model):
	name = models.CharField(max_length=64)
	score = models.IntegerField()
	card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="User_game")

#소셜 로그인
NAVER_CALLBACK_URI = BASE_URL + 'naver/callback/'
GOOGLE_CALLBACK_URI = BASE_URL + 'google/callback/'

class NaverLogin(SocialLoginView):
    adapter_class = NaverOAuth2Adapter
    callback_url = NAVER_CALLBACK_URI
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer