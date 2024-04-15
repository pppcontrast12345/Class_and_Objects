from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        self.social_media = SocialMedia(
            "Mike",
        "Instagram",
        100,
        "stories")

    def test_correct_init(self):
        self.assertEqual("Mike", self.social_media._username)
        self.assertEqual("Instagram", self.social_media._platform)
        self.assertEqual(100, self.social_media._followers)
        self.assertEqual("stories", self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)

    def test_social_media_validate_and_set_platform_attribute(self):
        self.social_media._validate_and_set_platform("Twitter")
        self.assertEqual(self.social_media.platform, "Twitter")

    def test_platform_property(self):
        self.assertEqual("Instagram", self.social_media.platform)

    def test_platform_setter_valid_platform(self):
        self.social_media.platform = "YouTube"
        self.assertEqual("YouTube", self.social_media.platform)

    def test_platform_setter_invalid_platform(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "InvalidPlatform"

        self.assertEqual("Platform should be one of"
                         " ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_followers_setter_valid_value(self):
        self.social_media.followers = 200
        self.assertEqual(200, self.social_media.followers)

    def test_followers_setter_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -50

        self.assertEqual("Followers cannot be negative.",
                         str(ve.exception))

    def test_like_post_valid_index(self):
        self.assertEqual("Invalid post index.", self.social_media.like_post(0))

    def test_like_post_max_likes(self):
        self.social_media._posts = [{'likes': 10, 'comments': []}]
        self.assertEqual("Post has reached the maximum number of likes.", self.social_media.like_post(0))

    def test_like_post_invalid_index(self):
        self.assertEqual("Invalid post index.", self.social_media.like_post(2))

    def test_create_post_returns_string(self):
        post_content = "This is a new post."
        result = self.social_media.create_post(post_content)

        self.assertEqual(result,
                         f"New {self.social_media._content_type}"
                         f" post created by {self.social_media._username} on {self.social_media._platform}.")

    def test_comment_on_post_valid_index_valid_comment(self):
        self.social_media._posts = [{'likes': 5, 'comments': []}]
        self.assertEqual("Comment added by Mike on the post.", self.social_media.comment_on_post(0, "This is a fake post."))

    def test_comment_on_post_valid_index_invalid_comment(self):
        self.social_media._posts = [{'likes': 5, 'comments': []}]
        self.assertEqual("Comment should be more than 10 characters.", self.social_media.comment_on_post(0, "Short."))


if __name__ == "__main__":
    main()