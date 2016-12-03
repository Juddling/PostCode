import re
import unittest

pattern = """
    (GIR\s0AA) |
    (
        # A9 or A99 prefix
        ( ([A-PR-UWYZ][0-9][0-9]?) |
             # AA99 prefix with some excluded areas
            (([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9]) |
             # AA9 prefix with some excluded areas
             ([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9]) |
             # WC1A prefix
             (WC[0-9][A-Z]) |
             (
                # A9A prefix
               ([A-PR-UWYZ][0-9][A-HJKPSTUW]) |
                # AA9A prefix
               ([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])
             )
            )
          )
          # 9AA suffix
        (?P<space>\s)[0-9][ABD-HJLNP-UW-Z]{2}
    )"""
prog = re.compile(pattern, re.VERBOSE)


class TestPostCodes(unittest.TestCase):
    def assert_invalid_postcode(self, post_code):
        self.assertIsNone(prog.match(post_code))

    def test_junk(self):
        self.assert_invalid_postcode("$%± ()()")

    def test_invalid(self):
        self.assert_invalid_postcode("XX XXX")

    def test_incorrect_length(self):
        self.assert_invalid_postcode("A1 9A")

    def test_no_space(self):
        self.assert_invalid_postcode("LS44PL")

    def test_q_in_first_position(self):
        self.assert_invalid_postcode("Q1A 9AA")

    def test_v_in_first_position(self):
        self.assert_invalid_postcode("V1A 9AA")

    def test_x_in_first_position(self):
        self.assert_invalid_postcode("X1A 9BB")

    def test_i_in_second_position(self):
        self.assert_invalid_postcode("LI10 3QP")

    def test_j_in_second_position(self):
        self.assert_invalid_postcode("LJ10 3QP")

    def test_z_in_second_position(self):
        self.assert_invalid_postcode("LZ10 3QP")

    def text_c_in_fourth_position(self):
        self.assert_invalid_postcode("AA9C 9AA")

    def test_single_digit_district(self):
        self.assert_invalid_postcode("FY10 4PL")

    def test_double_digit_district(self):
        self.assert_invalid_postcode("SO1 4QQ")

    def test_valid_codes(self):
        valid_codes = [
            "EC1A 1BB",
            "W1A 0AX",
            "M1 1AE",
            "B33 8TH",
            "CR2 6XH",
            "DN55 1PT",
            "GIR 0AA",
            "SO10 9AA",
            "FY9 9AA",
            "WC1A 9AA"]

        for code in valid_codes:
            self.assertIsNotNone(prog.match(code))
