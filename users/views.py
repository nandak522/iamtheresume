from utils import response

def view_homepage(request, homepage_template):
    user = request.user
    if user.is_authenticated():
        return response(request, homepage_template, {'message':'Welcome %s' % user.email})
    return response(request, homepage_template, {'message':'You are Anonymous'})
