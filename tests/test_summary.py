import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from summarize import summarize

class EvidenceSummaryTests(unittest.TestCase):
    def test_manual_results_do_not_inflate_pass_rate(self):
        result = summarize([{"status":"PASS","count":"76"}, {"status":"FAIL","count":"91"}, {"status":"MANUAL","count":"3"}])
        self.assertEqual(result["evaluated"], 167)
        self.assertEqual(result["pass_rate_percent"], 45.51)
    def test_empty_input_is_not_claimed_compliant(self):
        self.assertIsNone(summarize([])["pass_rate_percent"])
    def test_invalid_results_are_rejected(self):
        for row in [{"status":"UNKNOWN","count":"1"}, {"status":"PASS","count":"-1"}]:
            with self.assertRaises(ValueError):
                summarize([row])

if __name__ == "__main__":
    unittest.main()
