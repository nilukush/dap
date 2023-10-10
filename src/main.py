from data_processor import WhatsAppDataProcessor

if __name__ == "__main__":
    print("[DEBUG] Initializing WhatsAppDataProcessor...")
    processor = WhatsAppDataProcessor(
        "../data/september_click_to_whatsapp_ads_leads.csv"
    )

    print("\n[DEBUG] Extracting phones with 'Whatsapp Referr'...")
    phones_with_whatsapp_referr = processor.get_phones_with_whatsapp_referr()

    print("\n[DEBUG] Saving filtered rows to CSV...")
    processor.save_filtered_rows_to_csv(
        phones_with_whatsapp_referr, "../outputs/filtered_data.csv"
    )

    print("\n[DEBUG] Getting summary of the data...")
    print(processor.get_summary())
