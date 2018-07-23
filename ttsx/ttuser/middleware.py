# coding = utf-8
from django.utils import deprecation


# 中间件，view中间件，返回未登录的地址，
class UrlMiddleware(deprecation.MiddlewareMixin):
    def process_view(self, request, view_name, view_args, view_kwargs):
        if request.path not in ['/user/register/',
                                '/user/register_handle/',
                                '/user/login/',
                                '/user/register_valid/',
                                '/user/login_handle/',
                                '/user/login_out/',
                                '/user/islogin/',]:
            request.session['url_path'] = request.get_full_path()
