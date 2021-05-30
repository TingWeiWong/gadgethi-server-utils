import unittest
from gadgethiServerUtils.authentication import GadgethiHMAC256Encryption, GadgethiHMAC256Verification

class AuthenticationTests(unittest.TestCase):
    """
    Testing Strategy:
    - GadgethiHMAC256Encryption
        * constructor
        
    - GadgethiHMAC256Verification
    """

    # GadgethiHMAC256Encryption
    # ----------------------------
    def test_GadgethiHMAC256Encryption_instantiate_ok(self):
        gAuthEncryptor = GadgethiHMAC256Encryption("test-key", "test-secret")
        self.assertIsNotNone(gAuthEncryptor, "could not instantiate calculator")


    # GadgethiHMAC256Verification
    # ----------------------------
    def test_GadgethiHMAC256Verification_instantiate_ok(self):
        verification = GadgethiHMAC256Verification("test-encrypted-message")
        self.assertIsNotNone(verification, "could not instantiate calculator")
