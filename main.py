from chat_sharing import ChatSharing


if __name__ == '__main__':
    print('\n---> start testing...\n')
    sharing = ChatSharing()
    sharing.handle_website_message_from_webhook({'message': 'Hello'})
    print('\n\n------------------------------------------------------------------------------------------\n\n')
    other_sharing = ChatSharing()
    other_sharing.handle_website_message_from_salesman({'message': 'Hello'})
    print('\n---> end testing...\n')
