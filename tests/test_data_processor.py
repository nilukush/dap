import unittest

from src.data_processor import WhatsAppDataProcessor


class TestWhatsAppDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = WhatsAppDataProcessor(
            "/mnt/data/september_click_to_whatsapp_ads_leads.csv"
        )

    def test_get_phones_with_whatsapp_referr(self):
        phones = self.processor.get_phones_with_whatsapp_referr()
        # Just a simple test to check if we get an output, more detailed tests can be added based on specific
        # requirements
        self.assertTrue(len(phones) > 0)

    def test_get_filtered_rows(self):
        phones = self.processor.get_phones_with_whatsapp_referr()
        filtered_rows = self.processor.get_filtered_rows(phones)
        # Testing if the filtered rows indeed have the phones we expect
        self.assertTrue(all(row in phones for row in filtered_rows["phone"]))

    def test_get_summary(self):
        summary = self.processor.get_summary()
        # Testing if the summary has all the keys we expect
        self.assertListEqual(
            list(summary.keys()),
            [
                "total_entries",
                "unique_phones",
                "unique_flows",
                "unique_actions",
                "top_flows",
                "top_actions",
            ],
        )


if __name__ == "__main__":
    unittest.main()
