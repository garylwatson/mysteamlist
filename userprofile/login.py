# Access steam user data

def loginFcn():
    import steamfront
    API_KEY = "1A709663E9448C9129559C952D980649"
    client = steamfront.Client(API_KEY)
    userid = input("Enter Steam id: ")
    user = client.getUser(id64=userid)
    print(user.name)
    
loginFcn()