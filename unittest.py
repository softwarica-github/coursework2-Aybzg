import unittest
from PIL import Image
from main import Stegno  

class TestStegno(unittest.TestCase):

    def setUp(self):
        self.stegno = Stegno()

    def test_genData(self):
        data = "Hi"
        expected_output = ['01001000', '01101001']
        self.assertEqual(self.stegno.genData(data), expected_output, "The genData method does not work as expected.")

    def test_modPix(self):
        
        pixels = [(0, 0, 0), (1, 1, 1), (2, 2, 2)] * 3
        data = "H"  # 01001000 in binary
        modified_pixels = list(self.stegno.modPix(pixels, data))
        self.assertNotEqual(pixels[:9], modified_pixels, "The modPix method does not modify the pixels as expected.")

    def test_encode_and_decode(self):
        
        original_message = "Secret Message"
        img = Image.new('RGB', (100, 100), color = 'white')
        self.stegno.encode_enc(img, original_message)
        decoded_message = self.stegno.decode(img)
        self.assertEqual(original_message, decoded_message, "The decoded message does not match the original.")

if __name__ == '__main__':
    unittest.main()
