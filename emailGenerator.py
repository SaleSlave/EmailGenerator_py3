#!/usr/bin/env python3
import argparse
import sys


class EmailGenerator:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Generate email addresses based on names and a specific pattern.")
        parser.add_argument('-d', '--domain', dest='domain', action='store', required=True, help="Target domain (e.g., example.com)")
        parser.add_argument('-f', '--file', dest='file', action='store', required=True, help="Path to the file containing names")
        parser.add_argument('-m', '--method', dest='method', default="fn.ln", action='store', required=False, help="Email generation method/pattern")
        parser.add_argument('-o', '--output_file_path', dest='output_file_path', default="emaillistoutput.txt", action='store', required=False, help="Path to the output file")

        try:
            self.args = parser.parse_args()
        except Exception as err:
            print(f"Error while parsing arguments: {err}")
            sys.exit(1)

    def get_email(self, method, name, domain):
        first_name = ""
        last_name = ""
        middle_name = ""
        first_initial = ""
        middle_initial = ""
        last_initial = ""

        # Split name by whitespaces.
        name_in_a_list = name.split()

        # Robust name parsing to avoid IndexError on single-word names
        first_name = name_in_a_list[0].lower()
        first_initial = first_name[0]
        last_name = name_in_a_list[-1].lower()
        last_initial = last_name[0]

        if len(name_in_a_list) >= 3:
            middle_name = name_in_a_list[1].lower()
            middle_initial = middle_name[0]
        else:
            middle_name = ""
            middle_initial = ""

        # Dictionary mapping methods to email formats using f-strings
        switcher = {
            "fn": f"{first_name}@{domain}",
            "ln": f"{last_name}@{domain}",
            "fnln": f"{first_name}{last_name}@{domain}",
            "fn.ln": f"{first_name}.{last_name}@{domain}",
            "filn": f"{first_initial}{last_name}@{domain}",
            "fi.ln": f"{first_initial}.{last_name}@{domain}",
            "fnli": f"{first_name}{last_initial}@{domain}",
            "fn.li": f"{first_name}.{last_initial}@{domain}",
            "fili": f"{first_initial}{last_initial}@{domain}",
            "fi.li": f"{first_initial}.{last_initial}@{domain}",
            "lnfn": f"{last_name}{first_name}@{domain}",
            "ln.fn": f"{last_name}.{first_name}@{domain}",
            "lnfi": f"{last_name}{first_initial}@{domain}",
            "ln.fi": f"{last_name}.{first_initial}@{domain}",
            "lifn": f"{last_initial}{first_name}@{domain}",
            "li.fn": f"{last_initial}.{first_name}@{domain}",
            "lifi": f"{last_initial}{first_initial}@{domain}",
            "li.fi": f"{last_initial}.{first_initial}@{domain}",
            "fimiln": f"{first_initial}{middle_initial}{last_name}@{domain}",
            "fimi.ln": f"{first_initial}{middle_initial}.{last_name}@{domain}",
            "fnmiln": f"{first_name}{middle_initial}{last_name}@{domain}",
            "fn.mi.ln": f"{first_name}.{middle_initial}.{last_name}@{domain}",
            "fnmnln": f"{first_name}{middle_name}{last_name}@{domain}",
            "fn.mn.ln": f"{first_name}.{middle_name}.{last_name}@{domain}",
            "fn-ln": f"{first_name}-{last_name}@{domain}",
            "fi-ln": f"{first_initial}-{last_name}@{domain}",
            "fn-li": f"{first_name}-{last_initial}@{domain}",
            "fi-li": f"{first_initial}-{last_initial}@{domain}",
            "ln-fn": f"{last_name}-{first_name}@{domain}",
            "ln-fi": f"{last_name}-{first_initial}@{domain}",
            "li-fn": f"{last_initial}-{first_name}@{domain}",
            "li-fi": f"{last_initial}-{first_initial}@{domain}",
            "fimi-ln": f"{first_initial}{middle_initial}-{last_name}@{domain}",
            "fn-mi-ln": f"{first_name}-{middle_initial}-{last_name}@{domain}",
            "fn-mn-ln": f"{first_name}-{middle_name}-{last_name}@{domain}",
            "fn_ln": f"{first_name}_{last_name}@{domain}",
            "fi_ln": f"{first_initial}_{last_name}@{domain}",
            "fn_li": f"{first_name}_{last_initial}@{domain}",
            "fi_li": f"{first_initial}_{last_initial}@{domain}",
            "ln_fn": f"{last_name}_{first_name}@{domain}",
            "ln_fi": f"{last_name}_{first_initial}@{domain}",
            "li_fn": f"{last_initial}_{first_name}@{domain}",
            "li_fi": f"{last_initial}_{first_initial}@{domain}",
            "fimi_ln": f"{first_initial}{middle_initial}_{last_name}@{domain}",
            "fn_mi_ln": f"{first_name}_{middle_initial}_{last_name}@{domain}",
            "fn_mn_ln": f"{first_name}_{middle_name}_{last_name}@{domain}",
        }
        
        # Fallback to default format if method is not found
        return switcher.get(method, f"{first_name}.{last_name}@{domain}")

    def run(self):
        # Read input file and create a list from the lines
        with open(self.args.file, 'r', encoding='utf-8') as f:
            names = f.readlines()
            
        # Strip newline characters and ignore empty lines
        names = [name.strip() for name in names if name.strip()]

        domain = self.args.domain
        method = self.args.method

        # Open output file as writable (using 'with' ensures it closes automatically)
        with open(self.args.output_file_path, 'w', encoding='utf-8') as output_file:
            for name in names:
                email = self.get_email(method, name, domain)
                output_file.write(f"{email}\n")
                
        print(f"Successfully generated emails and saved to {self.args.output_file_path}")


if __name__ == "__main__":
    email_generator = EmailGenerator()
    email_generator.run()
