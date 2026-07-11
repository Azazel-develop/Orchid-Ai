import hashlib


class SecureMemory:


    def encrypt(self,data):

        return hashlib.sha256(
            data.encode()
        ).hexdigest()
