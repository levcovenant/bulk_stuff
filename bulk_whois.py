#!/usr/bin/python3

import pythonwhois
import csv


with open('bulk_whois_results.csv', 'w+', newline="") as outfile:
    w = csv.writer(outfile)
    w.writerow(['Domain Name', 'Registrar', 'Expiration Date', 'Nameservers'])
    # outfile.close()


result_list = []
with open('domain_list', 'r') as f:
    for domain in f.readlines():
        # whois_csv(domain.strip())
        whois_data = pythonwhois.get_whois(domain.strip())
        try:
            eDate = ' '.join(str(x) for x in whois_data['expiration_date'])
            result_dict = {
                'domain': domain.strip(),
                'registrar': whois_data['registrar'],
                'edate': eDate,
                'nameservers': whois_data['nameservers']
            }
            result_list.append(result_dict)
        except Exception as e:
            print(e)

with open('bulk_whois_results.csv', 'a+', newline="") as outfile:
    w = csv.writer(outfile)
    for i in result_list:  # eg list or dictionary i'm assuming a list structure
        w.writerow([
            i['domain'],
            i['registrar'],
            i['edate'],
            i['nameservers'],
        ])
print('done')
