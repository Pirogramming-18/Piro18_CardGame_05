from django.shortcuts import render

# BASE_URL = 'http://localhost:8000/api/v1/accounts/rest-auth/'

#소셜 로그인
# NAVER_CALLBACK_URI = BASE_URL + 'naver/callback/'
# GOOGLE_CALLBACK_URI = BASE_URL + 'google/callback/'

# class NaverLogin(SocialLoginView):
#     adapter_class = NaverOAuth2Adapter
#     callback_url = NAVER_CALLBACK_URI
#     client_class = OAuth2Client
#     serializer_class = SocialLoginSerializer

# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = GOOGLE_CALLBACK_URI
#     client_class = OAuth2Client
#     serializer_class = SocialLoginSerializer