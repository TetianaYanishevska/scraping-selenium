from services import SocialNetworkScraper

if __name__ == "__main__":
    service = SocialNetworkScraper()
    service.social_network_register()
    service.social_network_login()
    title = "Test automated post"
    content = "Test automated post content"
    service.social_network_add_post(title, content)
    service.social_network_like_post()
    service.social_network_logout()
    print('Done')
