# Website for Finding People with Similar Interests

# List to store user profiles
profiles = []

# Function to create a user profile
def create_profile(username, interests):
    profile = {
        'username': username,
        'interests': interests.split(', ')
    }
    profiles.append(profile)
    print(f'Profile for "{username}" created successfully!')

# Function to list all user profiles
def list_profiles():
    if not profiles:
        print('No profiles to display.')
    else:
        print('User Profiles:')
        for i, profile in enumerate(profiles):
            print(f'{i + 1}. Username: {profile["username"]}, Interests: {", ".join(profile["interests"])}')

# Function to find people with similar interests
def find_similar_interests(username):
    similar_profiles = []
    for profile in profiles:
        if profile['username'] != username:
            common_interests = set(profile['interests']) & set(profiles[username]['interests'])
            if common_interests:
                similar_profiles.append(profile)
    
    if not similar_profiles:
        print(f'No users with similar interests found for "{username}".')
    else:
        print(f'Users with similar interests to "{username}":')
        for i, profile in enumerate(similar_profiles):
            print(f'{i + 1}. Username: {profile["username"]}, Interests: {", ".join(profile["interests"])}')

# Main program loop
while True:
    print('\nWebsite Menu:')
    print('1. Create Profile')
    print('2. List Profiles')
    print('3. Find Similar Interests')
    print('4. Exit')
    
    choice = input('Enter your choice: ')
    
    if choice == '1':
        username = input('Enter your username: ')
        interests = input('Enter your interests (comma-separated): ')
        create_profile(username, interests)
    elif choice == '2':
        list_profiles()
    elif choice == '3':
        username = input('Enter your username to find similar interests: ')
        find_similar_interests(username)
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.')
# Website for Finding People with Similar Interests (Simplified)

# Dictionary to store user profiles
profiles = {}

# Function to create a user profile
def create_profile(username, interests):
    profiles[username] = interests.split(', ')

# Function to find people with similar interests
def find_similar_interests(username):
    user_interests = profiles.get(username)
    if user_interests is None:
        print(f'User "{username}" not found.')
        return
    
    similar_users = [user for user, interests in profiles.items() if user != username and set(user_interests) & set(interests)]
    
    if not similar_users:
        print(f'No users with similar interests to "{username}".')
    else:
        print(f'Users with similar interests to "{username}":')
        for user in similar_users:
            print(user)

# Main program loop
while True:
    print('\nWebsite Menu:')
    print('1. Create Profile')
    print('2. Find Similar Interests')
    print('3. Exit')
    
    choice = input('Enter your choice: ')
    
    if choice == '1':
        username = input('Enter your username: ')
        interests = input('Enter your interests (comma-separated): ')
        create_profile(username, interests)
    elif choice == '2':
        username = input('Enter your username to find similar interests: ')
        find_similar_interests(username)
    elif choice == '3':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please try again.')
