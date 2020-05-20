from rest_framework import routers
from login.api import CreateUserView, CreatePostsView

router = routers.SimpleRouter()
router.register(r"users", CreateUserView, basename="user")
router.register(r"posts", CreatePostsView, basename="post")

urlpatterns = router.urls
