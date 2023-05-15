from services import SocialNetworkScraper

if __name__ == "__main__":
    service = SocialNetworkScraper()
    title = "Test automated post"
    content = "Test automated post content"
    service.social_network_add_post(title, content)
    print('Done')
