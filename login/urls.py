from rest_framework import routers
from login.api import CreateUserView, CreatePostsView, CreateProfileView

router = routers.SimpleRouter()
router.register(r"users", CreateUserView, basename="user")
router.register(r"posts", CreatePostsView, basename="post")
router.register(r"profile", CreateProfileView, basename="profile")

urlpatterns = router.urls
