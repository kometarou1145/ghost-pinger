import tls_client

def get_new_session(client: str, random_ext: bool):
    session = tls_client.Session(
        client_identifier=client,
        random_tls_extension_order=random_ext
    )

    return session