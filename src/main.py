import os
import hvac

def to_env(key):
    return key.replace('/', '_').upper()

if __name__ == "__main__":
    VAULT_URL = (os.environ.get('VAULT_URL'))
    VAULT_NAMESPACE = (os.environ.get('VAULT_NAMESPACE'))
    VAULT_ROLE_ID = (os.environ.get('VAULT_ROLE_ID'))
    VAULT_SECRET_ID = (os.environ.get('VAULT_SECRET_ID'))
    SECRET_BASE_PATH = (os.environ.get('SECRET_BASE_PATH'))

    client = hvac.Client(url=VAULT_URL,
                     namespace=VAULT_NAMESPACE)

    client.auth.approle.login(
        role_id=VAULT_ROLE_ID,
        secret_id=VAULT_SECRET_ID
        )

    current_token = client.auth.token.lookup_self()
    # print(f"{client.is_authenticated() =}")

    list_response = client.secrets.kv.v2.list_secrets(
        path=SECRET_BASE_PATH,
        mount_point='secret')


    secrets = list_response['data']['keys']


    for secret in secrets:
        secret_version_response = client.secrets.kv.v2.read_secret_version(
            path="{0}/{1}".format(SECRET_BASE_PATH, secret),
            mount_point="secret"
        )

        for key in secret_version_response['data']['data'].keys():
            env_key = "{0}/{1}/{2}".format(SECRET_BASE_PATH, secret, key)
            print(f"{to_env(env_key)}={secret_version_response['data']['data'][key]}")

