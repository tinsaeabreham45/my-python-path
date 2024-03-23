current_users = ['StellarEcho','LunaSpectra','ZenithVortex','admin','SereneCipher','QuantumQuill',
                 'LunaCraze','SolarSculpt','MysticPulse']
new_users = ['lunaSpectra','ZephyrWhisper','SereneCipher','EchoEnigma','NimbusNova']

for users in new_users:
    if users.title() in current_users == users:
        print(f'{users} has been used try other name please')
    else:
        print(f'hello: {users}')