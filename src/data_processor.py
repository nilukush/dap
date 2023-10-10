import pandas as pd


class WhatsAppDataProcessor:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        print("[DEBUG] Loaded CSV data with shape:", self.df.shape)

    def get_phones_with_whatsapp_referr(self):
        phones = self.df[self.df["flow_name"] == "Whatsapp Referr"]["phone"].unique()
        print(
            f"[DEBUG] Found {len(phones)} unique phones with 'Whatsapp Referr' flow_name."
        )
        return phones

    def get_filtered_rows(self, phones):
        filtered_rows = self.df[self.df["phone"].isin(phones)]
        print(
            f"[DEBUG] Filtered rows based on phones. Shape of the result: {filtered_rows.shape}"
        )
        return filtered_rows

    def save_filtered_rows_to_csv(self, phones, output_file="filtered_data.csv"):
        filtered_rows = self.get_filtered_rows(phones)
        filtered_rows.to_csv(output_file, index=False)
        print(f"[DEBUG] Saved filtered rows to {output_file}")

    def get_summary(self):
        summary = {
            "total_entries": len(self.df),
            "unique_phones": self.df["phone"].nunique(),
            "unique_flows": self.df["flow_name"].nunique(),
            "unique_actions": self.df["action_name"].nunique(),
            "top_flows": self.df["flow_name"].value_counts().to_dict(),
            "top_actions": self.df["action_name"].value_counts().to_dict(),
        }
        print("[DEBUG] Generated summary:", summary)
        return summary
