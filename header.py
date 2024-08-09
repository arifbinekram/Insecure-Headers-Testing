import requests

# Open the file containing URLs
with open("urls.txt", "r") as urls:
    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespace
        if not url:
            continue  # Skip empty lines

        try:
            req = requests.get(url)
            print(url, 'report:')

            # Check X-XSS-Protection header
            try:
                xssprotect = req.headers.get('X-XSS-Protection', None)
                if xssprotect != '1; mode=block':
                    print('X-XSS-Protection not set properly, XSS may be possible:', xssprotect)
            except Exception as e:
                print('X-XSS-Protection not set, XSS may be possible', e)

            # Check X-Content-Type-Options header
            try:
                contenttype = req.headers.get('X-Content-Type-Options', None)
                if contenttype != 'nosniff':
                    print('X-Content-Type-Options not set properly:', contenttype)
            except Exception as e:
                print('X-Content-Type-Options not set', e)

            # Check Strict-Transport-Security header
            try:
                hsts = req.headers['Strict-Transport-Security']
            except KeyError:
                print('HSTS header not set, MITM attacks may be possible')

            # Check Content-Security-Policy header
            try:
                csp = req.headers['Content-Security-Policy']
                print('Content-Security-Policy set:', csp)
            except KeyError:
                print('Content-Security-Policy missing')

            print('----')

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
