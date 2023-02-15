import os
import hvac

if __name__ == "__main__":
    VAULT_URL = (os.environ.get('VAULT_URL'))
    VAULT_NAMESPACE = (os.environ.get('VAULT_NAMESPACE'))
    VAULT_ROLE_ID = (os.environ.get('VAULT_ROLE_ID'))
    VAULT_SECRET_ID = (os.environ.get('VAULT_SECRET_ID'))
    

    client = hvac.Client(url=VAULT_URL,
                     namespace=VAULT_NAMESPACE)

    client.auth.approle.login(
        role_id=VAULT_ROLE_ID,
        secret_id=VAULT_SECRET_ID
        )

    current_token = client.auth.token.lookup_self()
    print(f"{client.is_authenticated() =}")

