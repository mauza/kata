from SECEdgar.filings import Filing

cik = '0000712515'

filing = Filing(cik=cik, filing_type='10-q', count=15)
filing.save('data')
