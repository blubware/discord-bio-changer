import requests, json

def bio():
    

    bio = input('Bio: ')

    tokens = open('tokens.txt', 'r'.strip()).readlines()
    
    url = 'https://discord.com/api/v9/users/@me'
    url_2 = 'https://discord.com/api/v9/users/@me/profile'
    
    if len(bio) > 190:
        print('Bio cannot exceed 190 characters, retry')
        bio()
        

    payload = {'bio': bio}
    
    for token in tokens:
        headers = {'authorization': f'{token.strip()}'}
        
        request = requests.get(url, headers=headers)
        
        response = request.text        
        response_content = json.loads(response)

        username = response_content.get('username')
        discriminator = response_content.get('discriminator')
        
        request_2 = requests.patch(url_2, json=payload, headers=headers)
                
        match request_2.status_code:
            case 200:
                print(f'Bio changed to {bio} | {username}#{discriminator}')
                
            case _:
                print(f'''Status code: {request_2.status_code}

Response Text:
{request_2.text}
Token:
{token}''')
                
                
bio()