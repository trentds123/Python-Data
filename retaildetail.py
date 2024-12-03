from mrjob.job import MRJob

class RetailDetail(MRJob):
    

    def mapper(self, _, line):
        fields = line.strip().split('\t')
        # Ensure there are at least 8 fields
        if len(fields) < 8:
            return  # Skip lines with insufficient data
        if fields[0] == "InvoiceNo":
            return  # Skip header line
        invoice_date = fields[4]
        country = fields[7]
        # Validate date format
        if "/" in invoice_date:
            month = invoice_date.split('/')[0]
        else:
            return  # Skip lines with invalid date format
        # Parse quantity and price safely
        try:
            quantity = int(fields[3])
            price = float(fields[5])
        except ValueError:
            return  # Skip lines with invalid numeric data
        amount_spent = quantity * price
        yield (country, month), (amount_spent, price)

    def reducer(self, key, values):
        total_spent = 0
        max_price = 0
        for amount_spent, price in values:
            total_spent += amount_spent
            if price > max_price:
                max_price = price
        yield key, (total_spent, max_price)

if __name__ == '__main__':
    RetailDetail.run()

